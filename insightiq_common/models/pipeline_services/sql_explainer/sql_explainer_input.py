from pydantic import BaseModel
from pydantic import Field


class SQLExplainerInput(BaseModel):
    sql_query: str = Field(description="The SQL query to be validated and explained")
