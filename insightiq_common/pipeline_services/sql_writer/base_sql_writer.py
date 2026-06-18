from abc import ABC, abstractmethod
from insightiq_common.models.pipeline_services.sql_writer.sql_writer_input import (
    SQLWriterInput,
)
from insightiq_common.models.pipeline_services.sql_writer.sql_writer_output import (
    SQLWriterOutput,
)


class BaseSQLWriter(ABC):
    @abstractmethod
    def write(self, input: SQLWriterInput) -> SQLWriterOutput:
        pass
