from compressor import Compressor
from filter import Filter


class ImageStorage:
    def store(self, fileName: str, compressor: Compressor, filter: Filter) -> None:
        compressor.compress(fileName)
        filter.apply(fileName)
