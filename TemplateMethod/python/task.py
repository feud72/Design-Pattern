from abc import ABCMeta, abstractmethod
from audit_trail import AuditTrail


class Task(metaclass=ABCMeta):
    def __init__(self, audit_trail: AuditTrail) -> None:
        self.__audit_trail = audit_trail

    def execute(self) -> None:
        self.__audit_trail.record()
        self.doExecute()

    @abstractmethod
    def doExecute(self) -> None:
        pass
