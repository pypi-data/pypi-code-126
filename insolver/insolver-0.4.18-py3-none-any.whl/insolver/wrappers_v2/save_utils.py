import os
import json
import pickle
import joblib

from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED


def save(obj, path=None, name=None, method=None, binary=True, **kwargs):
    if method == "pickle":
        if binary:
            with open(os.path.join(path, f"{name}.pickle"), "wb") as _file:
                pickle.dump(obj, _file, **kwargs)
        else:
            return pickle.dumps(obj, **kwargs)
    elif method == "joblib":
        if binary:
            joblib.dump(obj, os.path.join(path, f"{name}.joblib"))
        else:
            container = BytesIO()
            joblib.dump(obj, container)
            container.seek(0)
            return container
    else:
        raise ValueError(f'Invalid method "{method}" argument.')


def save_insolver(model, metadata, path=None, name=None, method=None, **kwargs):
    buffer = BytesIO()
    with ZipFile(buffer, mode="x", compression=ZIP_DEFLATED) as zip_file:
        zip_file.writestr("metadata.json", json.dumps(metadata))
        zip_file.writestr(
            f"model_{name}",
            BytesIO(save(model, binary=False, method=method, **kwargs)).getvalue(),
        )
    with open(os.path.join(path, name), "xb") as f:
        f.write(buffer.getvalue())


# def load(path, method, **kwargs):
#     if method == 'pickle':
#         with open(path, 'rb') as _file:
#             return pickle.load(_file)
#     elif method == 'joblib':
#         return joblib.load(path)

# self._back_load_dict = {'sklearn': self._pickle_load,
#                         'h2o': partial(self._h2o_load, h2o_init_params=h2o_init_params)}
# self._back_save_dict = {'sklearn': self._pickle_save, 'h2o': self._h2o_save}

# def _pickle_load(self, load_path):
#     with open(load_path, 'rb') as _model:
#         self.model = pickle.load(_model)
#
# def _pickle_save(self, path, name):
#     with open(os.path.join(path, f'{name}.pickle'), 'wb') as _model:
#         pickle.dump(self.model, _model, pickle.HIGHEST_PROTOCOL)
#
# def _joblib_load(self, load_path):
#     self.model = joblib.load(load_path)
#
# def _joblib_save(self, path, name):
#     joblib.dump(self.model, os.path.join(path, f'{name}.joblib'))

#
# metadata['algo']
# metadata['task']
# metadata['model_class']
# metadata['backend']
# metadata['saving_method']


# def load(load_path):
#     """Loading a model to the wrapper.
#
#     Args:
#         load_path (str): Path to the model that will be loaded to wrapper.
#     """
#     load_path = os.path.normpath(load_path)
#     if backend in self._back_load_dict.keys():
#         self._back_load_dict[self.backend](load_path)
#     else:
#         raise NotImplementedError(f'Error with the backend choice. Supported backends: {self._backends}')
