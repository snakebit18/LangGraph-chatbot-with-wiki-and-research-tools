import streamlit as st
from chatbot import initialize_chatbot


def main():
    st.title("Langgraph Chatbot with Tools")

    # Initialize the chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = [{'role': 'assistant', 'content': "Hello! How can I assist you today?"}]

    # Initialize the chatbot graph
    graph = initialize_chatbot()

    # Display chat history
    for message in st.session_state.messages:
        st.chat_message(message['role']).write(message['content'])

    # User input
    user_input = st.chat_input(placeholder="You:...")

    if user_input:
        # Append user message to the chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        # Process the user input through the graph
        events = graph.stream({'messages': st.session_state.messages})

        for event in events:
            # Extract and display messages from tools and chatbot
            if 'chatbot' in event:
                chatbot_messages = event['chatbot'].get('messages', [])
                for message in chatbot_messages:
                    if hasattr(message, 'content') and isinstance(message.content, str) and len(message.content) > 0:   
                        st.chat_message("assistant").write(message.content)
                        st.session_state.messages.append({"role": "assistant", "content": message.content})

            if 'tools' in event:
                tool_messages = event['tools'].get('messages', [])
                for message in tool_messages:
                    if not hasattr(message, 'tool_call_id'):
                        message.tool_call_id = "default_tool_call_id"
                    if hasattr(message, 'content') and isinstance(message.content, str) and len(message.content) > 0:
                        st.chat_message("tool").write(message.content)
                        st.session_state.messages.append({"role": "tool", "content": message.content})

if __name__ == "__main__":
    main()

