import pandas as pd
import kdp_api
from kdp_api.api import read_api
from kdp_api.models import SequenceReadRequest
from kdp_api.models import RecordBatch


class ReadApi(object):

    def read_dataset_in_sequence(self, config, dataset_id: str,
                                 starting_record_id: str = '', batch_size: int = 1000):
        with kdp_api.ApiClient(config) as api_client:
            api_instance = read_api.ReadApi(api_client)
            has_more_records = bool(True)
            dictionary_list = []

            while has_more_records:
                record_batch: RecordBatch = self.read_batch_in_sequence(
                    api_instance=api_instance,
                    dataset_id=dataset_id,
                    starting_record_id=starting_record_id,
                    batch_size=batch_size)
                has_more_records = record_batch.more
                starting_record_id = record_batch.last_record_id
                for json_record in record_batch.records:
                    dictionary_list.append(json_record['_data_store'])

            return dictionary_list

    @staticmethod
    def read_batch_in_sequence(api_instance, dataset_id: str, starting_record_id: str,
                               batch_size: int):
        sequence_read_request = SequenceReadRequest(dataset_id=dataset_id,
                                                    starting_record_id=starting_record_id,
                                                    batch_size=batch_size)
        return api_instance.read_in_sequence(sequence_read_request=sequence_read_request)

    def read_dataset_to_dictionary_list(self, config, dataset_id: str, starting_record_id: str = '',
                                        batch_size: int = 100000):

        return self.read_dataset_in_sequence(config=config,
                                             dataset_id=dataset_id,
                                             starting_record_id=starting_record_id,
                                             batch_size=batch_size)

    def read_dataset_to_pandas_dataframe(self, config, dataset_id: str, starting_record_id: str = '',
                                         batch_size: int = 100000):
        dictionary_list = self.read_dataset_to_dictionary_list(config, dataset_id, starting_record_id,
                                                               batch_size)
        return pd.DataFrame(dictionary_list)


    def get_splits(self, config, dataset_id: str):
        with kdp_api.ApiClient(config) as api_client:
            api_instance = read_api.ReadApi(api_client)

            return api_instance.get_splits(dataset_id=dataset_id)


    def read_batch(self, config, dataset_id: str, starting_record_id: str, ending_record_id:str,
        exclude_starting_record_id: bool, batch_size: int = 10):
        with kdp_api.ApiClient(config) as api_client:
            api_instance = read_api.ReadApi(api_client)

            request = {}
            request['datasetId'] = dataset_id
            request['excludeStartingRecordId'] = exclude_starting_record_id
            request['startingRecordId'] = starting_record_id
            request['endingRecordId'] = ending_record_id
            request['batchSize'] = batch_size

            return api_instance.read(request)
