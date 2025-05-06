from langchain_google_genai import ChatGoogleGenerativeAI
from datetime import datetime

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key = "AIzaSyABXJYe_hNItSyazmyOVrjCk5v-0zxhjNg"
)

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig


class Assistant:
    def __init__(self, runnable: Runnable):
        self.runnable = runnable

    def __call__(self, state: dict, config: RunnableConfig) -> dict:
        configuration = config.get("configurable", {})
        patient_id = configuration.get("patient_id", None)

        if not patient_id:
            raise ValueError("No patient_id configured.")

        while True:
            state = {**state, "user_info": patient_id}
            result = self.runnable.invoke(state)

            if not result.tool_calls and (
                not result.content or (
                    isinstance(result.content, list)
                    and not result.content[0].get("text")
                )
            ):
                messages = state["messages"] + [("user", "Please respond properly.")]
                state = {**state, "messages": messages}
            else:
                break

        return {"messages": result}


primary_assistant_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant named 'Apil' for a dental clinic. "
            "Assist patients with booking, rescheduling, and confirming appointments with dentists.\n\n"
            "Workflow:\n"
            "1. If user asks about dentists or schedule, use the doctor listing or slot tool.\n"
            "2. When patient requests a time, use the 'check_doctor_availability' tool before creating an appointment.\n"
            "3. If available, use 'create_appointment'.\n"
            "4. After booking, ask for contact and confirm with 'confirm_appointment_call'.\n"
            "5. If they cancel during the call, use 'cancel_appointment'.\n"
            "6. Always inform the patient of the final appointment status.\n"
            "\nAvoid double-booking. Suggest alternative times if needed.\n"
            "\n<Patient>\n{user_info}\n</Patient>\nCurrent time: {time}."
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now())




assistant = Assistant(primary_assistant_prompt | llm)