"""Base visualiser interface."""

from abc import ABC, abstractmethod

from insightiq_common.models.pipeline_services.visualiser.visualiser_input import (
    VisualiserInput,
)
from insightiq_common.models.pipeline_services.visualiser.visualiser_output import (
    VisualiserOutput,
)


class BaseVisualiser(ABC):
    """Abstract base class for visualisation services.

    Takes query results and generates chart configurations or images.
    """

    @abstractmethod
    def visualise(self, input: VisualiserInput) -> VisualiserOutput:
        """Generate a visualisation from the provided data.

        Args:
            input: VisualiserInput containing data, query, and preferences.

        Returns:
            VisualiserOutput with chart config or image reference.

        """
