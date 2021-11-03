from filter import Filter


class BlackAndWhiteFilter(Filter):
    def apply(self, fileName: str) -> None:
        print(f"{fileName}: Applying B&W filter")
