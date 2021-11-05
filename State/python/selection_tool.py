from ui_control import UIControl


class SelectionTool(UIControl):
    def mouseDown(self) -> None:
        print("셀렉션 아이콘")

    def mouseUp(self) -> None:
        print("점선 사각형을 그린다")
