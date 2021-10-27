import 'EditorState.dart';

class History {
  final List<EditorState> states = [];

  void push(EditorState state) {
    states.add(state);
  }

  EditorState pop() {
    return states.removeLast();
  }
}
