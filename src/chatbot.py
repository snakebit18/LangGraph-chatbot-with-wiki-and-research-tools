import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools import get_tools
from graph_builder import build_graph

def initialize_chatbot():
    """Initialize the chatbot with tools and return the graph."""
    # Load environment variables
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")

    # Initialize LLM
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It")

    # Bind tools to LLM
    tools = get_tools()
    llm_with_tools = llm.bind_tools(tools=tools)

    # Build and return the graph
    return build_graph(llm_with_tools, tools)