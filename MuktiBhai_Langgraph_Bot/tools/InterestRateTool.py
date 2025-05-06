from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap
from langchain.schema.output_parser import StrOutputParser
from bank_info.interestrates import rate
from utils.getLLM import get_llm_embedings
from models.toolsSchemas import InterestInput
from langchain.schema.output_parser import StrOutputParser
from langchain_core.tools import tool

output_parser = StrOutputParser()

@tool("interest-rate-tool", args_schema=InterestInput, return_direct=True)
def resultInterestRate(query:str):
        """
        ⁡⁣⁢⁣This tool handles financial data on saving deposits, including the highest and lowest interest rates,
        minimum balance requirements, and payment frequencies. It also covers call and current deposit accounts,
        along with fixed deposit products, highlighting the highest and lowest rates, minimum balance, and payment 
        terms. The tool handles information on loan products, microfinance loans, transaction limits, and EMI definitions.
        It also handles general interest rate details, notes on annual charges, and other relevant banking service parameters, 
        offering a comprehensive reference for comparing financial products and services.

        Parameters
        ----------
        query : str
            A question about the financial products or services, such as interest rates, minimum balance, payment terms,
            loan details, on various deposits, ⁡⁣⁢⁣etc.⁡

        """
        
        print(">>>>>>>>>>>>>>>>>>>>> Entering resultInterestRate Tool <<<<<<<<<<<<<<<<<<<<<<<<<\n")

        llm = get_llm_embedings('open_ai').get('llm')

        system_prompt = """
                    You are Mukti Bhai, a helpful Virtual Assistant of Muktinath Bikas Bank.  
                    Only answer from the provided context. 
                    If the answer is unavailable, you are strictly not allowed to answer on your own. Always respond with 'none'.
                    """

        human_prompt = """
                    You are Mukti Bhai, a polite and helpful Virtual Assistant of Muktinath Bikas Bank.
                    Simply answer the question from the given context. Ensure clarity, brevity, and human-like responses.
                    here is the Question inside triple backticks:```{question}```\n
                    here is the Context inside four backticks: ````{interests}````   
                    """
        
        prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", human_prompt)
        ])

        chain = RunnableMap({"interests":lambda x: rate, "question": lambda x: x['question'],}) | prompt | llm | output_parser

        result = chain.invoke({'question':query})
        
        return result
    



