from pydantic import BaseModel, Field
from typing import Any, Optional
from insightiq_common.models.pipeline_services.normalizer.normalizer_output import (
    NormalizerOutput,
)
from typing import List
from insightiq_common.models.common.entities.message import Message


class SQLWriterInput(BaseModel):
    sanitised_message: str = Field(description="The sanitised message")
    message_history: Optional[List[Message]] = Field(
        description="The message history", default=None
    )
    schema_context: Optional[str] = Field(description="The schema context", default=None)
    semantic_context: Optional[str] = Field(description="The semantic context", default=None)
    additional_context: Optional[dict[str, Any]] = Field(description="Additional context", default=None)
