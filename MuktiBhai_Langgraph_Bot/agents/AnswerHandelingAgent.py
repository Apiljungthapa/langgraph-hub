from models.agentSchemas import PayLoadParser
from state.graphState import OverallState
from utils.getLLM import get_llm_embedings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap


def getClearContext(agents,state):
    all_agent_context = ""
    for state_key in agents:
        list_of_messages=(state[state_key])
        for i in  list_of_messages:
            all_agent_context +=i.content+", "
    return (all_agent_context.replace(".",""))



def Answer_Handling_Agent(overall_state:OverallState):

    print(">>>>>>>>>>>>>>>>>> Answer_Handling_Agent Running <<<<<<<<<<<<<<<<<<<<<<")

    llm = get_llm_embedings("open_ai")["llm"]

    template = """
                You are given a user query and context. Your task is to answer the user query using only the information provided in the context. 
                Ensure that your answer is strictly related to the context and avoid making any assumptions or adding extra information. 
                if the user query is not in the context then you for that information please contact with the bank.

                User Query:
                {query}

                Context:
                {context}

                """
    
    payload_template = """ 
        You are the classifier who identifies the user's question and its answer. 
        You are given the question and answer. By analyzing the question, tell me if it's related to 
        'live_agent', 'appointment', 'complain', 'feedback', or 'none'.
        If the user is asking for an appointment or the application process, put `payLoad_Type` as 'appointment'.
        If the user is asking for a complaint, put `payLoad_Type` as 'complain'.
        If the user is asking for feedback, put `payLoad_Type` as 'feedback'.
        If the user is asking for a live agent, put `payLoad_Type` as 'live_agent'.
        If the user wants to talk with a live person in the bank, then put `payLoad_Type` as 'live agent'.
        If the user is not asking for any of the above, then put 'none'. \n\n

        Here is the user query: {query}\n\n

        Here is the answer: {answer}
        """
    
    agents = list(overall_state.keys())[:-6:-1]

    contexts = getClearContext(agents,overall_state)

    prompt = ChatPromptTemplate.from_template(template)

    chain = RunnableMap({"query": lambda x: x['question'],
                         "context": lambda x: contexts}) | prompt | llm

    result = chain.invoke({'question': overall_state['messages']})

    llm_with_parser = llm.with_structured_output(PayLoadParser)

    payload_prompt = ChatPromptTemplate.from_template(payload_template)

    payload_chain = RunnableMap({"query": lambda x: x['question'],
                         "answer": lambda x: x['clean_output']}) | payload_prompt | llm_with_parser

    payload_result = payload_chain.invoke({'question': overall_state['messages'], 'clean_output': result})

    payload_result = payload_result.payLoad_Type

    print("payload_result: ",payload_result)

    return {"clean_output": result,"which_payload": payload_result}
