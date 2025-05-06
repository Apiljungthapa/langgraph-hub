from typing import Literal
from pydantic import BaseModel, Field


class AssistantParser(BaseModel):   
    
    routes: Literal[ "to_routes","general"]

    class Config:
        json_schema_extra = {
            "example": {
                "routes": "to_routes"
            }
        }


class PayLoadParser(BaseModel):   
    
    payLoad_Type: Literal['live_agent', 'appointment', 'complain', 'feedback', 'none'] = Field(description="""
    this column may only contains values from the list ['live_agent', 'appointment', 'complain', 'feedback', 'none']
""")

    class Config:
        json_schema_extra = {
            "example": {
                "payLoad_Type": "appointment"
            }
        }
