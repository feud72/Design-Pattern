from selection_tool import SelectionTool
from brush_tool import BrushTool
from canvas import Canvas


def main():
    currentTool = SelectionTool()
    canvas = Canvas(currentTool=currentTool)

    canvas.mouseDown()
    canvas.mouseUp()

    canvas.setCurrentTool(BrushTool())
    canvas.mouseDown()
    canvas.mouseUp()


main()
