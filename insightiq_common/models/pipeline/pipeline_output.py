from pydantic import BaseModel
from pydantic import Field
from enum import Enum
from typing import List, Dict, Optional
import uuid

from insightiq_common.models.pipeline.pipeline_stages import PipelineStage
from insightiq_common.models.common.entities.data_output import DataOutput
from insightiq_common.models.common.entities.message import Message


class DetailedErrorType(Enum):
    NormalisationError = "normalisation_error"
    SQLWriterError = "sql_writer_error"
    SQLExecutorError = "sql_executor_error"
    SQLExecutionError = "sql_execution_error"
    UserClarificationError = "user_clarification_error"
    OtherError = "other_error"


class OutputType(Enum):
    DataGeneratedSuccessfully = "data_generated_successfully"
    VisualisationGeneratedSuccessfully = "visualisation_generated_successfully"
    UserClarificationNeeded = "user_clarification_needed"
    PipelineError = "pipeline_error"


class PipelineOutput(BaseModel):
    session_id: str = Field(
        description="The session id",
    )
    user_id: str = Field(
        description="The user id",
    )
    user_query: Message = Field(description="The user query")
    conversation_history: Optional[List[Message]] = Field(
        description="The conversation history", default=None
    )
    last_output: Optional["PipelineOutput"] = Field(
        description="The last output", default=None
    )
    finished_pipeline_stages: List[PipelineStage] = Field(
        description="The finished pipeline stages", default=[]
    )
    # TODO: Add validation output
    # validation_output:bool = Field(description="Whether the validation was successful", default=False)
    sanitised_query: Optional[str] = Field(description="The sanitised query", default=None)
    user_clarification_needed: bool = Field(
        description="Whether user clarification is needed", default=False
    )
    user_clarification_question: Optional[str] = Field(
        description="The user clarification question", default=None
    )
    tables_referenced: Optional[List[str]] = Field(
        description="Tables referenced by similar queries from semantic context", default=None
    )
    cache_hit: bool = Field(description="Whether the cache was hit", default=False)
    sql: Optional[str] = Field(description="The SQL query", default=None)
    data: Optional[DataOutput] = Field(description="The data output", default=None)
    output_type: Optional[OutputType] = Field(
        description="The type of output", default=None
    )
    detailed_error_type: Optional[DetailedErrorType] = Field(
        description="The type of detailed error", default=None
    )
    error_message: Optional[str] = Field(description="The error message", default=None)
    visualisation_config: Optional[Dict] = Field(
        description="Plotly JSON configuration for the visualisation", default=None
    )
