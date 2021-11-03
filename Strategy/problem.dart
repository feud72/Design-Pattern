class ImageStorage {
  String compressor;
  String filter;

  ImageStorage({
    required this.compressor,
    required this.filter,
  });

  void store(String fileName) {
    if (compressor == "jpeg") {
      print("Compressing using JPEG");
    } else if (compressor == "png") {
      print("Compressing using PNG");
    }

    if (filter == "b&w") {
      print("Applying B&W filter");
    } else if (filter == "high-contrast") {
      print("Applying high contrast filter");
    }
  }
}
