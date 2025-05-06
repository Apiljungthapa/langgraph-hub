from typing import Literal
from langgraph.prebuilt.tool_node import Command
from models.agentSchemas import AssistantParser
from state.graphState import OverallState
from utils.getLLM import get_llm_embedings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap


def PrimaryAssistant(overall_state: OverallState) -> Command[Literal["Agent_Routers", "__end__"]]:

    print(">>>>>>>>>>>>>>>>>> PrimaryAssistant Running <<<<<<<<<<<<<<<<<<<<<<")

    llm = get_llm_embedings("open_ai")["llm"]

    template = """
                Note:
                You are Mukti Bhai, the chatbot for Muktinath Bikas Bank. Your role is to respond to user queries using only the context provided.

                - For banking-related questions, direct users to "to_routes."
                - For casual inquiries (e.g., "Hello", "How are you?", "What's your name?", "Good morning/afternoon", "Can you chat with me?", "Who are you?"), respond in a friendly, warm, and human-like manner.
                - For questions unrelated to banking or casual interactions, respond with: 
                
                "I am Mukti Bhai, Muktinath Bikas Bank's chatbot. I can only assist with banking-related topics."

                Here is the user's query:\n\n
                User query: {query}
                """

    llm_with_parser = llm.with_structured_output(AssistantParser)

    prompt = ChatPromptTemplate.from_template(template)
    
    chain = RunnableMap({"query": lambda x: x['question']}) | prompt | llm_with_parser

    result = chain.invoke({'question': overall_state['messages']})
    direction = result.routes

    if direction == "to_routes":
        return Command(
            goto="Agent_Routers"
        )
    else:
        # For general responses, without parsing the routes
        chain = RunnableMap({"query": lambda x: x['question']}) | prompt | llm
        result = chain.invoke({'question': overall_state['messages']})

        return Command(
            update={"clean_output": result, "which_payload": "none"},
            goto="__end__"
        )