from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap
from langchain.schema.output_parser import StrOutputParser
from models.toolsSchemas import AppointmentInput
from vectorsDB.getvectors import get_vector_store_result
from utils.getLLM import get_llm_embedings
from langchain_core.tools import tool

output_parser = StrOutputParser()



@tool("appointment-tool" , args_schema=AppointmentInput, return_direct=True)
def resultAppointment(query: str):
    """
    This tool is designed to provide responses to appointment-related questions within the context of an online application process.

    Parameters
    ----------
    query : str
        A question regarding the appointment process, submitted by the user.

    Returns
    -------
    dict
        A text-based response that provides relevant information or answers to the user's appointment-related query.  
    """

    print(">>>>>>>>>>>>>>>>>>>>> Entering resultAppointment Tool <<<<<<<<<<<<<<<<<<<<<<<<<\n")

    index_name = 'muktinath'
    name_space = 'muktinathGeneralInquiry_new'

    llm = get_llm_embedings('open_ai').get('llm')


    system_prompt = """
                    You are Mukti Bhai, a helpful Virtual Assistant of Muktinath Bikas Bank.  
                    Only answer from the provided context. 
                    If the answer is unavailable, you are strictly not allowed to answer on your own. Always respond with 'none'.
                    """


    human_prompt = """
       You are virtual assistant of Muktinath Bikas Bank.
    question inside triple backticks:```{question}```
    Contetxt inside four backticks: ````{context}````
    Provide the response based on the context.
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", human_prompt)
    ])

    chain = RunnableMap({ "context":lambda x: get_vector_store_result(x['question'], index_name, name_space), 
                            "question": lambda x: x['question']}) | prompt | llm | output_parser
    
    result = chain.invoke({'question':query})

    result=result + " If you want to take appointment plese click the button below:"

    return result
    



#________________________________This Tool is used for appoitment Related Questions________________________________________
#__________________________________________________Done_____________________________________________________________________
