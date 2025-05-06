from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap
from utils.getLLM import get_llm_embedings
from vectorsDB.getvectors import get_vector_store_result
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from models.toolsSchemas import chargesInput
from langchain.schema.output_parser import StrOutputParser
output_parser = StrOutputParser()


@tool("fee-charges-tool", args_schema=chargesInput, return_direct=True)
def resultFeeCharges(query:str, config: RunnableConfig):
        
        """
        This tool manages the "Standard Tariff of Charges, 2081" from Muktinath Bikas Bank Ltd.,
        covering all applicable fees. It includes charges for customer services (balance certificates, statements, cheques),
        banking services (branch, electronic clearing, digital banking, ATM transactions, lockers, remittances), 
        and credit facilities (interest rates, admin fees, renewal, penalties). It details fees for loans, bank guarantees 
        (based on contractor classification), and offers waiver provisions with specific authorization levels. 
        Special concessions for bank staff and miscellaneous charges, such as insurance on gold/silver loans and 
        letter of credit fees, are also included.

        Parameters
        ----------
        query : str
            A question or inquiry related to the tariff of charges.

        Returns
        -------
            A detailed response that provides the relevant fee or service information based on the query.
        """
        
        print(">>>>>>>>>>>>>>>>>>>>> Entering resultFeeCharges Tool <<<<<<<<<<<<<<<<<<<<<<<<<\n")

        system_prompt = """
                    You are Mukti Bhai, a helpful Virtual Assistant of Muktinath Bikas Bank.  
                    Only answer from the provided context. 
                    If the answer is unavailable, you are strictly not allowed to answer on your own. Always respond with 'none'.
                    """
        

        human_prompt = """
        You are a polite and helpful Virtual Assistant of Muktinath Bikas Bank.
        Your task is to answer the question from the given context in human-like, accurate and concise form.
        here is the Question inside triple backticks:```{question}```  \n 
        here is Context inside double backticks:``{context}``
        """

        index_name = 'muktinath'
        name_space = 'charges_muktinath'

        llm = get_llm_embedings('open_ai').get('llm')

        prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", human_prompt)])

        chain = RunnableMap({"context":lambda x: get_vector_store_result(x['question'], index_name, name_space),
                            "question": lambda x: x['question']}) | prompt | llm | output_parser

        result = chain.invoke({'question':query})

        return result 
    
