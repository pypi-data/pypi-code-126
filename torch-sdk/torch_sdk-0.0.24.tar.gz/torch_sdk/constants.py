from enum import Enum

class RuleExecutionStatus(Enum):
    STARTED = 1
    RUNNING = 2
    ERRORED = 3
    WARNING = 4
    SUCCESSFUL = 5
    ABORTED = 6


DATA_QUALITY = 'DATA_QUALITY'
RECONCILIATION = 'RECONCILIATION'
