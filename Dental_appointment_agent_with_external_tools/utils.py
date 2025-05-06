"""
Utility functions and helpers for the dental appointment scheduling bot.
"""
from datetime import datetime
from typing import Dict, Any
from langchain_core.messages import ToolMessage

def get_current_time() -> str:
    """Get the current time in ISO format."""
    return datetime.now().isoformat()

def format_system_prompt(prompt_template: str, **kwargs) -> str:
    """Format the system prompt with the given kwargs."""
    return prompt_template.format(**kwargs)

def extract_tool_calls(message: Any) -> list:
    """
    Extract tool calls from a message if they exist.
    
    Args:
        message: A message object that might contain tool_calls
        
    Returns:
        A list of tool calls or an empty list if none exist
    """
    if hasattr(message, "tool_calls") and message.tool_calls:
        return message.tool_calls
    return []

def create_tool_message(tool_name: str, tool_id: str, content: Any) -> ToolMessage:
    """
    Create a ToolMessage with the given parameters.
    
    Args:
        tool_name: The name of the tool
        tool_id: The ID of the tool call
        content: The content/result of the tool call
        
    Returns:
        A ToolMessage object
    """
    return ToolMessage(name=tool_name, tool_call_id=tool_id, content=content)

def print_message(message: Any) -> None:
    """
    Pretty print a message if it has content.
    
    Args:
        message: The message to print
    """
    if hasattr(message, 'content'):
        message.pretty_print()
    else:
        print("⚠️ Received a message without a 'content' attribute.")

def log_tool_call(call: Dict[str, Any], context: str = "") -> None:
    """
    Log a tool call for debugging purposes.
    
    Args:
        call: The tool call dictionary
        context: Additional context about where the call is happening
    """
    print("________________________________________")
    print(f"Tool calling in {context}", call)
    print("________________________________________")