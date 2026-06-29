"""Input model for the preserved-query pipeline."""

import uuid
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict, Field

from insightiq_common.models.pipeline.pipeline_output import OutputType


class PreservedQueryPipelineInput(BaseModel):
    """Input for executing preserved SQL and returning saved metadata."""

    model_config = ConfigDict(populate_by_name=True)

    sql: str = Field(description="SQL query to execute")
    sanitised_query: str = Field(description="Sanitised natural language query")
    output_type: OutputType = Field(description="Expected successful output type")
    visualisation_config: Optional[Dict[str, Any]] = Field(
        default=None,
        alias="visual_config",
        description="Preserved Plotly visualisation config",
    )
    session_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
