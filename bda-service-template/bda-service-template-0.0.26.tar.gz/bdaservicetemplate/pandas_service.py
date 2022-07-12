from .generic_service import GenericService
import pandas as pd
import os
from fileioutilities.file_io import FileIO
from dsioutilities import Dataset


class PandasService(GenericService):
    def __init__(self):
        super().__init__()

    def get_dataset(self, name="input-dataset"):
        input_dataset = Dataset(name, dataset_type="tabular")
        
        # If list of csv concatenate them
        if isinstance(input_dataset.get_path(), list):
            df = pd.concat([pd.read_csv(filename) for filename in input_dataset.get_path()])
        else:
            df = pd.read_csv(input_dataset.get_path())
        return df

    def save_dataset(self, dataset: pd.DataFrame, name="output-dataset"):
        dataset.to_csv(Dataset(name, dataset_type="tabular").get_path(), index=False)

    def download_model(self, name='input_model'):
        path = os.path.join(".", "model")
        FileIO(name=name).download(local_path=path)
        return path

    def upload_model(self, path, name='output_model'):
        fileIO = FileIO(name=name)
        fileIO.upload(local_path=path)
