from langgraph.graph import StateGraph, START, END
from agents.AnswerHandelingAgent import Answer_Handling_Agent
from agents.AppointmentAgent import Appointment_Handling_Agent
from agents.BankDetailsAgent import Bank_Details_Handling_Agent
from agents.ContactDocumentAgent import Contact_Document_Handling_Agent
from agents.GeneralBankingAgent import General_Banking_Handling_Agent
from agents.InterestChargesAgent import Interest_Charges_Handling_Agent
from agents.PrimaryAssistantAgent import PrimaryAssistant
from agents.RoutingAgent import Agent_Routings
from agents.Tool_Or_End_Conditional_Edge import toolOrend
from state.graphState import OverallState
from langgraph.prebuilt import ToolNode
from tools.InterestRateTool import resultInterestRate
from tools.appointmentTool import resultAppointment
from tools.bankDetailTool import bankDetailsTool
from tools.chargesTool import resultFeeCharges
from tools.contactTool import resultBranchContact
from tools.documentTool import resultDocuments
from tools.generalBankingTool import generalBanking
from utils.visualizeGraph import draw_graph

def Make_Graph():
        graph_builder = StateGraph(OverallState)

        graph_builder.add_node("primary_assistant", PrimaryAssistant)
        graph_builder.add_node("Agent_Routers", Agent_Routings)
        graph_builder.add_node("Interest_Charges_Handling_Agent", Interest_Charges_Handling_Agent)
        graph_builder.add_node("Contact_Document_Handling_Agent", Contact_Document_Handling_Agent)
        graph_builder.add_node("General_Banking_Handling_Agent", General_Banking_Handling_Agent)
        graph_builder.add_node("Bank_Details_Handling_Agent", Bank_Details_Handling_Agent)
        graph_builder.add_node("Appointment_Handling_Agent", Appointment_Handling_Agent)
        graph_builder.add_node("Answer_Handling_Agent", Answer_Handling_Agent)


        graph_builder.add_edge(START, "primary_assistant")
        graph_builder.add_edge("Agent_Routers", "Interest_Charges_Handling_Agent")
        graph_builder.add_edge("Agent_Routers", "Contact_Document_Handling_Agent")
        graph_builder.add_edge("Agent_Routers", "General_Banking_Handling_Agent")
        graph_builder.add_edge("Agent_Routers", "Bank_Details_Handling_Agent")
        graph_builder.add_edge("Agent_Routers", "Appointment_Handling_Agent")


        graph_builder.add_node("Interest_Charges_tool",ToolNode([resultInterestRate, resultFeeCharges],messages_key="Interest_Charges_Tool"))
        graph_builder.add_node("Contact_Document_tool",ToolNode([resultBranchContact, resultDocuments],messages_key="Contact_Document_Tool"))
        graph_builder.add_node("General_Banking_tool",ToolNode([generalBanking],messages_key="General_Banking_Tool"))
        graph_builder.add_node("Bank_Details_tool",ToolNode([bankDetailsTool],messages_key="Bank_Details_Tool"))
        graph_builder.add_node("Appointment_tool",ToolNode([resultAppointment],messages_key="Appointment_Tool"))


        graph_builder.add_conditional_edges("Interest_Charges_Handling_Agent",toolOrend,{"tools": "Interest_Charges_tool","end_it":END})
        graph_builder.add_conditional_edges("Contact_Document_Handling_Agent",toolOrend,{"tools": "Contact_Document_tool","end_it":END})
        graph_builder.add_conditional_edges("General_Banking_Handling_Agent",toolOrend,{"tools": "General_Banking_tool","end_it":END})
        graph_builder.add_conditional_edges("Bank_Details_Handling_Agent",toolOrend,{"tools": "Bank_Details_tool","end_it":END})
        graph_builder.add_conditional_edges("Appointment_Handling_Agent",toolOrend,{"tools": "Appointment_tool","end_it":END})


        graph_builder.add_edge("Interest_Charges_tool", "Answer_Handling_Agent")
        graph_builder.add_edge("Contact_Document_tool", "Answer_Handling_Agent")
        graph_builder.add_edge("General_Banking_tool", "Answer_Handling_Agent")
        graph_builder.add_edge("Bank_Details_tool", "Answer_Handling_Agent")
        graph_builder.add_edge("Appointment_tool", "Answer_Handling_Agent")

        graph_builder.add_edge("Answer_Handling_Agent", END)

        # Compile the graph
        graph = graph_builder.compile()

        return graph

def draw():
    draw_graph(Make_Graph())



