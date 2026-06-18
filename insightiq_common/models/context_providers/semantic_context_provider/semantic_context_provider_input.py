from pydantic import BaseModel, Field
from typing import Optional


class SemanticContextProviderInput(BaseModel):
    """Input model for semantic context providers."""

    sanitized_query: str = Field(
        description="Sanitized query to generate semantic context for"
    )
    allowed_tables: Optional[list[str]] = Field(
        default=None,
        description="List of table names to allow for semantic context generation",
    )
