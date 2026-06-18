from abc import ABC, abstractmethod
from insightiq_common.models.pipeline_services.sql_executor.sql_executor_input import (
    SQLExecutorInput,
)
from insightiq_common.models.pipeline_services.sql_executor.sql_executor_output import (
    SQLExecutorOutput,
)


class BaseSQLExecutor(ABC):
    @abstractmethod
    def execute(self, input: SQLExecutorInput) -> SQLExecutorOutput:
        pass
