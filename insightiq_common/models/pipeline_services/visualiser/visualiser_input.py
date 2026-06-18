"""Input model for the visualiser service."""

from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field


class VisualiserInput(BaseModel):
    """Input model for visualisation generation.

    The data should be pre-processed (filtered, aggregated) before
    passing to the visualiser. The service determines the best chart type.
    """

    data: List[Dict[str, Any]] = Field(
        description="Query result data as a list of row dicts"
    )
    query: str = Field(
        description="The original natural language question"
    )
    sql_query: Optional[str] = Field(
        default=None,
        description="The SQL query that produced the data",
    )
    output_type: Literal["config", "visualization"] = Field(
        default="config",
        description="Output mode: 'config' for Plotly JSON, 'visualization' for static image",
    )
    visual_hint: Optional[str] = Field(
        default=None,
        description="Optional hint about desired chart type (e.g. 'bar chart', 'line graph')",
    )
    pipeline_validated: bool = Field(
        default=False,
        description="If True, data is pre-validated by the pipeline. Skip query validation and always generate a chart.",
    )
