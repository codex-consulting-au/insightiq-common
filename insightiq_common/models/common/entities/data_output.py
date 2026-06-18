from pydantic import BaseModel
from pydantic import Field
from typing import Any, List, Dict, Optional


class DataMetadata(BaseModel):
    number_rows: int = Field(description="The number of rows in the data", default=0)
    number_columns: int = Field(
        description="The number of columns in the data", default=0
    )
    column_data_types: Dict[str, str] = Field(
        description="The data types of the columns", default_factory=dict
    )
    unique_value_counts: Dict[str, int] = Field(
        description="The count of unique values of the columns", default_factory=dict
    )

    @staticmethod
    def get_metadata(data: List[Dict[str, Any]]) -> "DataMetadata":
        number_rows = len(data)
        number_columns = len(data[0])
        column_data_types = {
            key: type(value).__name__ for key, value in data[0].items()
        }
        unique_value_counts = {
            key: len(set(row[key] for row in data)) for key in data[0].keys()
        }
        return DataMetadata(
            number_rows=number_rows,
            number_columns=number_columns,
            column_data_types=column_data_types,
            unique_value_counts=unique_value_counts,
        )


class DataOutput(BaseModel):
    data: Optional[List[Dict]] = Field(
        description="The data returned from the query", default=[]
    )
    metadata: DataMetadata = Field(description="The metadata of the data", default=None)
    file_uri: str = Field(description="The URI of the file", default=None)
    file_name: str = Field(description="The name of the file", default=None)
