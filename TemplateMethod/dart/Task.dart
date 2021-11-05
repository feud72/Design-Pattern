import 'AuditTrail.dart';

abstract class Task {
  AuditTrail _auditTrail;

  Task({
    required auditTrail,
  }) : _auditTrail = auditTrail;

  void execute() {
    _auditTrail.record();
    doExecute();
  }

  void doExecute();
}
