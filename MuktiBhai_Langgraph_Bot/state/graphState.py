from typing import Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


class OverallState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    Interest_Charges_Tool: Annotated[list[AnyMessage], add_messages]
    Contact_Document_Tool: Annotated[list[AnyMessage], add_messages]
    General_Banking_Tool: Annotated[list[AnyMessage], add_messages]
    Bank_Details_Tool: Annotated[list[AnyMessage], add_messages]
    Appointment_Tool: Annotated[list[AnyMessage], add_messages]
    clean_output:str
    which_payload:str




    

