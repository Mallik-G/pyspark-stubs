# Stubs for pyspark.ml.stat (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

class ChiSquareTest:
    @staticmethod
    def test(dataset, featuresCol, labelCol): ...

class Correlation:
    @staticmethod
    def corr(dataset, column, method: str = ...): ...
