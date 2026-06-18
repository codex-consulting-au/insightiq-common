from pydantic import BaseModel
from pydantic import Field


class SQLExplainerOutput(BaseModel):
    explanation: str = Field(
        description="Explanation of the query execution plan or validation details",
        default=None,
    )
    is_valid: bool = Field(
        description="Whether the SQL query is valid and can be executed", default=None
    )
    error_message: str = Field(
        description="Error message if the query is invalid", default=None
    )
