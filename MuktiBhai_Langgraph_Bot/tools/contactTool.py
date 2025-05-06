from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap
from utils.getLLM import get_llm_embedings
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from models.toolsSchemas import ContactInput
from langchain.schema.output_parser import StrOutputParser
from bank_info.contactnumbers import contact

output_parser = StrOutputParser()

@tool("branch-info-tool", args_schema=ContactInput, return_direct=True)
def resultBranchContact(query: str, config: RunnableConfig):
    """
    This tool is designed to handle and manage contact information for multiple branches of a bank.
    It can be used to retrieve specific branch details such as the branch name, address, district, phone number, and email address.

    Parameters
    ----------
    query : str
        A question about the contact details of Muktinath Bikas Bank. This could be the name of a branch, its location,
        or any other key attribute of the branch (e.g., "Amarsingh Chowk Branch", "contact of Adamghat Branch").

    Returns
    -------
    str
        A text-based response answering the user's query based on the bank's branch information.
    """
    print(">>>>>>>>>>>>>>>>>>>>> Entering resultBranchContact Tool <<<<<<<<<<<<<<<<<<<<<<<<<\n")
    
    llm = get_llm_embedings('open_ai').get('llm')

    system_prompt = """
    You are Mukti Bhai, a helpful Virtual Assistant of Muktinath Bikas Bank. 
    You provide the contact details of the bank's branches, including phone numbers, email, contact information, and address.
    Only answer based on the provided context. 
    If the answer is unavailable, you are strictly not allowed to provide an answer on your own. Always respond with 'none'.
    """

    human_prompt = """
        You are Mukti Bhai, a polite and helpful Virtual Assistant of Muktinath Bikas Bank.
        Answer the question from the given context. Ensure clarity, brevity, and human-like responses.
        Here is the question inside triple backticks:```{question}``` \n
        Here is the context inside double backticks:``{context}``
        
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", human_prompt)
    ])

    chain = RunnableMap({"context":lambda x: contact, "question": lambda x: x['question']}) | prompt | llm | output_parser 
    
    result = chain.invoke({'question': query})

    return  result
