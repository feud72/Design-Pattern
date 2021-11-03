from filter import Filter


class HighContrastFilter(Filter):
    def apply(self, fileName: str) -> None:
        print(f"{fileName}: Applying high contrast filter")
