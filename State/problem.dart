class Canvas {
  ToolType _currentTool;

  Canvas({
    required currentTool,
  }) : _currentTool = currentTool;

  ToolType get currentTool => _currentTool;

  set currentTool(ToolType currentTool) {
    _currentTool = currentTool;
  }

  void mouseDown() {
    if (currentTool == ToolType.SELECTION) {
      print("셀렉션 아이콘");
    } else if (currentTool == ToolType.BRUSH) {
      print("브러쉬 아이콘");
    } else if (currentTool == ToolType.ERASER) {
      print("지우개 아이콘");
    }
  }

  void mouseUp() {
    if (currentTool == ToolType.SELECTION) {
      print("점선 사각형을 그린다");
    } else if (currentTool == ToolType.BRUSH) {
      print("선을 그린다");
    } else if (currentTool == ToolType.ERASER) {
      print("지운다");
    }
  }
}

enum ToolType { SELECTION, BRUSH, ERASER }
