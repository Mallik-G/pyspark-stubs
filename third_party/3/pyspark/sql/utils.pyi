# Stubs for pyspark.sql.utils (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class CapturedException(Exception):
    desc = ...  # type: Any
    stackTrace = ...  # type: Any
    def __init__(self, desc, stackTrace) -> None: ...

class AnalysisException(CapturedException): ...
class ParseException(CapturedException): ...
class IllegalArgumentException(CapturedException): ...
class StreamingQueryException(CapturedException): ...
class QueryExecutionException(CapturedException): ...

def capture_sql_exception(f): ...
def install_exception_handler(): ...
def toJArray(gateway, jtype, arr): ...
