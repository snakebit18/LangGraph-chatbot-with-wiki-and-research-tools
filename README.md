# Langgraph Chatbot

This project implements a chatbot using the Langgraph framework and Streamlit for the user interface. The chatbot leverages the capabilities of the Langchain API to provide intelligent responses based on user input.

## Project Structure

```
LanggraphChatbot
├── src
│   ├── app.py          # Entry point for the Streamlit application
│   ├── chatbot.py      # Contains chatbot logic and state management
│   └── utils
│       └── __init__.py # Utility functions and classes
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd LanggraphChatbot
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   ```

## Usage

To run the Streamlit application, execute the following command in your terminal:

```bash
streamlit run src/app.py
```

Once the application is running, you can interact with the chatbot through the web interface.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.