class AuditTrail:
    def record(self) -> None:
        print("Audit")


class TransferMoneyTask:
    def __init__(self, audit_trail: AuditTrail) -> None:
        self.__audit_trail = audit_trail

    def execute(self) -> None:
        self.__audit_trail.record()
        print("Transfer Money")


class GenerateReportTask:
    def __init__(self, audit_trail: AuditTrail) -> None:
        self.__audit_trail = audit_trail

    def execute(self) -> None:
        self.__audit_trail.record()
        print("Generate Report")


def main():
    audit_trail = AuditTrail()
    task = TransferMoneyTask(audit_trail=audit_trail)
    task.execute()

    anotherTask = GenerateReportTask(audit_trail=audit_trail)
    anotherTask.execute()


main()
