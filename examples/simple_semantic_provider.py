"""Simple example of a Semantic Context Provider."""

from insightiq_common.context_providers.semantic_context_provider import (
    BaseSemanticContextProvider,
)
from insightiq_common.models.context_providers.semantic_context_provider import (
    SemanticContextProviderInput,
    SemanticContextProviderOutput,
)


class SimpleSemanticProvider(BaseSemanticContextProvider):
    """A simple semantic provider that returns basic query info."""

    def __init__(self):
        super().__init__(
            name="SimpleSemanticProvider",
            description="Returns basic semantic information for queries",
        )

    def get_context(
        self, input_data: SemanticContextProviderInput
    ) -> SemanticContextProviderOutput:
        """Get semantic context for query."""
        # Simple implementation - just echo the query
        context = f"Query: {input_data.sanitized_query}"
        tables = input_data.allowed_tables or []
        return SemanticContextProviderOutput(context=context, tables_used=tables)


# Usage
if __name__ == "__main__":
    provider = SimpleSemanticProvider()
    input_data = SemanticContextProviderInput(
        sanitized_query="show me sales data",
        allowed_tables=["sales", "customers"],
    )
    output = provider.get_context(input_data)
    print(output.context)  # Output: Query: show me sales data
    print(output.tables_used)  # Output: ['sales', 'customers']
