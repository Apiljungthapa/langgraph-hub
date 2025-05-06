from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap
from utils.getLLM import get_llm_embedings
from vectorsDB.getvectors import get_vector_store_result
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from models.toolsSchemas import DocumentsInput
from langchain.schema.output_parser import StrOutputParser

output_parser = StrOutputParser()

@tool("documents-inquiry-tool", args_schema=DocumentsInput, return_direct=True)
def resultDocuments(query: str, config: RunnableConfig):
    """
    This tool provides information on the required documents for opening different types of bank accounts, 
    applying for loans, and conducting transactions. It includes details on identification, guarantor requirements, 
    income verification, and other necessary paperwork for various financial services. Additionally, it outlines 
    the compliance guidelines for loan applications and account registrations. It also covers the types of online
    loan accounts and online accounts that users can apply for.
    
    Parameters
    ----------
    query : str
        A question regarding the required documents for bank accounts, loan applications, or transactions. This 
        could include inquiries about specific account types, loan categories, or general banking requirements.
   
    Returns
    -------
    str
        A response that provides the necessary documentation and information based on the user's query.
    """


    index_name = 'muktinath'
    name_space = 'muktinathDocuments_new' 

    llm = get_llm_embedings('open_ai').get('llm')

    print(">>>>>>>>>>>>>>>>>>>>> Entering resultDocuments Tool <<<<<<<<<<<<<<<<<<<<<<<<<\n")

    system_prompt = """
                    You are Mukti Bhai, a helpful Virtual Assistant of Muktinath Bikas Bank.  
                    Only answer from the provided context. 
                    If the answer is unavailable, you are strictly not allowed to answer on your own. Always respond with 'none'.
                    khata and account is same.
                     Note: If the question is too general (e.g., "How to create a bank account?"), 
                     provide the answer specific to accounts like NORMAL SAVINGS ACCOUNT.
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

    chain = RunnableMap({"context":lambda x: get_vector_store_result(x['question'], index_name, name_space),
                            "question": lambda x: x['question']}) | prompt | llm | output_parser
    
    result = chain.invoke({'question': query})

    
    return result
