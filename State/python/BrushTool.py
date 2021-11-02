from UIControl import UIControl


class BrushTool(UIControl):
    def mouseDown(self) -> None:
        print("브러쉬 아이콘")

    def mouseUp(self) -> None:
        print("선을 그린다")
