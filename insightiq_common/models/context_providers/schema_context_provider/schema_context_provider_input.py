from pydantic import BaseModel, Field
from typing import Any, Optional


class SchemaContextProviderInput(BaseModel):
    """Input model for schema context providers."""

    tables: Optional[list[str]] = Field(
        description="List of table names to get schema context for", default=None
    )
    additional_data: Optional[dict[str, Any]] = Field(
        default=None,
        description="Additional data to pass to the schema context provider",
    )
