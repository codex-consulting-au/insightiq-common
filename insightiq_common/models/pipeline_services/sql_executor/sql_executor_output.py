from pydantic import BaseModel
from pydantic import Field
from typing import List, Dict, Any
from enum import Enum

from insightiq_common.models.common.entities.data_output import DataOutput


# TODO: Add more error types
class SQLExecutorErrorType(Enum):
    OTHER = "other"


class SQLExecutorOutput(BaseModel):
    data_output: DataOutput = Field(description="The data output", default=None)
    error_type: SQLExecutorErrorType = Field(
        description="The type of error", default=None
    )
    error_message: str = Field(
        description="The error message returned from the SQL query", default=None
    )
