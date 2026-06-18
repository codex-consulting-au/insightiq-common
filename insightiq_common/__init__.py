"""InsightIQ Common - Shared context providers for InsightIQ services."""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("insightiq-common")
except PackageNotFoundError:
    # Package is not installed
    __version__ = "0.0.0.dev"

from insightiq_common.context_providers.schema_context_provider.base_schema_context_provider import (
    BaseSchemaContextProvider,
)
from insightiq_common.context_providers.semantic_context_provider.base_semantic_context_provider import (
    BaseSemanticContextProvider,
)
from insightiq_common.models.context_providers.schema_context_provider.schema_context_provider_input import (
    SchemaContextProviderInput,
)
from insightiq_common.models.context_providers.schema_context_provider.schema_context_provider_output import (
    SchemaContextProviderOutput,
)
from insightiq_common.models.context_providers.semantic_context_provider.semantic_context_provider_input import (
    SemanticContextProviderInput,
)
from insightiq_common.models.context_providers.semantic_context_provider.semantic_context_provider_output import (
    SemanticContextProviderOutput,
)

__all__ = [
    "__version__",
    "BaseSchemaContextProvider",
    "BaseSemanticContextProvider",
    "SchemaContextProviderInput",
    "SchemaContextProviderOutput",
    "SemanticContextProviderInput",
    "SemanticContextProviderOutput",
]
