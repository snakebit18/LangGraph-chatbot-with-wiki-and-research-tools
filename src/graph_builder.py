from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages
from typing import Annotated, TypedDict

def build_graph(llm_with_tools, tools):
    """Build and return the Langgraph graph."""
    class State(TypedDict):
        messages: Annotated[list, add_messages]

    def chatbot(state: State):
        """Chatbot node logic."""
        return {"messages": [llm_with_tools.invoke(state["messages"])]}

    # Initialize graph
    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", chatbot)

    # Add tools node
    tool_node = ToolNode(tools=tools)
    graph_builder.add_node("tools", tool_node)

    # Add edges
    graph_builder.add_conditional_edges("chatbot", tools_condition)
    graph_builder.add_edge("tools", "chatbot")
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    return graph_builder.compile()
