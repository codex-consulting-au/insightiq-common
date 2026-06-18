from abc import ABC, abstractmethod
from typing import BinaryIO
from insightiq_common.models.pipeline_services.file_storage_service.file_storage_service_input import (
    FileReadInput,
    FileWriteInput,
    FileExistsInput,
    FileListInput,
    FileGlobInput,
    FileMkdirInput,
    FileSaveJSONInput,
    FileLoadJSONInput,
    FileSavePickleInput,
    FileLoadPickleInput,
    FileSaveDataFrameInput,
    FileLoadDataFrameInput,
    FileSaveImageInput,
    FileLoadImageInput,
    FileURIInput,
)
from insightiq_common.models.pipeline_services.file_storage_service.file_storage_service_output import (
    FileReadOutput,
    FileWriteOutput,
    FileExistsOutput,
    FileListOutput,
    FileMkdirOutput,
    FileSaveJSONOutput,
    FileLoadJSONOutput,
    FileSavePickleOutput,
    FileLoadPickleOutput,
    FileSaveDataFrameOutput,
    FileLoadDataFrameOutput,
    FileSaveImageOutput,
    FileLoadImageOutput,
    FileURIOutput,
)


class BaseFileStorageService(ABC):
    """
    Abstract base class for file storage operations.
    Supports local, S3, GCS, Azure Blob, and other storage backends.
    """

    # Core file operations
    @abstractmethod
    def open(self, input: FileReadInput) -> BinaryIO:
        """Open a file for streaming access"""
        pass

    @abstractmethod
    def read_bytes(self, input: FileReadInput) -> FileReadOutput:
        """Read file as bytes"""
        pass

    @abstractmethod
    def write_bytes(self, input: FileWriteInput) -> FileWriteOutput:
        """Write bytes to file"""
        pass

    # File system operations
    @abstractmethod
    def exists(self, input: FileExistsInput) -> FileExistsOutput:
        """Check if a file exists"""
        pass

    @abstractmethod
    def list_files(self, input: FileListInput) -> FileListOutput:
        """List files under a prefix"""
        pass

    @abstractmethod
    def glob(self, input: FileGlobInput) -> FileListOutput:
        """Find files matching a glob pattern"""
        pass

    @abstractmethod
    def mkdir(self, input: FileMkdirInput) -> FileMkdirOutput:
        """Create a directory"""
        pass

    # Structured data operations
    @abstractmethod
    def save_json(self, input: FileSaveJSONInput) -> FileSaveJSONOutput:
        """Save object as JSON"""
        pass

    @abstractmethod
    def load_json(self, input: FileLoadJSONInput) -> FileLoadJSONOutput:
        """Load JSON file"""
        pass

    @abstractmethod
    def save_pickle(self, input: FileSavePickleInput) -> FileSavePickleOutput:
        """Save object as pickle"""
        pass

    @abstractmethod
    def load_pickle(self, input: FileLoadPickleInput) -> FileLoadPickleOutput:
        """Load pickle file"""
        pass

    # DataFrame operations
    @abstractmethod
    def save_df(self, input: FileSaveDataFrameInput) -> FileSaveDataFrameOutput:
        """Save DataFrame as Parquet/CSV"""
        pass

    @abstractmethod
    def load_df(self, input: FileLoadDataFrameInput) -> FileLoadDataFrameOutput:
        """Load DataFrame from Parquet/CSV"""
        pass

    # Image operations
    @abstractmethod
    def save_image(self, input: FileSaveImageInput) -> FileSaveImageOutput:
        """Save image as PNG"""
        pass

    @abstractmethod
    def load_image(self, input: FileLoadImageInput) -> FileLoadImageOutput:
        """Read PNG image"""
        pass

    # Advanced operations
    @abstractmethod
    def get_uri(self, input: FileURIInput) -> FileURIOutput:
        """Get fully qualified URI for a path"""
        pass
