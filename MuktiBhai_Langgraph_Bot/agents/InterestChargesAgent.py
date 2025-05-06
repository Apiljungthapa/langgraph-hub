from state.graphState import OverallState
from tools.InterestRateTool import resultInterestRate
from tools.chargesTool import resultFeeCharges
from utils.getLLM import get_llm_embedings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap

def Interest_Charges_Handling_Agent(overall_state:OverallState):

    print(">>>>>>>>>>>>>>>>>> Interest_Charges_Handling_Agent Running <<<<<<<<<<<<<<<<<<<<<<")

    llm = get_llm_embedings("open_ai")["llm"]

    tools = [resultInterestRate, resultFeeCharges]

    llm_with_tools=llm.bind_tools(tools)

    template = """
        You are given with the tool resultInterestRate and resultFeeCharges. pick the correct tool according to the user 
        query and pass valid params to the tool.
        below is the user query: \n
        {query}

        Note:
        this is strict that you must call only one tool at a time. you are strtictly not allowed to call the tool
        more than oen
        """

    prompt = ChatPromptTemplate.from_template(template)

    chain = RunnableMap({"query": lambda x: x['question']}) | prompt | llm_with_tools
 
    result = chain.invoke({'question': overall_state['messages']})

    return {"Interest_Charges_Tool": result}
