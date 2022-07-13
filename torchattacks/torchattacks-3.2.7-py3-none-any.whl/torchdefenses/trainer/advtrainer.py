import torch

from ._trainer import Trainer
from ..utils import get_subloader

r"""
Base class for adversarial trainers.

Functions:
    self.record_rob : function for recording standard accuracy and robust accuracy against FGSM, PGD, and GN.

"""


class AdvTrainer(Trainer):
    def __init__(self, name, rmodel):
        super(AdvTrainer, self).__init__(name, rmodel)
        self._flag_record_rob = False

    def record_rob(self, train_loader, val_loader,
                   eps=None, alpha=None, steps=None, std=None,
                   n_train_limit=None, n_val_limit=None):
        self._flag_record_rob = True
        self._record_rob_keys = ['Clean']
        self._train_loader_rob = get_subloader(train_loader, n_train_limit)
        self._val_loader_rob = get_subloader(val_loader, n_val_limit)
        self._init_record_keys = self._init_record_keys_with_rob
        
        if eps is not None: # FGSM, PGD
            self._eps_rob = eps
            self._record_rob_keys.append('FGSM')
        
            # PGD
            if (alpha is not None) and (steps is not None):
                self._alpha_rob = alpha
                self._steps_rob = steps
                self._record_rob_keys.append('PGD')
            elif (alpha is None) and (steps is not None):
                raise ValueError('Both alpha and steps should be given for PGD.')
            elif (alpha is not None) and (steps is None):
                raise ValueError('Both alpha and steps should be given for PGD.')
        
        # GN
        if std is not None:
            self._std_rob = std
            self._record_rob_keys.append('GN')

    def _init_record_keys_with_rob(self, record_type):
        # Add Epoch and Iter to Record_keys
        keys = ["Epoch"]
        if record_type == "Iter":
            keys = ["Epoch", "Iter"]

        # Add Custom Record_dict keys to Record_keys
        for key in self.record_dict.keys():
            keys.append(key)

        # Add robust keys
        keys += [key + '(Tr)' for key in self._record_rob_keys]
        keys += [key + '(Val)' for key in self._record_rob_keys]

        # Add lr to Record_keys
        keys.append("lr")
        return keys

    # Update Records
    def _update_record(self, record, lr):
        if self._flag_record_rob:
            rob_record = []
            for loader in [self._train_loader_rob, self._val_loader_rob]:
                rob_record.append(self.rmodel.eval_accuracy(loader))
                if 'FGSM' in self._record_rob_keys:
                    rob_record.append(self.rmodel.eval_rob_accuracy_fgsm(loader,
                                                                         eps=self._eps_rob,
                                                                         verbose=False))
                if 'PGD' in self._record_rob_keys:
                    rob_record.append(self.rmodel.eval_rob_accuracy_pgd(loader,
                                                                        eps=self._eps_rob,
                                                                        alpha=self._alpha_rob,
                                                                        steps=self._steps_rob,
                                                                        verbose=False))
                if 'GN' in self._record_rob_keys:
                    rob_record.append(self.rmodel.eval_rob_accuracy_gn(loader,
                                                                       std=self._std_rob,
                                                                       verbose=False))
            return record + rob_record + [lr]

        return record + [lr]
