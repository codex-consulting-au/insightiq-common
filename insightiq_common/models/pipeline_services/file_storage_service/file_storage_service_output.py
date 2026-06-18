from typing import Any
from pydantic import BaseModel, Field
from typing import Dict, Optional


class FileReadOutput(BaseModel):
    success: bool = Field(description="Whether the read operation succeeded")
    data: Optional[bytes | str] = Field(default=None, description="File contents")
    error_message: str = Field(default=None, description="Error message if failed")


class FileWriteOutput(BaseModel):
    success: bool = Field(description="Whether the write operation succeeded")
    error_message: str = Field(default=None, description="Error message if failed")


class FileExistsOutput(BaseModel):
    exists: bool = Field(description="Whether the file exists")
    error_message: str = Field(
        default=None, description="Error message if check failed"
    )


class FileListOutput(BaseModel):
    success: bool = Field(description="Whether the list operation succeeded")
    files: list[str] = Field(default_factory=list, description="List of file paths")
    error_message: str = Field(default=None, description="Error message if failed")


class FileGlobOutput(BaseModel):
    success: bool = Field(description="Whether the glob operation succeeded")
    files: list[str] = Field(default_factory=list, description="List of file paths")
    error_message: str = Field(default=None, description="Error message if failed")


class FileMkdirOutput(BaseModel):
    success: bool = Field(description="Whether the mkdir operation succeeded")
    error_message: str = Field(default=None, description="Error message if failed")


class FileSaveJSONOutput(BaseModel):
    success: bool = Field(description="Whether the JSON operation succeeded")
    error_message: str = Field(default=None, description="Error message if failed")


class FileLoadJSONOutput(BaseModel):
    success: bool = Field(description="Whether the JSON operation succeeded")
    data: Dict[Any, Any] = Field(
        default=None, description="Loaded JSON data (for load operations)"
    )
    error_message: str = Field(default=None, description="Error message if failed")


class FileSavePickleOutput(BaseModel):
    success: bool = Field(description="Whether the pickle operation succeeded")
    error_message: str = Field(default=None, description="Error message if failed")


class FileLoadPickleOutput(BaseModel):
    success: bool = Field(description="Whether the pickle operation succeeded")
    data: Any = Field(
        default=None, description="Loaded pickle data (for load operations)"
    )
    error_message: str = Field(default=None, description="Error message if failed")


class FileSaveDataFrameOutput(BaseModel):
    success: bool = Field(description="Whether the DataFrame operation succeeded")
    error_message: str = Field(default=None, description="Error message if failed")


class FileLoadDataFrameOutput(BaseModel):
    success: bool = Field(description="Whether the DataFrame operation succeeded")
    data: Any = Field(
        default=None, description="Loaded DataFrame data (for load operations)"
    )
    error_message: str = Field(default=None, description="Error message if failed")


class FileSaveImageOutput(BaseModel):
    success: bool = Field(description="Whether the image operation succeeded")
    error_message: str = Field(default="", description="Error message if failed")


class FileLoadImageOutput(BaseModel):
    success: bool = Field(description="Whether the image operation succeeded")
    data: Any = Field(
        default=None, description="Loaded image data (for load operations)"
    )
    error_message: str = Field(default=None, description="Error message if failed")


class FileWalkOutput(BaseModel):
    success: bool = Field(description="Whether the walk operation succeeded")
    files: list[str] = Field(
        default_factory=list, description="List of file paths found"
    )
    error_message: str = Field(default="", description="Error message if failed")


class FileURIOutput(BaseModel):
    success: bool = Field(description="Whether the URI generation succeeded")
    uri: str = Field(default="", description="Fully qualified URI")
    error_message: str = Field(default="", description="Error message if failed")
