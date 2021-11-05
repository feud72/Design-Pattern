# Template Method 패턴

은행 어플리케이션을 만들고 있습니다.

어떠한 작업을 할 때 항상 '누가' '언제' '무엇을' 했는지 기록하는 AuditTrail 을 포함하여 작성하고자 합니다.

이체를 하는 TransferMoneyTask 클래스와 내역 조회를 하는 GenerateReportTask 클래스 두 가지를 작성합니다.

### AuditTrail 클래스

- method: void record()

### TransferMoneyTask 클래스

- field: AuditTrail auditTrail

- method: void execute() {

  auditTrail.record()

  // blah blah

  }

### GenerateReportTask 클래스

- field: AuditTrail auditTrail

- method: void execute() {

  auditTrail.record()

  // blah blah

  }

아래와 같이 구현을 하였습니다.

[dart 코드](problem.dart)

[python 코드](problem.py)

### 문제

- code duplication. task를 새로 작성할 때마다 private field, constructor 등의 중복되는 코드를 작성해야 합니다.

- 중복되는 코드의 작성을 피하고 싶습니다.

- 올바른 작동을 보장하기 위해서 auditTrail을 반드시 기록해야 하지만, 강제성이 없습니다. 팀원 중 누군가 auditTrail 필드가 포함되지 않은 task 클래스를 작성한다면 치명적인 문제가 생길 수 있습니다.

- 클래스 작성에서 auditTrail 필드의 사용을 강제하고 싶습니다.
