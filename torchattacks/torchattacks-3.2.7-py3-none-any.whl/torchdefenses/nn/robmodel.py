from collections import OrderedDict

import torch
import torch.nn as nn

from torchattacks import FGSM, PGD, PGDL2, GN, AutoAttack, MultiAttack

from .modules.normalize import Normalize
from ..utils import get_accuracy


class RobModel(nn.Module):
    r"""
    Wrapper class for PyTorch models.
    """
    def __init__(self, model, n_classes,
                 normalize={'mean': [0., 0., 0.], 'std': [1., 1., 1.]},
                 device=None):
        super().__init__()
        assert isinstance(n_classes, int)
        self.model = model
        if device is None:
            device = next(model.parameters()).device
        self.register_buffer('n_classes', torch.tensor(n_classes))

        norm = Normalize(normalize['mean'], normalize['std'])
        self.model = nn.Sequential(norm, model)
        self.to(device)

    def forward(self, x):
        out = self.model(x)
        return out

    # Load from state dict
    def load_dict(self, save_path):
        state_dict = torch.load(save_path, map_location='cpu')
        self.load_state_dict_auto(state_dict['rmodel'])
        print("Model loaded.")

        if 'record_info' in state_dict.keys():
            print("Record Info:")
            print(state_dict['record_info'])

    # DataParallel considered version of load_state_dict.
    def load_state_dict_auto(self, state_dict):
        state_dict = self._convert_dict_auto(state_dict)
        self.load_state_dict(state_dict)

    def _convert_dict_auto(self, state_dict):
        keys = state_dict.keys()
        
        # for under v0.4.0 version models
        for old_key in ['norm.mean', 'norm.std', 'norm.n_channels', 'model.0.n_channels']:
            if old_key in state_dict: del state_dict[old_key]
        
        save_parallel = any(key.startswith("model.module.") for key in keys)
        curr_parallel = any(key.startswith("model.module.") for key in self.state_dict().keys())
        if save_parallel and not curr_parallel:
            new_state_dict = {k.replace("model.module.", "model."): v for k, v in state_dict.items()}
            return new_state_dict
        elif curr_parallel and not save_parallel:
            new_state_dict = {k.replace("model.", "model.module."): v for k, v in state_dict.items()}
            return new_state_dict
        else:
            return state_dict

    def save_dict(self, save_path):
        save_dict = OrderedDict()
        save_dict["rmodel"] = self.state_dict()
        torch.save(save_dict, save_path)

    def set_parallel(self):
        self.model = torch.nn.DataParallel(self.model)
        return self

    def named_parameters_with_module(self):
        module_by_name = {}
        for name, module in self.named_modules():
            module_by_name[name] = module

        for name, param in self.named_parameters():
            if '.' in name:
                module_name = name.rsplit(".", maxsplit=1)[0]
                yield name, param, module_by_name[module_name]
            else:
                yield name, param, None
    
    # Evaluation Robustness
    def eval_accuracy(self, data_loader):
        return get_accuracy(self, data_loader)

    def eval_rob_accuracy(self, data_loader, atk, save_path=None, verbose=True, save_pred=False):
        return atk.save(data_loader, save_path, verbose, return_verbose=True, save_pred=save_pred)[0]

    def eval_rob_accuracy_gn(self, data_loader, std, save_path=None, verbose=True, save_pred=False):
        atk = GN(self, std=std)
        return atk.save(data_loader, save_path, verbose, return_verbose=True, save_pred=save_pred)[0]

    def eval_rob_accuracy_fgsm(self, data_loader, eps, save_path=None, verbose=True, save_pred=False):
        atk = FGSM(self, eps=eps)
        return atk.save(data_loader, save_path, verbose, return_verbose=True, save_pred=save_pred)[0]

    def eval_rob_accuracy_pgd(self, data_loader, eps, alpha, steps, random_start=True,
                              restart_num=1, norm='Linf', save_path=None, verbose=True, save_pred=False):
        if norm == 'Linf':
            atk = PGD(self, eps=eps, alpha=alpha,
                      steps=steps, random_start=random_start)
        elif norm == 'L2':
            atk = PGDL2(self, eps=eps, alpha=alpha,
                        steps=steps, random_start=random_start)
        else:
            raise ValueError('Invalid norm.')

        if restart_num > 1:
            atk = MultiAttack([atk]*restart_num)
        return atk.save(data_loader, save_path, verbose, return_verbose=True, save_pred=save_pred)[0]

    def eval_rob_accuracy_autoattack(self, data_loader, eps, version='standard',
                                     norm='Linf', save_path=None, verbose=True, save_pred=False):
        atk = AutoAttack(self, norm=norm, eps=eps,
                         version=version, n_classes=self.n_classes)
        return atk.save(data_loader, save_path, verbose, return_verbose=True, save_pred=save_pred)[0]
