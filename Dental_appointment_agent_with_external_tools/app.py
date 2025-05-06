"""
Main execution script for the dental appointment scheduling bot.
"""

import asyncio
from langchain_core.messages import HumanMessage
from utils import print_message
from workflow import create_workflow, get_workflow_visualization
from IPython.display import Image, display
from langchain_core.runnables.graph import CurveStyle, MermaidDrawMethod, NodeStyles


async def run_workflow(initial_message: str, thread_id: str = "1"):
    """
    Run the appointment scheduling workflow with the given initial message.
    
    Args:
        initial_message (str): The initial message from the user.
        thread_id (str): An identifier for the conversation thread.
        
    Returns:
        app: The executed workflow application instance.

    """
    # Create the workflow
    app = create_workflow()

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    initial_state = {
        "messages": [
            HumanMessage(content=initial_message)
        ]
    }


    print("📤 Starting the appointment scheduling flow...\n")
    async for chunk in app.astream(initial_state, config=config, stream_mode="values"):
        response_message = chunk["messages"][-1]
        print_message(response_message)

    return app


if __name__ == "__main__":

    # initial_message = "Book my appointment for the day after tomoroow at 11 pm"
    initial_message = "yes do it appointment"

    asyncio.run(run_workflow(initial_message))
