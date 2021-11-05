from audit_trail import AuditTrail
from transfer_money_task import TransferMoneyTask
from generate_report_task import GenerateReportTask


def main():
    audit_trail = AuditTrail()
    task = TransferMoneyTask(audit_trail=audit_trail)
    task.execute()

    anotherTask = GenerateReportTask(audit_trail=audit_trail)
    anotherTask.execute()


main()
