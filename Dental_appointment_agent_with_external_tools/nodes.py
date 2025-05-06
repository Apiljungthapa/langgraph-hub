"""
Node functions and logic for the dental appointment scheduling workflow.
"""
from typing import Literal, Dict, List, Any
from typing_extensions import TypedDict
from langchain_core.messages import SystemMessage, ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from typing import Annotated

from config import GOOGLE_API_KEY, LLM_MODEL
from prompts import INITIAL_SYSTEM_PROMPT
from tools import get_scheduling_tools, get_booking_tools, make_confirmation_call
from utils import get_current_time, extract_tool_calls, create_tool_message, log_tool_call

# Type definitions
class MessagesState(TypedDict):
    messages: Annotated[list, add_messages]

# Initialize tools
scheduling_tools = get_scheduling_tools()
booking_tools = get_booking_tools() + [make_confirmation_call]

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    api_key=GOOGLE_API_KEY
)

# Bind tools to LLM
bind_tools = llm.bind_tools(scheduling_tools + [make_confirmation_call])

def call_model(state: MessagesState) -> Dict[str, List[Any]]:
    """
    Agent node that performs the main reasoning and decides which tools to call.
    
    Args:
        state: The current state containing message history
        
    Returns:
        Updated state with the model's response added
    """
    today_time = get_current_time()
    system_prompt = INITIAL_SYSTEM_PROMPT.format(today_time=today_time)
    
    response = bind_tools.invoke(
        [SystemMessage(content=system_prompt)] + state['messages']
    )
    
    return {"messages": [response]}


async def tools_condition(state: MessagesState) -> Literal["find_slots", "tools", "__end__"]:
    """
    Determines the next step in the workflow based on the last message's tool calls.

    Args:
        state: The current state containing message history
        
    Returns:
        - "find_slots": if the tool call is for finding free slots
        - "tools": if there are other tool calls
        - "__end__": if there are no tool calls
    """
    last_message = state['messages'][-1]
    tool_calls = extract_tool_calls(last_message)
    
    if tool_calls:
        for call in tool_calls:
            log_tool_call(call, "tools_condition")
            
            tool_name = call.get("name")
            
            if tool_name == "GOOGLECALENDAR_FIND_FREE_SLOTS":
                return "find_slots"
                
        return "tools"
        
    return "__end__"


async def find_slots(state: MessagesState) -> Dict[str, List[Any]]:
    """
    Executes the GOOGLECALENDAR_FIND_FREE_SLOTS tool if present in tool calls.
    
    Args:
        state: The current state containing message history
        
    Returns:
        Updated state with tool response messages
    """
    last_message = state['messages'][-1]
    tool_messages = []
    tool_calls = extract_tool_calls(last_message)
    
    if tool_calls:
        for call in tool_calls:
            log_tool_call(call, "find_slots")
            
            tool_name = call.get("name")
            tool_id = call.get("id")
            tool_args = call.get("args")
            
            if tool_name == "GOOGLECALENDAR_FIND_FREE_SLOTS":
                # Find the free slots tool from the available tools
                find_free_slots_tool = next(
                    (tool for tool in scheduling_tools if tool.name == tool_name),
                    None
                )
                
                if find_free_slots_tool:
                    # Call the tool and create a response message
                    result = find_free_slots_tool.invoke(tool_args)
                    tool_messages.append(
                        create_tool_message(tool_name, tool_id, result)
                    )
    
    return {"messages": tool_messages}


# Create tool nodes
tool_node = ToolNode(booking_tools)