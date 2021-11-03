class BrowseHistory {
  List<String> _urls = [];

  List<String> get urls => _urls;

  void push(String url) {
    urls.add(url);
  }

  String pop() {
    return urls.removeLast();
  }
}

void main(List<String> args) {
  var history = new BrowseHistory();
  history.push("a");
  history.push("b");
  history.push("c");

  for (var url in history.urls) {
    print(url);
  }
}
