from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap
from langchain.schema.output_parser import StrOutputParser
from bank_info.savingaccount import saving_accounts
from utils.getLLM import get_llm_embedings
from models.toolsSchemas import GeneralInput
from langchain.schema.output_parser import StrOutputParser
from langchain_core.tools import tool
from vectorsDB.getvectors import get_vector_store_result

output_parser = StrOutputParser()
 
@tool("general-banking-tool", args_schema=GeneralInput, return_direct=True)
def generalBanking(query:str):
    """
    Handles general banking inquiries, covering various aspects of banking services, including:

    - Banking card-related information.
    - Digital banking services.
    - General loan-related queries (e.g., "What types of loans do you offer?").
    - FAQs and common banking inquiries.
    - Inclusive banking services.
    - Information about different banking products.
    - Details regarding savings accounts (Bachat Khata).

    Parameters
    ----------
    query : str  
         A customer's text-based inquiry related to banking services, including cards, loans, digital banking savings accounts, common banking services.  
    """
    print(">>>>>>>>>>>>>>>>>>>>> Entering generalBanking Tool <<<<<<<<<<<<<<<<<<<<<<<<<\n")

    
    template = """
        You are Mukti Bhai, a polite and helpful Virtual Assistant of Muktinath Bikas Bank.
        Your task is to answer the question from the given context and Saving account information in human-like, accurate and concise form.
        Context inside double backticks:``{context}``
        Question inside triple backticks:```{question}```
        Saving account information inside four backticks:````{saving_account}
        Provide more desriptive response.    
        """

    index_name = 'muktinath'
    name_space = 'muktinathGeneralInquiry_new'

    llm = get_llm_embedings('open_ai').get('llm')

    prompt = ChatPromptTemplate.from_template(template)

    chain = RunnableMap({
        "context":lambda x: get_vector_store_result(x['question'], index_name, name_space),
        "saving_account":lambda x: saving_accounts,
        "question": lambda x: x['question']
    }) | prompt | llm | output_parser

    result = chain.invoke({'question':query})
  
    return result
    

 
