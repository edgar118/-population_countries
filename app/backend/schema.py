from pydantic import BaseModel
from typing import List, Optional

class Country_schema(BaseModel):    
    countries: List[str]