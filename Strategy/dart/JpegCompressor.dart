import 'Compressor.dart';

class JpegCompressor implements Compressor {
  @override
  void compress(String fileName) {
    print("$fileName: Compressing using JPEG");
  }
}
