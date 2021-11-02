import 'UIControl.dart';

class BrushTool implements UIControl {
  @override
  void mouseDown() {
    print("브러쉬 아이콘");
  }

  @override
  void mouseUp() {
    print("선을 그린다");
  }
}
