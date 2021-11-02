import 'UIControl.dart';

class Canvas {
  UIControl _currentTool;

  UIControl get currentTool => _currentTool;

  set currentTool(UIControl currentTool) {
    _currentTool = currentTool;
  }

  Canvas({
    required currentTool,
  }) : _currentTool = currentTool;

  void mouseDown() {
    currentTool.mouseDown();
  }

  void mouseUp() {
    currentTool.mouseUp();
  }
}
