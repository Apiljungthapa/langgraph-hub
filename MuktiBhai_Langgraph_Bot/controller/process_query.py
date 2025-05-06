from models.apiSchemas import QueryParams
from utils.getLLM import get_llm_embedings
from controller.graph import Make_Graph, draw
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig

llm = get_llm_embedings('open_ai').get('llm')

def graph_output(query, sender, metadata, live, source, contact, config: RunnableConfig = None):
    graph = Make_Graph()
    draw()
    
    # Create a default config if not provided
    if config is None:
        config = RunnableConfig(configurable={})
    
    output = graph.invoke({"messages":[HumanMessage(content=query)]})

    configuration = config.get("configurable", {})

    print("configuration ho yo", configuration)
    sender_id = configuration.get("sender_id", None)
    # if not passenger_id:
    #     raise ValueError("No passenger ID configured.")
    
    output, payload = output["clean_output"].content, output["which_payload"]

    if payload=="liveagent":
        message = {
            "type": "quick_reply",
            "data": [
                {    
                    "title": "Talk to Live Agent",
                    "payload": "I want to talk to liveagent"
                },
            ],
            "user_details": {
                "name": "",
                "mobileNumber": ""
            }
        }
        message = {"custom": message}
        return message

    elif payload=="contact":
        message = {
            "type": "quick_reply",
            "data": [
                {    
                    "title": "Contact",
                    "payload": "I want to contact"
                },
            ],
            "user_details": {
                "name": "",
                "mobileNumber": ""
            }
        }
        message = {"custom": message}
        return message
    
    elif payload=="appointment":
        message = {
            "type": "quick_reply",
            "data": [
                {    
                    "title": "Take appointment",
                    "payload": "Take appointment"
                },
            ],
            "user_details": {
                "name": "",
                "mobileNumber": ""
            }
        }
        message = {"custom": message}

        print("message", message)
        return message

    else:
        return {"text": output, "payload": payload}

def process_query_controller(**request_params: QueryParams):
    query = request_params['query']
    sender = request_params['sender']
    sender = str(sender)
    metadata = request_params['metadata']
    live = request_params['live']
    contact = request_params['contact']
    source = request_params['source']

    # Create a default RunnableConfig if needed
    config = RunnableConfig(configurable={
        "sender_id": sender,
    })

    return graph_output(
        query=query, 
        sender=sender, 
        metadata=metadata, 
        live=live, 
        source=source, 
        contact=contact, 
        config=config
    )