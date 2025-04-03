import os
import json

class ChatManager:
    CHAT_DIR = "chats"

    def __init__(self):
        os.makedirs(self.CHAT_DIR, exist_ok=True)

    def save_chat(self, thread_name, messages):
        """Save chat history to a JSON file"""
        file_path = os.path.join(self.CHAT_DIR, f"{thread_name}.json")
        with open(file_path, "w") as file:
            json.dump(messages, file, indent=4)

    def load_chat(self, thread_name):
        """Load chat history from a JSON file"""
        file_path = os.path.join(self.CHAT_DIR, f"{thread_name}.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                return json.load(file)
        return []

    def list_chats(self):
        """List all saved chat threads"""
        return [f[:-5] for f in os.listdir(self.CHAT_DIR) if f.endswith(".json")]

    def delete_chat(self, thread_name):
        """Delete a specific chat thread"""
        file_path = os.path.join(self.CHAT_DIR, f"{thread_name}.json")
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
