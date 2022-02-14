"""
File to store constants
"""
from enum import Enum

class S3FileTypes(Enum):
    """
    supported file types for S3BucketConnector
    """

    CSV = "csv"
    PARQUET = "parkquet"


class MetaProseccFormat(Enum):
    """
    formation for MetaProsecc class
    """

    META_DATE_FORMAT = "%Y-%m_%d"
    META_PROCESS_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    META_SOURCE_DATE_COL = "curce_date"
    META_PROCESS_COL = "datetime_of_processing"
    META_FILE_FORMAT = "csv"

    