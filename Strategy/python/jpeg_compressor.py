from compressor import Compressor


class JpegCompressor(Compressor):
    def compress(self, fileName: str) -> None:
        print(f"{fileName}: Compressing using JPEG")
