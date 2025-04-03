import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import markdown
from chat_manager import ChatManager  # Import the ChatManager class

app = Flask(__name__)
chat_manager = ChatManager()


class ChatThread:
    def __init__(self, thread_name="default", system_prompt="You are a PhD-level mathematician, expert programmer in all languages, and approach every tasks with software engineering principles, using Australian and British spelling.",
                 model="grok-2-latest"):
        self.client = OpenAI(
            api_key=os.environ.get("X_API_KEY"),
            base_url="https://api.x.ai/v1",
        )
        self.thread_name = thread_name
        self.messages = chat_manager.load_chat(self.thread_name)
        if not self.messages:
            self.messages = [{"role": "system", "content": system_prompt}]
        self.model = model

    def add_message(self, content, role="user"):
        self.messages.append({"role": role, "content": content})
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        assistant_message = completion.choices[0].message
        self.messages.append({
            "role": "assistant",
            "content": assistant_message.content
        })
        chat_manager.save_chat(self.thread_name, self.messages)
        formatted_content = markdown.markdown(
            assistant_message.content,
            extensions=['fenced_code']
        )
        return formatted_content

    def get_history(self):
        return [
            {
                "role": msg["role"],
                "content": markdown.markdown(msg["content"], extensions=['fenced_code'])
                if msg["role"] == "assistant" else msg["content"]
            }
            for msg in self.messages
        ]

    def clear_history(self):
        system_prompt = self.messages[0]
        self.messages = [system_prompt]
        chat_manager.save_chat(self.thread_name, self.messages)


chat_thread = ChatThread()


@app.route('/')
def index():
    return render_template('index.html', messages=chat_thread.get_history(), threads=chat_manager.list_chats())


@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    if message:
        message = message.replace("<br>", "\n").replace("<tab>", "\t")
        response = chat_thread.add_message(message)
        return jsonify({
            'status': 'success',
            'response': response,
            'messages': chat_thread.get_history()
        })
    return jsonify({'status': 'error', 'message': 'No message provided'})


@app.route('/clear_chat', methods=['POST'])
def clear_chat():
    chat_thread.clear_history()
    return jsonify({
        'status': 'success',
        'messages': chat_thread.get_history()
    })


@app.route('/switch_thread', methods=['POST'])
def switch_thread():
    thread_name = request.json.get('thread_name')
    global chat_thread
    chat_thread = ChatThread(thread_name=thread_name)
    return jsonify({
        'status': 'success',
        'messages': chat_thread.get_history()
    })


@app.route('/delete_thread', methods=['POST'])
def delete_thread():
    thread_name = request.json.get('thread_name')
    success = chat_manager.delete_chat(thread_name)
    return jsonify({
        'status': 'success' if success else 'error',
        'threads': chat_manager.list_chats()
    })

@app.route('/create_thread', methods=['POST'])
def create_thread():
    thread_name = request.json.get('thread_name')
    if thread_name:
        global chat_thread
        chat_thread = ChatThread(thread_name=thread_name)
        chat_manager.save_chat(thread_name, chat_thread.messages)
        return jsonify({
            'status': 'success',
            'threads': chat_manager.list_chats()
        })
    return jsonify({'status': 'error', 'message': 'No thread name provided'})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
