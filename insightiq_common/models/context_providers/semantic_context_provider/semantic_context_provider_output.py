from pydantic import BaseModel, Field


class SemanticContextProviderOutput(BaseModel):
    """Output model for semantic context providers."""

    context: str = Field(description="Semantic context as a formatted string")
    tables_used: list[str] = Field(
        description="List of tables used to generate the semantic context"
    )
    matched_count: int = Field(
        default=0,
        description="Number of similar examples found above the similarity threshold",
    )
