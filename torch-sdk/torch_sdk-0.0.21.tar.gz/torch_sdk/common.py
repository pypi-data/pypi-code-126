from time import sleep
import logging
from torch_sdk.errors import TorchSdkException
import torch_sdk.constants as const
LOGGER = logging.getLogger("common")


class RuleExecutionResult:
    def __init__(self, execution_details):
        self.item = execution_details.items
        self.result = execution_details.result
        self.rule_id = execution_details.execution.ruleId
        self.rule_name = execution_details.execution.ruleName
        self.rule_version = execution_details.execution.ruleVersion
        self.rule_type = execution_details.execution.ruleType
        self.started_at = execution_details.execution.startedAt
        self.finished_at = execution_details.execution.finishedAt
        self.execution_id = execution_details.execution.id

    def __eq__(self, other):
        return self.execution_id == other.execution_id

    def __repr__(self):
        return f"RuleExecutionResult({self.__dict__})"


class Executor:
    def __init__(self, rule_type, torch_client):
        self.id = None
        self.exec_call, self.result_call = get_callables(rule_type, torch_client)

    def get_status(self, execution_id=None):
        if execution_id is None:
            if self.id is not None:
                execution_id = self.id
            else:
                raise TorchSdkException('execution_id is required.')
        print('Getting rule execution status.')
        execution_details = self.result_call(execution_id=execution_id)
        return const.RuleExecutionStatus[execution_details.execution.executionStatus]

    def get_result(self, execution_id=None, sleep_interval=5, total_retries=0):
        if execution_id is None:
            if self.id is not None:
                execution_id = self.id
            else:
                raise TorchSdkException('execution_id is required.')

        retry_count = 0
        while 1:
            execution_details = self.result_call(execution_id=execution_id)
            print(f'Checking rule execution result')
            if const.RuleExecutionStatus[execution_details.execution.executionStatus] == const.RuleExecutionStatus.SUCCESSFUL \
                    and const.RuleExecutionStatus[execution_details.execution.resultStatus] == const.RuleExecutionStatus.SUCCESSFUL:
                print('Rule completed successfully.')
                return RuleExecutionResult(execution_details)
            elif const.RuleExecutionStatus[execution_details.execution.executionStatus] == const.RuleExecutionStatus.RUNNING \
                    and const.RuleExecutionStatus[execution_details.execution.resultStatus] == const.RuleExecutionStatus.RUNNING:
                sleep(sleep_interval)
                retry_count = retry_count + 1
                if (total_retries == 0) or (total_retries > 0 and retry_count < total_retries):
                    continue
                else:
                    print(f'Exiting after {total_retries} retries.')
                    return
            else:
                raise TorchSdkException(f'Rule execution failed. Details:{execution_details}')


def get_callables(rule_type, torch_client):
    if rule_type == const.RECONCILIATION:
        result_call = torch_client.get_reconciliation_rule_result
        exec_call = torch_client.execute_reconciliation_rule
    elif rule_type == const.DATA_QUALITY:
        result_call = torch_client.get_dq_rule_result
        exec_call = torch_client.execute_dq_rule
    else:
        raise TorchSdkException(f'{rule_type} not found. Please provide correct rule_type.'
                                f' Allowed values are {const.RECONCILIATION}, {const.DATA_QUALITY}')
    return exec_call, result_call


class SyncExecutor(Executor):
    def execute(self, rule_id, incremental=False, sleep_interval=5, total_retries=0):
        execution_obj = self.exec_call(rule_id=rule_id, incremental=incremental)
        retry_count = 0
        while 1:
            execution_details = self.result_call(execution_id=execution_obj.id)
            print('Checking rule execution result.')
            if const.RuleExecutionStatus[execution_details.execution.executionStatus] == const.RuleExecutionStatus.SUCCESSFUL \
                    and const.RuleExecutionStatus[execution_details.execution.resultStatus] == const.RuleExecutionStatus.SUCCESSFUL:
                print('Rule completed successfully.')
                self.id = execution_details.execution.id
                return execution_details.execution
            elif const.RuleExecutionStatus[execution_details.execution.executionStatus] == const.RuleExecutionStatus.RUNNING \
                    and const.RuleExecutionStatus[execution_details.execution.resultStatus] == const.RuleExecutionStatus.RUNNING:
                sleep(sleep_interval)
                retry_count = retry_count + 1
                if (total_retries == 0) or (total_retries > 0 and retry_count < total_retries):
                    continue
                else:
                    print(f'Exiting after {total_retries} retries.')
            else:
                raise TorchSdkException(f'Rule execution failed. Details:{execution_details}')


class AsyncExecutor(Executor):
    def execute(self, rule_id, incremental=False):
        execution_obj = self.exec_call(rule_id=rule_id, incremental=incremental)
        self.id = execution_obj.id
        return execution_obj


