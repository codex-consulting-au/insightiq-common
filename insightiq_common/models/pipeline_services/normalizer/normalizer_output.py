from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional


class NormalizerOutputType(Enum):
    USER_INPUT_NEEDED = "user_input_needed"
    FRESH_QUESTION = "fresh_question"
    FOLLOW_UP_QUESTION_SIMPLE_SQL_CHANGE = "follow_up_question_simple_sql_change"
    FOLLOW_UP_QUESTION_COMPLEX_SQL_CHANGE = "follow_up_question_complex_sql_change"
    FOLLOW_UP_QUESTION_VISUALIZATION_CHANGE = "follow_up_question_visualization_change"


class NormalizerOutput(BaseModel):
    sanitised_message: Optional[str] = Field(description="The sanitised message", default=None)
    user_input_needed: bool = Field(
        description="Whether the user needs to input more information", default=False
    )
    user_input_text: Optional[str] = Field(
        description="The text to be displayed to the user", default=None
    )
    sql_query: Optional[str] = Field(
        description="SQL query only if it is a follow up question and the chnage is really small",
        default=None,
    )
    output_type: Optional[NormalizerOutputType] = Field(
        description="The type of output", default=NormalizerOutputType.FRESH_QUESTION
    )
