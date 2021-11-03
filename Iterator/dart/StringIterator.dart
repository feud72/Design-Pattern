import 'BrowseHistory.dart';
import 'Iterator.dart';

class StringIterator implements Iterator {
  BrowseHistory history;
  int index = 0;

  StringIterator({
    required this.history,
  });

  @override
  String current() {
    return history.urls.elementAt(index);
  }

  @override
  bool hasNext() {
    return index < history.urls.length;
  }

  @override
  void next() {
    index++;
  }
}
