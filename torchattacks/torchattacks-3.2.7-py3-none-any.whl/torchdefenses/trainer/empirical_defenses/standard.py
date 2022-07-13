import torch
import torch.nn as nn

from ..advtrainer import AdvTrainer


class Standard(AdvTrainer):
    r"""
    Attributes:
        self.rmodel : rmodel.
        self.device : device where rmodel is.
        self.optimizer : optimizer.
        self.scheduler : scheduler (Automatically updated).
        self.max_epoch : total number of epochs.
        self.max_iter : total number of iterations.
        self.epoch : current epoch starts from 1 (Automatically updated).
        self.iter : current iters starts from 1 (Automatically updated).
            * e.g., is_last_batch = (self.iter == self.max_iter)
        self.record_dict : dictionary for printing records.

    Arguments:
        rmodel (nn.Module): rmodel to train.
    """
    def __init__(self, rmodel):
        super().__init__("Standard", rmodel)

    def calculate_cost(self, train_data):
        r"""
        Overridden.
        """
        images, labels = train_data
        images = images.to(self.device)
        labels = labels.to(self.device)
        logits = self.rmodel(images)

        cost = nn.CrossEntropyLoss()(logits, labels)
        self.record_dict["CALoss"] = cost.item()
        return cost
