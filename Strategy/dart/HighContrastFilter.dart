import 'Filter.dart';

class HighContrastFilter implements Filter {
  @override
  void apply(String fileName) {
    print("$fileName: Applying high contrast filter");
  }
}
