import 'UIControl.dart';

class EraserTool implements UIControl {
  @override
  void mouseDown() {
    print("지우개 아이콘");
  }

  @override
  void mouseUp() {
    print("지운다");
  }
}
