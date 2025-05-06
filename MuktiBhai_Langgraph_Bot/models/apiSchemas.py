from pydantic import BaseModel;
from fastapi import Query
from typing import Optional

class QueryParams(BaseModel):
    query: str = Query(..., description="The user's query or search term.")
    sender: str = Query(..., description="The identifier of the user sending the query.")
    source: Optional[str] = Query(default=None, description="The source of the query (optional).")
    metadata:str=Query(...,description="Additional Info of the user")