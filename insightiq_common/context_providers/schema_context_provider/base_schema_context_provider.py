from abc import ABC, abstractmethod

from insightiq_common.models.context_providers.schema_context_provider.schema_context_provider_input import (
    SchemaContextProviderInput,
)
from insightiq_common.models.context_providers.schema_context_provider.schema_context_provider_output import (
    SchemaContextProviderOutput,
)


class BaseSchemaContextProvider(ABC):
    """Base class for schema context providers.

    Schema context providers take a list of table names and generate
    contextual information about their schemas as a formatted string.

    Attributes:
        name: Name of the schema context provider
        description: Description of what this provider does
    """

    def __init__(self, name: str, description: str):
        """Initialize the base schema context provider.

        Args:
            name: Name of the schema context provider
            description: Description of what this provider does
        """
        self.name = name
        self.description = description

    @abstractmethod
    def get_context(
        self, input_data: SchemaContextProviderInput
    ) -> SchemaContextProviderOutput:
        """Get schema context for the given tables.

        Args:
            input_data: Input containing list of table names

        Returns:
            Output containing schema context as a formatted string
        """
        pass
