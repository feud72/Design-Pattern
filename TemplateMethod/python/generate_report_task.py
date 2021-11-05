from audit_trail import AuditTrail
from task import Task


class GenerateReportTask(Task):
    def __init__(self, audit_trail: AuditTrail) -> None:
        super().__init__(audit_trail)

    def doExecute(self) -> None:
        print("Generate Report")
