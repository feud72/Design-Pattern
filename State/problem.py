from enum import Enum, auto


class ToolType(Enum):
    SELECTION = auto()
    BRUSH = auto()
    ERASER = auto()


class Canvas:
    def __init__(self, currentTool: ToolType) -> None:
        self.__currentTool = currentTool

    def mouseDown(self) -> None:
        if self.__currentTool == ToolType.SELECTION:
            print("셀렉션 아이콘")
        elif self.__currentTool == ToolType.BRUSH:
            print("브러쉬 아이콘")
        elif self.__currentTool == ToolType.ERASER:
            print("지우개 아이콘")

    def mouseUp(self) -> None:
        if self.__currentTool == ToolType.SELECTION:
            print("점선 사각형을 그린다")
        elif self.__currentTool == ToolType.BRUSH:
            print("선을 그린다")
        elif self.__currentTool == ToolType.ERASER:
            print("지운다")

    def getCurrentTool(self) -> ToolType:
        return self.__currentTool

    def setCurrentTool(self, toolType: ToolType) -> None:
        self.__currentTool = toolType
