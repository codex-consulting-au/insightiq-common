from abc import ABC, abstractmethod

from insightiq_common.models.context_providers.semantic_context_provider.semantic_context_provider_input import (
    SemanticContextProviderInput,
)
from insightiq_common.models.context_providers.semantic_context_provider.semantic_context_provider_output import (
    SemanticContextProviderOutput,
)


class BaseSemanticContextProvider(ABC):
    """Base class for semantic context providers.

    Semantic context providers take a sanitized query and generate
    contextual information about relevant semantic data as a formatted string.

    Attributes:
        name: Name of the semantic context provider
        description: Description of what this provider does
    """

    def __init__(self, name: str, description: str):
        """Initialize the base semantic context provider.

        Args:
            name: Name of the semantic context provider
            description: Description of what this provider does
        """
        self.name = name
        self.description = description

    @abstractmethod
    def get_context(
        self, input_data: SemanticContextProviderInput
    ) -> SemanticContextProviderOutput:
        """Get semantic context for the given query.

        Args:
            input_data: Input containing sanitized query and optional allowed tables

        Returns:
            Output containing semantic context as a formatted string
        """
        pass
