from UIControl import UIControl


class Canvas:
    def __init__(self, currentTool: UIControl) -> None:
        self.__currentTool = currentTool

    def setCurrentTool(self, currentTool: UIControl) -> None:
        self.__currentTool = currentTool

    def mouseDown(self) -> None:
        self.__currentTool.mouseDown()

    def mouseUp(self) -> None:
        self.__currentTool.mouseUp()
