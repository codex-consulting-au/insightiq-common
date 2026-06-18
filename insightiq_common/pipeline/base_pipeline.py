from abc import ABC, abstractmethod
from logging import Logger

from insightiq_common.pipeline_services.normalizer.base_normalizer import BaseNormalizer
from insightiq_common.pipeline_services.sql_writer.base_sql_writer import BaseSQLWriter
from insightiq_common.pipeline_services.sql_executor.base_sql_executor import (
    BaseSQLExecutor,
)
from insightiq_common.pipeline_services.file_storage_service.base_file_storage_service import (
    BaseFileStorageService,
)
from insightiq_common.pipeline_services.visualiser.base_visualiser import (
    BaseVisualiser,
)
from insightiq_common.context_providers.schema_context_provider.base_schema_context_provider import (
    BaseSchemaContextProvider,
)
from insightiq_common.context_providers.semantic_context_provider.base_semantic_context_provider import (
    BaseSemanticContextProvider,
)
from insightiq_common.models.pipeline.pipeline_input import PipelineInput
from insightiq_common.models.pipeline.pipeline_output import PipelineOutput


class BasePipeline(ABC):
    def __init__(
        self,
        normalizer: BaseNormalizer=None,
        sql_writer: BaseSQLWriter=None,
        sql_executor: BaseSQLExecutor=None,
        file_storage_service: BaseFileStorageService=None,
        visualiser: BaseVisualiser=None,
        schema_context_providers: list[BaseSchemaContextProvider] = [],
        semantic_context_providers: list[BaseSemanticContextProvider] = [],
        logger: Logger = None,
    ):
        self.normalizer = normalizer
        self.sql_writer = sql_writer
        self.sql_executor = sql_executor
        self.file_storage_service = file_storage_service
        self.visualiser = visualiser
        self.schema_context_providers = schema_context_providers
        self.semantic_context_providers = semantic_context_providers
        self.logger = logger

    @abstractmethod
    def run(self, input: PipelineInput) -> PipelineOutput:
        pass
