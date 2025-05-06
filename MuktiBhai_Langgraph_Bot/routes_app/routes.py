from dotenv import load_dotenv
from fastapi import APIRouter
from models.apiSchemas import QueryParams
from langchain_community.callbacks.manager import get_openai_callback
from routes_app.menus import data
from controller.process_query import process_query_controller
# from Chains.postrating import post_rate
import json
import os
# from Chains.sendrating import send_rating
from routes_app.agentManager import agent_manager
load_dotenv()


router = APIRouter()


@router.get('/muktibhai')
def process_query(query:str,sender:str, source:str,metadata:str):

    is_exist_response=data.get(query,None)  # from routes_app.menus import data

    #________________________________________________________________________________________________________________

    if is_exist_response:
        result={"custom":is_exist_response} 
        return result
    
    #________________________________________________________________________________________________________________

    # if query in ["/customer_rating"]:
    #     metadata = json.loads(metadata)
    #     print("metadata here upper field>>>>>>>", metadata)

    #     agent_id = metadata.get("agentId")
    #     print("agnet id from metadata",agent_id)

    #     agent_manager.set_agent_id(agent_id)  # Store the agentId in the class

    #     return send_rating(agent_id, source=source)

    # _________________________________________________________________________________________________________________

    # if query in ["agent_rating:1","agent_rating:2","agent_rating:3","agent_rating:4","agent_rating:5"]:
    #     agent_id = agent_manager.get_agent_id()
    #     print("agnetID>>>>>",agent_id)

    #     response=post_rate(query, source=source, agentid=agent_id, senderid=sender)
    #     print("response here is >>>>>",response)
    #     return response
    
    #_________________________________________________________________________________________________________________

    menu_query = ["menu", "redirect to menu", "/menu", "home", "get started"]
    if query.lower() in [item.lower() for item in menu_query]:
        is_exist_response=data.get("/Menu")
        result={"custom":is_exist_response}
        return result
    
    
    with get_openai_callback() as cb:
        request_params:QueryParams={
        "query":query,
        "sender":sender,        
        "source":source,
        "metadata":metadata,
        "live":False,
        "contact":False
        }         
        result = process_query_controller(**request_params)
        print(str(cb))
    return {"result":result}