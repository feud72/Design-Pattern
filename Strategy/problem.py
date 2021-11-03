class ImageStorage:
    def __init__(self, compressor, filter) -> None:
        self.compressor = compressor
        self.filter = filter

    def store(self, fileName: str) -> None:
        if self.compressor == "jpeg":
            print(f"{fileName}: Compressing using JPEG")
        elif self.compressor == "png":
            print(f"{fileName}: Compressing using PNG")

        if self.filter == "b&w":
            print(f"{fileName}: Applying B&W filter")
        elif self.filter == "high-contrast":
            print(f"{fileName}: Applying high contrast filter")
