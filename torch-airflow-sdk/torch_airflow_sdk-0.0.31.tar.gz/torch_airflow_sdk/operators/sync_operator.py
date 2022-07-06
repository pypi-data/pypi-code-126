from airflow.models.baseoperator import BaseOperator
from torch_sdk.torch_client import TorchClient
from torch_airflow_sdk.initialiser import torch_credentials
from torch_sdk.common import SyncExecutor
import torch_sdk.constants as const


class SyncOperator(BaseOperator):
    """
    Description:
        SyncOperator is used to execute a policy by passing rule_type and rule_id.
        It will return only after the execution ends.

        :param rule_type: (String) TYpe of rule to be executed
        :param rule_id: (String) id of the rule to be executed
        :param incremental: (bool) optional Set it to True if full execution has to be done
    """

    def __init__(self, *, rule_type, rule_id, incremental=False, **kwargs):
        """
        :param rule_type: (String) TYpe of rule to be executed
        :param rule_id: (String) id of the rule to be executed
        :param incremental: (bool) optional Set it to True if full execution has to be done

        Example:
        syncoperator_task = SyncOperator(
            task_id='torch_pipeline_SYNCOPERATORTEST',
            rule_type='DATA_QUALITY',
            rule_id=46,
            dag=dag
        )

        In case you need to query the status in another task you need to pull the execution id from xcom by passing
        the rule name in the {rule_name}_execution_id. In this example the rule name of rule _id 46 is 'policy_with_email'

        After getting the execution_id you need to create object of SyncExecutor by passing rule_type and
        torch_client object and call get_status using the execution_id.

        def syncoperator_RESULT(**context):
            xcom_key = 'policy_with_email_execution_id'
            task_instance = context['ti']
            # get the rule_name and execution id - then push them in xcom
            execution_id = task_instance.xcom_pull(key=xcom_key)

            torch_client = TorchClient(**torch_credentials)
            sync_executor = SyncExecutor('DATA_QUALITY', torch_client)
            execution_status = sync_executor.get_status(execution_id)

        """
        super().__init__(**kwargs)
        self.rule_type = rule_type
        self.rule_id = rule_id
        self.incremental = incremental

    def execute(self, context):
        torch_client = TorchClient(**torch_credentials)
        execution_return = torch_client.execute_rule(self.rule_type, self.rule_id, sync=True, incremental=self.incremental)
        xcom_key = f'{self.rule_type}_{self.rule_id}_execution_id'
        task_instance = context['ti']
        # get the rule_name and execution id - then push them in xcom
        task_instance.xcom_push(key=xcom_key, value=execution_return.id)
