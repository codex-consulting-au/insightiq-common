from abc import ABC, abstractmethod
from typing import List
from insightiq_common.models.pipeline_services.normalizer.normalizer_input import (
    NormalizerInput,
)
from insightiq_common.models.pipeline_services.normalizer.normalizer_output import (
    NormalizerOutput,
)


class BaseNormalizer(ABC):
    @abstractmethod
    def normalize(self, input: NormalizerInput) -> NormalizerOutput:
        pass
