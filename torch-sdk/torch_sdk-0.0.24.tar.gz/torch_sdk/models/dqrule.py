from enum import Enum, auto


class RuleType(Enum):
    DATA_QUALITY = auto()
    RECONCILIATION = auto()
    EQUALITY = auto()
    DATA_DRIFT = auto()
    SCHEMA_DRIFT = auto()


class RuleExecutionMode(Enum):
    SCHEDULED = auto()
    MANUAL = auto()
    WEBHOOK = auto()
    API = auto()


class RuleExecutionStatus(Enum):
    STARTED = auto()
    RUNNING = auto()
    ERRORED = auto()
    WARNING = auto()
    SUCCESSFUL = auto()
    ABORTED = auto()


class RuleResultStatus(Enum):
    STARTED = auto()
    RUNNING = auto()
    ERRORED = auto()
    WARNING = auto()
    SUCCESSFUL = auto()
    ABORTED = auto()


class PolicyExecutionType(Enum):
    SAMPLE = auto()
    FULL = auto()
    INCREMENTAL = auto()


class RuleThresholdLevel:
    def __init__(self, success, warning=None, **kwargs):
        self.success = success
        self.warning = warning
        
    def __repr__(self):
        return f"RuleThresholdLevel({self.__dict__})"


class LivyExecutorConfig:
    def __init__(self, executorMemory=None, executorCores=None, numExecutors=None, **kwargs):
        self.executorMemory = executorMemory
        self.executorCores = executorCores
        self.numExecutors = numExecutors

    def __repr__(self):
        return f"LivyExecutorConfig({self.__dict__})"


class DataBricksExecutorConfig:
    def __init__(self, minWorkers=None, maxWorkers=None, clusterWorkerType=None, clusterDriverType=None, **kwargs):
        self.minWorkers = minWorkers
        self.maxWorkers = maxWorkers
        self.clusterWorkerType = clusterWorkerType
        self.clusterDriverType = clusterDriverType
    
    def __repr__(self):
        return f"DataBricksExecutorConfig({self.__dict__})"


class ExecutorConfig:
    def __init__(self, livy=None, databricks=None, **kwargs):
        if isinstance(livy, dict):
            self.livy = LivyExecutorConfig(**livy)
        else:
            self.livy = livy
        if isinstance(databricks, dict):
            self.databricks = DataBricksExecutorConfig(**databricks)
        else:
            self.databricks = databricks

    def __repr__(self):
        return f"ExecutorConfig({self.__dict__})"


class RuleExecutionSummary:
    def __init__(self, ruleId, executionMode, executionStatus, resultStatus, startedAt, executionType, thresholdLevel,
                 ruleVersion, id=None, ruleName=None, ruleType=None, lastMarker=None, leftLastMarker=None,
                 rightLastMarker=None, executionError=None, finishedAt=None, resetPoint=None, persistencePath=None,
                 resultPersistencePath=None, executorConfig=None, markerConfig=None, leftMarkerConfig=None,
                 rightMarkerConfig=None, **kwargs):

        self.ruleId = ruleId
        self.id = id
        self.ruleName = ruleName
        if isinstance(ruleType, dict):
            self.ruleType = RuleType(**ruleType)
        else:
            self.ruleType = ruleType
        if isinstance(executionMode, dict):
            self.executionMode = RuleExecutionMode(**executionMode)
        else:
            self.executionMode = executionMode
        if isinstance(executionStatus, dict):
            self.executionStatus = RuleExecutionStatus(**executionStatus)
        else:
            self.executionStatus = executionStatus
        if isinstance(resultStatus, dict):
            self.resultStatus = RuleResultStatus(**resultStatus)
        else:
            self.resultStatus = resultStatus
        
        self.lastMarker = lastMarker
        self.leftLastMarker = leftLastMarker
        self.rightLastMarker = rightLastMarker
        self.executionError = executionError
        self.startedAt = startedAt
        self.finishedAt = finishedAt
        
        if isinstance(thresholdLevel, dict):
            self.thresholdLevel = RuleThresholdLevel(**thresholdLevel)
        else:
            self.thresholdLevel = thresholdLevel
        self.resetPoint = resetPoint
        self.persistencePath = persistencePath
        self.resultPersistencePath = resultPersistencePath
        self.ruleVersion = ruleVersion
        if isinstance(executorConfig, dict):
            self.executorConfig = ExecutorConfig(**executorConfig)
        else:
            self.executorConfig = executorConfig
        self.markerConfig = markerConfig
        self.leftMarkerConfig = leftMarkerConfig
        self.rightMarkerConfig = rightMarkerConfig
        if isinstance(executionType, dict):
            self.executionType = PolicyExecutionType(**executionType)
        else:
            self.executionType = executionType

    def __repr__(self):
        return f"RuleExecutionSummary({self.__dict__})"


class RootCauseAnalysis:
    def __init__(self, key, bad, good, badFraction, goodFraction,**kwargs):
        self.key = key
        self.bad = bad
        self.good = good
        self.badFraction = badFraction
        self.goodFraction = goodFraction

    def __repr__(self):
        return f"RootCauseAnalysis({self.__dict__})"


class RuleExecutionResult:
    def __init__(self, status, description=None, successCount=None, failureCount=None, rows=None, failedRows=None,
                 qualityScore=None, rca=None, **kwargs):
        if isinstance(status, dict):
            self.status = RuleResultStatus(**status)
        else:
            self.status = status
        self.description = description
        self.successCount = successCount
        self.failureCount = failureCount
        self.failedRows = failedRows
        self.qualityScore = qualityScore
        self.rows = rows
        if isinstance(rca, dict):
            self.rca = RootCauseAnalysis(**rca)
        else:
            self.rca = rca
    
    def __repr__(self):
        return f"RuleExecutionResult({self.__dict__})"


class RuleItemResult:
    def __init__(self, id, ruleItemId, threshold, weightage, isWarning, resultPercent=None, businessItemId=None,
                 success=None, error=None, **kwargs):
        self.id = id
        self.ruleItemId = ruleItemId
        self.businessItemId = businessItemId
        self.threshold = threshold
        self.resultPercent = resultPercent
        self.resultPercent = resultPercent
        self.success = success
        self.error = error
        self.weightage = weightage
        self.isWarning = isWarning

    def __repr__(self):
        return f"RuleItemResult({self.__dict__})"


class DataQualityRuleExecutionResult:
    def __init__(self, execution, items, meta=None, result=None, **kwargs):
        if isinstance(execution, dict):
            self.execution = RuleExecutionSummary(**execution)
        else:
            self.execution = execution
        if isinstance(result, dict):
            self.result = RuleExecutionResult(**result)
        else:
            self.result = result
        self.items = list()
        for obj in items:
            if isinstance(obj, dict):
                self.items.append(RuleItemResult(**obj))
            else:
                self.items.append(obj)

        self.meta = meta
        self.executionId = self.execution.id

    def __repr__(self):
        return f"DataQualityRuleExecutionResult({self.__dict__})"
