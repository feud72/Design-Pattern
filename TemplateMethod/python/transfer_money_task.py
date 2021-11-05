from audit_trail import AuditTrail
from task import Task


class TransferMoneyTask(Task):
    def __init__(self, audit_trail: AuditTrail) -> None:
        super().__init__(audit_trail)

    def doExecute(self) -> None:
        print("Transfer Money")
