void main(List<String> args) {
  var auditTrail = AuditTrail();
  var task = TransferMoneyTask(auditTrail: auditTrail);
  task.execute();

  var anotherTask = GenerateReportTask(auditTrail: auditTrail);
  anotherTask.execute();
}

class TransferMoneyTask {
  AuditTrail _auditTrail;

  TransferMoneyTask({required auditTrail}) : _auditTrail = auditTrail;

  void execute() {
    this._auditTrail.record();
    print("Transfer Money");
  }
}

class GenerateReportTask {
  AuditTrail _auditTrail;

  GenerateReportTask({required auditTrail}) : _auditTrail = auditTrail;

  void execute() {
    this._auditTrail.record();
    print("Generate Report");
  }
}

class AuditTrail {
  void record() {
    print("Audit");
  }
}
