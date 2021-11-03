import 'Compressor.dart';

class PngCompressor implements Compressor {
  @override
  void compress(String fileName) {
    print("$fileName: Compressing using PNG");
  }
}
