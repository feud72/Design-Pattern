import 'AuditTrail.dart';
import 'TransferMoneyTask.dart';

void main(List<String> args) {
  var auditTrail = AuditTrail();
  var task = new TransferMoneyTask(auditTrail: auditTrail);
  task.execute();
}
