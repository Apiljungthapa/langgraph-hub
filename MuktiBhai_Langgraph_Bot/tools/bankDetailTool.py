from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap
from bank_info.bankdetails import data
from utils.getLLM import get_llm_embedings
from vectorsDB.getvectors import get_vector_store_result
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from models.toolsSchemas import AboutUsInput
from langchain.schema.output_parser import StrOutputParser

output_parser = StrOutputParser()


@tool("bank-details-tool", args_schema=AboutUsInput, return_direct=True)
def bankDetailsTool(query: str, config: RunnableConfig):
    """
    This tool handles all queries related to the bank. It addresses user inquiries about bank_info, leadership 
    (chairman, executive team, directors), departments of the bank (general, inclusive, digital), key contacts
    (CIO, complaints handling officer, compliance officer), committees (strategic committee), regional heads, 
    capital structure, contact email, general banking inquiries, banking hours.
    
    Parameters
    ----------
    query : str
        A question about about the bank's information, leadership, departments, key contacts, committees, regional heads, capital structure, and contact email, general banking inquiries, banking hours.
    ------
    """
    print(">>>>>>>>>>>>>>>>>>>>> Entering bankDetails Tool <<<<<<<<<<<<<<<<<<<<<<<<<\n")
    
    index_name = 'muktinath'
    name_space = 'muktinathDetails_new'
    
    llm = get_llm_embedings('open_ai').get('llm')

    prompt = ChatPromptTemplate.from_messages([

    ("system", """
               You are Mukti Bhai, a helpful Virtual Assistant of Muktinath Bikas Bank.  
                    Only answer from the provided context. 
                    If the answer is unavailable, you are strictly not allowed to answer on your own. Always respond with 'none'.
               """),

    ("human", """
              You are a virtual Assistant of Muktinath Bikas Bank.
                Answer the question from the given details. Ensure clarity, brevity, and human-like responses.
                Provide the user question answer if its available in details or context but dont try to give your 
                own if you dont find it.
                Question inside triple backticks:```{question}```
                Details inside four backticks:````{details}````
                Conside inside five backticks:`````{context}`````
               """)
        ])


    chain = RunnableMap({
        "details": lambda x: data,
        "context": lambda x: get_vector_store_result(x['question'], index_name, name_space),
        "question": lambda x: x['question']
    }) | prompt | llm | output_parser

    result = chain.invoke({'question': query})

    return result


