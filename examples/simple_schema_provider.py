"""Simple example of a Schema Context Provider."""

from insightiq_common.context_providers.schema_context_provider import (
    BaseSchemaContextProvider,
)
from insightiq_common.models.context_providers.schema_context_provider import (
    SchemaContextProviderInput,
    SchemaContextProviderOutput,
)


class SimpleSchemaProvider(BaseSchemaContextProvider):
    """A simple schema provider that returns basic table info."""

    def __init__(self):
        super().__init__(
            name="SimpleSchemaProvider",
            description="Returns basic schema information for tables",
        )

    def get_context(
        self, input_data: SchemaContextProviderInput
    ) -> SchemaContextProviderOutput:
        """Get schema context for tables."""
        # Simple implementation - just list the tables
        context = f"Tables: {', '.join(input_data.tables)}"
        return SchemaContextProviderOutput(context=context)


# Usage
if __name__ == "__main__":
    provider = SimpleSchemaProvider()
    input_data = SchemaContextProviderInput(tables=["users", "orders"])
    output = provider.get_context(input_data)
    print(output.context)  # Output: Tables: users, orders
