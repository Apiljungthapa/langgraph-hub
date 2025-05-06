from state.graphState import OverallState
from tools.bankDetailTool import bankDetailsTool
from utils.getLLM import get_llm_embedings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap

def Bank_Details_Handling_Agent(overall_state:OverallState):

    print(">>>>>>>>>>>>>>>>>> Bank_Details_Handling_Agent Running <<<<<<<<<<<<<<<<<<<<<<")

    llm = get_llm_embedings("open_ai")["llm"]

    tools = [bankDetailsTool]

    llm_with_tools=llm.bind_tools(tools)

    template = """
        You are given with the tool bankDetailsTool. pick the correct tool according to the user 
        query and pass valid params to the tool.
        below is the user query: \n
        {query}

         Note:
        If the user submits a query containing two questions, but your tool is not capable of handling both,
        call only the tool that can answer one of the questions. Do not attempt to call both tools if
        your tool is not designed to handle multiple questions at once. Only pass the parameters related 
        the question that your chosen tool can successfully process.
        """

    prompt = ChatPromptTemplate.from_template(template)

    chain = RunnableMap({"query": lambda x: x['question']}) | prompt | llm_with_tools
 
    result = chain.invoke({'question': overall_state['messages']})

    return {"Bank_Details_Tool": result}
