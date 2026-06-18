from abc import ABC, abstractmethod
from insightiq_common.models.pipeline_services.sql_explainer.sql_explainer_input import (
    SQLExplainerInput,
)
from insightiq_common.models.pipeline_services.sql_explainer.sql_explainer_output import (
    SQLExplainerOutput,
)


class BaseSQLExplainer(ABC):
    @abstractmethod
    def explain(self, input: SQLExplainerInput) -> SQLExplainerOutput:
        pass
