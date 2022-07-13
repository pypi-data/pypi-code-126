import torch
import torch.nn as nn
import torch.nn.functional as F

from torchattacks import TPGD

from ..advtrainer import AdvTrainer


class TRADES(AdvTrainer):
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
        beta (float): trade-off regularization parameter.
    """
    def __init__(self, rmodel, eps, alpha, steps, beta):
        super().__init__("TRADES", rmodel)
        self.atk = TPGD(rmodel, eps, alpha, steps)
        self.beta = beta

    def calculate_cost(self, train_data):
        r"""
        Overridden.
        """
        images, labels = train_data
        images = images.to(self.device)
        labels = labels.to(self.device)

        adv_images = self.atk(images)

        logits_clean = self.rmodel(adv_images)
        loss_ce = nn.CrossEntropyLoss()(logits_clean, labels)

        logits_adv = self.rmodel(adv_images)
        probs_clean = F.softmax(logits_clean, dim=1)
        log_probs_adv = F.log_softmax(logits_adv, dim=1)
        loss_kl = nn.KLDivLoss(reduction='batchmean')(log_probs_adv, probs_clean)

        cost = loss_ce + self.beta * loss_kl

        self.record_dict["Loss"] = cost.item()
        self.record_dict["CELoss"] = loss_ce.item()
        self.record_dict["KLLoss"] = loss_kl.item()

        return cost
