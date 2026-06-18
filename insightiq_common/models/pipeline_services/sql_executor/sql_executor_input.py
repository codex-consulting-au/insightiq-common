from pydantic import BaseModel
from pydantic import Field


class SQLExecutorInput(BaseModel):
    sql_query: str = Field(description="The SQL query to be executed")
