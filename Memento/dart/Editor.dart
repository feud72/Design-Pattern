import 'EditorState.dart';

class Editor {
  late String _content;

  EditorState createState() {
    return EditorState(content: this._content);
  }

  void restore(EditorState state) {
    this._content = state.content;
  }

  String get content => _content;

  set content(String content) {
    _content = content;
  }
}
