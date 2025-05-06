from state.graphState import OverallState

# def toolOrend(overall_state: OverallState):
#     messages = next((overall_state[tool] for tool in [
#         "Interest_Charges_Tool", "Contact_Document_Tool", 
#         "General_Banking_Tool", "Bank_Details_Tool", 
#         "Appointment_Tool"] if overall_state[tool]), None)

#     # Ensure that messages is not an empty list
#     if messages:
#         last_message = messages[-1]
#         if last_message.tool_calls:
#             return "tools"
#     return "end_it"

def toolOrend(overall_state: OverallState):
    messages = (overall_state["Interest_Charges_Tool"] if overall_state["Interest_Charges_Tool"] else
                overall_state["Contact_Document_Tool"] if overall_state["Contact_Document_Tool"] else
                overall_state["General_Banking_Tool"] if overall_state["General_Banking_Tool"] else
                overall_state["Bank_Details_Tool"] if overall_state["Bank_Details_Tool"] else
                overall_state["Appointment_Tool"])

    if messages and messages[-1].tool_calls:
        return "tools"
    return "end_it"

