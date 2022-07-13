from .OAuth2 import OAuth2
from typing import Tuple, Any

import requests
import json


class QueueDefinitions:

    def __init__(self, auth: OAuth2, folder_id: str):
        """
        This function is used to initialize the class
        
        :param auth: OAuth2
        :type auth: OAuth2
        :param folder_id: The ID of the folder you want to upload the file to
        :type folder_id: str
        """

        self.auth = auth
        self.folder_id = folder_id

    def getQueueDefinitions(self):
        """
        It returns a list of all the queues in the Orchestrator instance
        :return: A list of queue definitions.
        """

        url = self.auth.base_url + '/odata/QueueDefinitions'

        payload = {}

        headers = {
            'X-UIPATH-OrganizationUnitId': self.folder_id,
            'Authorization': self.auth.auth_token
        }

        r = requests.get(url=url, headers=headers, data=payload)

        if r.status_code == 200:
            return_value = r.json()
            return return_value

        else:
            raise ValueError(
                "Server Error: " + str(r.status_code) +
                ".  " + r.json()['message']
            )

    def checkQueueDefinitionExists(self, queue_name: str) -> Tuple[bool, Any]:
        """
        It checks if a queue exists in a folder
        
        :param queue_name: The name of the queue you want to check for
        :type queue_name: str
        :return: A boolean value.
        """

        queueExists: bool = None

        existingQueueDefinitions = self.getQueueDefinitions()
        queue_def = existingQueueDefinitions

        for queue in existingQueueDefinitions['value']:
            existingQueueName = str(queue['Name'])
            if existingQueueName.strip() == queue_name.strip():
                queueExists = True
                queue_def = queue
                break
            else:
                queueExists = False

        return (queueExists, queue_def)

    def createNewQueueDefinition(self, queue_name: str, description: str, max_retries: int, auto_retry=False, enforce_unique=False) -> Any:
        """
        This function creates a new queue definition in Orchestrator
        
        :param queue_name: The name of the queue you want to create
        :type queue_name: str
        :param description: str,
        :type description: str
        :param max_retries: The maximum number of times a job can be retried
        :type max_retries: int
        :param auto_retry: If true, the queue item will be automatically retried if the robot fails to
        process it, defaults to False (optional)
        :param enforce_unique: If true, the queue item will be rejected if the reference is not unique,
        defaults to False (optional)
        :return: A tuple containing a boolean and a dictionary.
        """

        url = self.auth.base_url + '/odata/QueueDefinitions'

        payload = json.dumps({
            "Name": queue_name,
            "Description": description,
            "MaxNumberOfRetries": max_retries,
            "AcceptAutomaticallyRetry": auto_retry,
            "EnforceUniqueReference": enforce_unique
        })

        headers = {
            'Content-Type': 'application/json',
            'X-UIPATH-OrganizationUnitId': self.folder_id,
            'Authorization': self.auth.auth_token
        }

        (qDefExists, qDef) = self.checkQueueDefinitionExists(queue_name)

        if qDefExists:
            print(f'Queue {queue_name} already exists and cannot be created.')
            return qDef
        else:
            r = requests.post(url=url, headers=headers, data=payload)

            if r.status_code == 201:
                print(f'Queue {queue_name} created.')
                return_value = r.json()
                return return_value

            else:
                raise ValueError(
                    "Server Error: " + str(r.status_code) +
                    ".  " + r.json()['message']
                )