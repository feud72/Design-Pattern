from image_storage import ImageStorage
from black_and_white_filter import BlackAndWhiteFilter
from high_contrast_filter import HighContrastFilter
from jpeg_compressor import JpegCompressor
from png_compressor import PngCompressor


def main():
    image = ImageStorage()
    image.store("image1", JpegCompressor(), BlackAndWhiteFilter())
    image.store("image2", PngCompressor(), HighContrastFilter())


main()
