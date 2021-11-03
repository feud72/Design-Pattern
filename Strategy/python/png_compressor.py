from compressor import Compressor


class PngCompressor(Compressor):
    def compress(self, fileName: str) -> None:
        print(f"{fileName}: Compressing using PNG")
