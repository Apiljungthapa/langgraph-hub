"""
Tool definitions and setup for the dental appointment scheduling bot.
"""
from composio_langgraph import Action, ComposioToolSet
from config import COMPOSIO_API_KEY

def initialize_tools():
    """Initialize and configure the ComposioToolSet with necessary API keys."""
    tools = ComposioToolSet(api_key=COMPOSIO_API_KEY)
    return tools

def get_scheduling_tools():
    """
    Get tools for the scheduling process including calendar free slots check,
    event creation, and email draft creation.
    """
    tools = initialize_tools()
    scheduling_tools = tools.get_tools(
        actions=[
            Action.GOOGLECALENDAR_FIND_FREE_SLOTS,
            Action.GOOGLECALENDAR_CREATE_EVENT,
            Action.GMAIL_CREATE_EMAIL_DRAFT
        ]
    )
    return scheduling_tools

def get_booking_tools():
    """
    Get tools specifically for booking actions after slots have been found.
    """
    tools = initialize_tools()
    booking_tools = tools.get_tools(
        actions=[
            Action.GOOGLECALENDAR_CREATE_EVENT,
            Action.GMAIL_CREATE_EMAIL_DRAFT
        ]
    )
    return booking_tools

def make_confirmation_call(phone_number: str) -> str:
    """
    Make a confirmation call to the given phone number.
    
    Args:
        phone_number: The phone number to call for confirmation
        
    Returns:
        A confirmation message
    """
    # This is a placeholder for actual implementation
    return f"Confirmation call scheduled to {phone_number}"

def get_all_tools():
    """
    Get all tools including scheduling tools and the confirmation call tool.
    """
    scheduling_tools = get_scheduling_tools()
    booking_tools = get_booking_tools()
    
    # Add the make_confirmation_call tool to booking tools
    booking_tools_with_call = booking_tools + [make_confirmation_call]
    
    return {
        "scheduling_tools": scheduling_tools,
        "booking_tools": booking_tools_with_call
    }