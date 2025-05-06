"""
Graph definition and construction for the dental appointment scheduling workflow.
"""
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from nodes import call_model, find_slots, tools_condition, tool_node, MessagesState

def create_workflow():
    """
    Create and configure the workflow graph.
    
    Returns:
        The compiled workflow application
    """
    # Create a new StateGraph with MessagesState
    workflow = StateGraph(MessagesState)
    
    # Add nodes to the graph
    workflow.add_node("agents", call_model)
    workflow.add_node("find_slots", find_slots)
    workflow.add_node("tools", tool_node)
    
    # Add edges to the graph
    workflow.add_edge("__start__", "agents")
    
    # Add conditional edges from the agents node
    workflow.add_conditional_edges(
        "agents",
        tools_condition,
        {
            "find_slots": "find_slots",
            "tools": "tools",
            "__end__": END
        }
    )
    
    # Add the remaining edges
    workflow.add_edge("find_slots", "agents")
    workflow.add_edge("tools", "agents")
    
    # Create a memory-based checkpointer
    checkpointer = MemorySaver()
    
    # Compile the workflow with the checkpointer
    app = workflow.compile(checkpointer=checkpointer)
    
    return app

def get_workflow_visualization(app):
    """
    Generate a visualization of the workflow graph.
    
    Args:
        app: The compiled workflow application
        
    Returns:
        A Mermaid diagram of the workflow
    """
    from IPython.display import Image
    from langchain_core.runnables.graph import MermaidDrawMethod
    
    return Image(
        app.get_graph().draw_mermaid_png(
            draw_method=MermaidDrawMethod.API,
        )
    )