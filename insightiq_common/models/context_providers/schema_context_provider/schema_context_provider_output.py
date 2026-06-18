from pydantic import BaseModel, Field


class SchemaContextProviderOutput(BaseModel):
    """Output model for schema context providers."""

    context: str = Field(description="Schema context as a formatted string")
