from SelectionTool import SelectionTool
from BrushTool import BrushTool
from Canvas import Canvas


def main():
    currentTool = SelectionTool()
    canvas = Canvas(currentTool=currentTool)

    canvas.mouseDown()
    canvas.mouseUp()

    canvas.setCurrentTool(BrushTool())
    canvas.mouseDown()
    canvas.mouseUp()


main()
