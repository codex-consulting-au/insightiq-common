from pydantic import BaseModel
from typing import List, Optional
from insightiq_common.models.common.entities.message import Message
from pydantic import Field


class NormalizerInput(BaseModel):
    message: Message = Field(description="The message to be normalised")
    message_history: Optional[List[Message]] = Field(
        description="The message history", default=None
    )
