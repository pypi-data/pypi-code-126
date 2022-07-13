from .OAuth2 import OAuth2

import requests
import json


class QueueItems:

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

    def addQueueItem(self, queue_name: str, queue_item_reference: str, specific_content: dict, priority='Normal') -> int:
        """
        This function will add a queue item to a queue in Orchestrator
        
        :param queue_name: The name of the queue you want to add the item to
        :type queue_name: str
        :param queue_item_reference: This is the name of the queue item
        :type queue_item_reference: str
        :param specific_content: dict
        :type specific_content: dict
        :param priority: 'High', 'Normal', 'Low', defaults to Normal (optional)
        :return: The ID of the queue item that was created.
        """

        url = self.auth.base_url + '/odata/Queues/UiPathODataSvc.AddQueueItem'

        payload = json.dumps({
            "itemData": {
                "Name": queue_name,
                "Priority": priority,
                "Reference": queue_item_reference,
                "SpecificContent": specific_content
            }
        })

        headers = {
            'Content-Type': 'application/json',
            'X-UIPATH-OrganizationUnitId': self.folder_id,
            'Authorization': self.auth.auth_token
        }

        r = requests.post(url=url, headers=headers, data=payload)

        if r.status_code == 201:
            print(f"Queue Item '{queue_item_reference}' created.")
            return r.json()['Id']

        else:
            raise ValueError(
                "Server Error: " + str(r.status_code) +
                ".  " + r.json()['message']
            )

    def getQueueItem(self, queue_item_id: int):
        """
        This function will retrieve a queue item from Orchestrator based on the queue item ID.
        
        :param queue_item_id: The ID of the queue item you want to retrieve
        :type queue_item_id: int
        :return: A JSON object containing the queue item data.
        """

        url = self.auth.base_url + f'/odata/QueueItems({str(queue_item_id)})'

        payload = {}

        headers = {
            'Content-Type': 'application/json',
            'X-UIPATH-OrganizationUnitId': self.folder_id,
            'Authorization': self.auth.auth_token
        }

        r = requests.get(url=url, headers=headers, data=payload)

        if r.status_code == 200:
            data = r.json()
            print(f"Queue Item '{data['Reference']}' retrieved.")
            return data

        else:
            raise ValueError(
                "Server Error: " + str(r.status_code) +
                ".  " + r.json()['message']
            )
