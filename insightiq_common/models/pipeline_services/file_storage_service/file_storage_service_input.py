from typing import Any
from pydantic import BaseModel, Field
from typing import Dict, Optional


class FileReadInput(BaseModel):
    path: str = Field(description="Path to the file to read")
    mode: str = Field(default="rb", description="File open mode")


class FileWriteInput(BaseModel):
    path: str = Field(description="Path to write the file")
    data: bytes | str = Field(description="Data to write to the file")
    encoding: str = Field(
        default="utf-8", description="Text encoding (for string data)"
    )


class FileExistsInput(BaseModel):
    path: str = Field(description="Path to check for existence")


class FileListInput(BaseModel):
    prefix: str = Field(default="", description="Prefix to filter files")


class FileGlobInput(BaseModel):
    pattern: str = Field(description="Glob pattern (e.g., 'data/**/*.json')")


class FileMkdirInput(BaseModel):
    path: str = Field(description="Directory path to create")
    exist_ok: bool = Field(default=True, description="No error if directory exists")


class FileSaveJSONInput(BaseModel):
    path: str = Field(description="Path to JSON file")
    indent: Optional[int] = Field(default=None, description="JSON indentation level")
    dict_to_save: Dict[Any, Any] = Field(
        default=None, description="Dictionary to save (for save operations)"
    )


class FileLoadJSONInput(BaseModel):
    path: str = Field(description="Path to JSON file")


class FileSavePickleInput(BaseModel):
    path: str = Field(description="Path to pickle file")
    object_to_save: Any = Field(
        default=None, description="Object to save (for save operations)"
    )


class FileLoadPickleInput(BaseModel):
    path: str = Field(description="Path to pickle file")


class FileSaveDataFrameInput(BaseModel):
    path: str = Field(description="Path to DataFrame file (Parquet/CSV)")
    df: Any = Field(default=None, description="DataFrame to save (for save operations)")


class FileLoadDataFrameInput(BaseModel):
    path: str = Field(description="Path to DataFrame file (Parquet/CSV)")


class FileSaveImageInput(BaseModel):
    path: str = Field(description="Path to image file (PNG)")
    image_to_save: Any = Field(
        default=None, description="Image data to save (for save operations)"
    )


class FileLoadImageInput(BaseModel):
    path: str = Field(description="Path to image file (PNG)")


class FileURIInput(BaseModel):
    path: str = Field(description="Path to get URI for")
