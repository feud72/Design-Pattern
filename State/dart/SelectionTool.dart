import 'UIControl.dart';

class SelectionTool implements UIControl {
  @override
  void mouseDown() {
    print("셀렉션 아이콘");
  }

  @override
  void mouseUp() {
    print("점선 사각형을 그린다");
  }
}
