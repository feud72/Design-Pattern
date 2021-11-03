# Iterator 패턴

웹 브라우저를 만들고 있습니다.

여러 사이트를 방문한 후 history 기능을 통해 우리가 방문했던 URL의 리스트를 얻고 싶습니다.

### BrowserHistory 클래스

- method: void push(String url)

- method: String pop()

구현한 코드는 다음과 같습니다.

[dart 코드](problem.dart)

[python 코드](problem.py)

### 문제

- BrowserHistory 클래스를 범용성 있게 재사용하고 싶습니다.

- String 형태가 아닌 다른 타입의 객체를 사용하도록 코드를 변경하더라도

- 어플리케이션의 다른 부분의 작동에 영향이 없도록 캡슐화하고 싶습니다.

- next(), current(), hasNext() method를 구현합니다.

- Single responsibility principle을 고려하여 작성합니다.
