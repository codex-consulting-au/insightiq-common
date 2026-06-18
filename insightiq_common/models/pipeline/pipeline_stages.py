from enum import Enum


class PipelineStage(Enum):
    Normalisation = "normalisation"
    SQLWriting = "sql_writing"
    SQLExecution = "sql_execution"
    Validation = "validation"
    UserClarification = "user_clarification"
    Visualisation = "visualisation"
    Other = "other"
