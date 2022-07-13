import torch
import torch.nn as nn

from torchattacks import PGD

from ..advtrainer import AdvTrainer


class AT(AdvTrainer):
    r"""
    Adversarial training in 'Towards Deep Learning Models Resistant to Adversarial Attacks'
    [https://arxiv.org/abs/1706.06083]

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
        eps (float): strength of the attack or maximum perturbation.
        alpha (float): step size.
        steps (int): number of steps.
        random_start (bool): using random initialization of delta.
    """
    def __init__(self, rmodel, eps, alpha, steps, random_start=True):
        super().__init__("AT", rmodel)
        self.atk = PGD(rmodel, eps, alpha, steps, random_start)

    def calculate_cost(self, train_data):
        r"""
        Overridden.
        """
        images, labels = train_data
        images = images.to(self.device)
        labels = labels.to(self.device)

        adv_images = self.atk(images, labels)
        logits_adv = self.rmodel(adv_images)

        cost = nn.CrossEntropyLoss()(logits_adv, labels)
        self.record_dict["CALoss"] = cost.item()
        return cost
