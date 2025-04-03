# xai: An AI Chat Application

Welcome to **xai**, a Flask-based web application designed to interact with the xAI API. This application provides a user-friendly interface for engaging in conversations with an AI model, managing multiple chat threads, and storing conversation history.

## Features

- **AI-Powered Conversations**: Utilise the xAI API to generate responses to user queries.
- **Multiple Chat Threads**: Create, switch between, and manage multiple conversation threads.
- **Persistent Chat History**: Save and load conversation history for each thread.
- **Markdown Support**: Render AI responses in Markdown format for enhanced readability.

## Installation

To set up and run the xai application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/xai.git
   cd xai
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.10+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   Set the `X_API_KEY` environment variable with your xAI API key:
   ```bash
   export X_API_KEY=your_xai_api_key
   ```

4. **Run the Application**:
   Start the Flask development server:
   ```bash
   python xai.py
   ```
   The application will be available at `http://localhost:5001`.

## Usage

### Web Interface

- **Home Page**: Access the main chat interface at `http://localhost:5001`.
- **Sending Messages**: Type your message in the input field and press Enter or click the send button.
- **Thread Management**:
  - **Create Thread**: Use the "Create New Thread" feature to start a new conversation.
  - **Switch Thread**: Select a different thread from the list to continue or review previous conversations.
  - **Delete Thread**: Remove unwanted threads from the list.
  - **Clear Chat**: Clear the current thread's conversation history.

### API Endpoints

The following endpoints are available for programmatic interaction:

- **GET /**: Render the main chat interface.
- **POST /send_message**: Send a message and receive a response.
- **POST /clear_chat**: Clear the current chat history.
- **POST /switch_thread**: Switch to a different chat thread.
- **POST /delete_thread**: Delete a specific chat thread.
- **POST /create_thread**: Create a new chat thread.

## Code Structure

- **xai.py**: Main application file containing Flask routes and AI interaction logic.
- **chat_manager.py**: Handles chat thread management and persistence.
- **templates/index.html**: HTML template for the web interface.
- **static/**: Directory for CSS and JavaScript files (if applicable).

## Key Classes and Functions

### `ChatThread`

This class manages individual chat threads:

- **Initialisation**: Sets up the thread with a name, system prompt, and model.
- **add_message**: Adds a user message, generates an AI response, and updates the chat history.
- **get_history**: Retrieves the formatted chat history.
- **clear_history**: Clears the chat history, keeping only the system prompt.

### `ChatManager`

This class handles chat thread persistence:

- **save_chat**: Saves a chat thread's history to a JSON file.
- **load_chat**: Loads a chat thread's history from a JSON file.
- **list_chats**: Lists all saved chat threads.
- **delete_chat**: Deletes a specific chat thread.

## Configuration

- **API Key**: Set the `X_API_KEY` environment variable with your xAI API key.
- **Model**: The default model used is `grok-2-latest`. You can modify this in the `ChatThread` class.
- **System Prompt**: The default system prompt defines the AI's persona and behaviour. You can customise this in the `ChatThread` class.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with your improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- xAI for providing the API and model access.
- The open-source community for various libraries and tools used in this project.
This README provides a comprehensive overview of the xai application, including installation instructions, usage guidelines, code structure explanation, and configuration details. It follows software engineering principles and uses British and Australian spelling conventions as requested.
