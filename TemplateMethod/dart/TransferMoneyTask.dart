import 'AuditTrail.dart';
import 'Task.dart';

class TransferMoneyTask extends Task {
  TransferMoneyTask({
    required AuditTrail auditTrail,
  }) : super(auditTrail: auditTrail);

  @override
  void doExecute() {
    print("Transfer Money");
  }
}
