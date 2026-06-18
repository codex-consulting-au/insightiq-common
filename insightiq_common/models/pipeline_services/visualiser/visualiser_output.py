"""Output model for the visualiser service."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class VisualiserOutput(BaseModel):
    """Output model for visualisation generation."""

    success: bool = Field(
        description="Whether visualisation generation succeeded"
    )
    chart_config: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Plotly JSON configuration (config mode)",
    )
    image_url: Optional[str] = Field(
        default=None,
        description="URL or path to generated image (visualization mode)",
    )
    chart_type: Optional[str] = Field(
        default=None,
        description="Type of chart generated (bar, line, scatter, etc.)",
    )
    confidence: Optional[float] = Field(
        default=None,
        description="Confidence score of the chart recommendation (0.0 to 1.0)",
    )
    reasoning: Optional[str] = Field(
        default=None,
        description="Explanation for the chart type selection",
    )
    error: Optional[str] = Field(
        default=None,
        description="Error message if generation failed",
    )
