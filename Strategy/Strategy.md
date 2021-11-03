# Strategy 패턴

이미지를 저장하는 ImageStorage 클래스를 작성했습니다.

파일 압축 방식과 필터 효과를 입력하면 해당 형식과 필터에 맞추어 출력물을 저장합니다.

### ImageStorage 클래스

- field: String compressor

- field: String filter

- method: void store(String fileName)

아래와 같이 구현을 하였습니다.

[dart 코드](problem.dart)

[python 코드](problem.py)

### 문제

- Single responsibility principle을 위배하고 있습니다. store method에 단지 저장 기능을 수행하는 것 뿐 아니라 파일 압축, 필터 등의 로직이 포함되어 있습니다.

- 압축 방식과 필터의 종류가 추가될 때마다 ImageStorage 클래스를 수정해야 합니다. 클래스가 지나치게 비대해 지는 것을 원하지 않습니다.
