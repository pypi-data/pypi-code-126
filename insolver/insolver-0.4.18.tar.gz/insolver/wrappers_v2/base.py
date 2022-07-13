import os
import copy
import time

from insolver.wrappers_v2.save_utils import save, save_insolver


class InsolverBaseWrapper:
    """Base wrapper serving as a building block for other wrappers."""

    model, _back_save_dict, backend, algo = None, None, None, None

    def __call__(self):
        return self.model

    def _get_init_args(self, vars_):
        copy_vars = copy.deepcopy(vars_)
        copy_vars.pop("self")
        self.metadata = {"init_params": copy_vars}

    def save_model(self, path=None, name=None, form="insolver", method=None, **kwargs):
        """Saving the model contained in wrapper.

        Args:
            path (str, optional): Path to save the model. Using current working directory by default.
            name (str, optional): Model name.
            form (str, optional): Saving form, values ['insolver', 'raw'] are supported. Option 'raw' saves fitted model
             without additional metadata. Option 'insolver' saves model as a zip-file with model and json with metadata
             inside.
            method (str, optional): Saving method.
            **kwargs: Other parameters passed to, e.g. h2o.save_model().
        """
        _forms = ["insolver", "raw"]

        if method not in self._back_save_dict[self.backend]:
            raise ValueError(
                f'Invalid "{method}" value for parameter method. '
                f"Supported values for {self.backend} are {self._back_save_dict[self.backend]}."
            )

        if self.model is None:
            raise ValueError("No fitted model found.")

        if form not in _forms:
            raise ValueError(f'Invalid "{form}" value for parameter form. Supported values are {_forms}.')

        path = os.getcwd() if path is None else os.path.normpath(path)
        def_name = (
            f"{'insolver' if form == 'insolver' else method}_{self.algo}_{self.backend}_{round(time.time() * 1000)}"
        )
        name = name if name is not None else def_name

        if form == "insolver":
            self.metadata.update({"saving_method": method})
            save_insolver(self.model, self.metadata, path, name, method=method)
        else:
            save(self.model, path=path, name=name, method=method, binary=True, **kwargs)
        return os.path.normpath(os.path.join(path, name))

    def _update_meta(self):
        self.meta = self.__dict__.copy()
        for key in ["object", "model"]:
            self.meta.pop(key)
