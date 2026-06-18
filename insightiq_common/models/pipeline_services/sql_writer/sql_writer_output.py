from pydantic import BaseModel
from pydantic import Field
from typing import Dict, Optional


class SQLWriterOutput(BaseModel):
    sql_query: Optional[str] = Field(description="The SQL query to be executed", default=None)
    user_input_needed: bool = Field(
        description="Whether the user needs to input more information", default=False
    )
    user_input_text: Optional[str] = Field(
        description="The text to be displayed to the user", default=None
    )
