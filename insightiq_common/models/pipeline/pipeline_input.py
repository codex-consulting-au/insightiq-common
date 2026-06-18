from typing import List, Optional
from pydantic import BaseModel, Field
import uuid

from insightiq_common.models.common.entities.message import Message


class PipelineInput(BaseModel):
    query: Message = Field(description="The query to be processed")
    message_history: Optional[List[Message]] = Field(
        description="The message history", default=None
    )
    session_id: Optional[str] = Field(
        description="The session id", default=str(uuid.uuid4())
    )
    user_id: Optional[str] = Field(description="The user id", default=str(uuid.uuid4()))
