import torch
import torch.nn as nn
import torch.nn.functional as F

from torchattacks import PGD

from ..advtrainer import AdvTrainer


class MART(AdvTrainer):
    r"""
    MART in 'Improving Adversarial Robustness Requires Revisiting Misclassified Examples'
    [https://openreview.net/forum?id=rklOg6EFwS]
    [https://github.com/YisenWang/MART]

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
        random_start (bool): using random initialization of delta.
    """
    def __init__(self, rmodel, eps, alpha, steps, beta, random_start=True):
        super().__init__("MART", rmodel)
        self.atk = PGD(rmodel, eps, alpha, steps, random_start)
        self.beta = beta

    def calculate_cost(self, train_data):
        r"""
        Overridden.
        """
        images, labels = train_data
        images = images.to(self.device)
        labels = labels.to(self.device)

        adv_images = self.atk(images, labels)

        logits_clean = self.rmodel(images)
        logits_adv = self.rmodel(adv_images)

        probs_adv = F.softmax(logits_adv, dim=1)

        # Caculate BCELoss
        tmp1 = torch.argsort(probs_adv, dim=1)[:, -2:]
        new_y = torch.where(tmp1[:, -1] == labels, tmp1[:, -2], tmp1[:, -1])
        loss_bce_adv = F.cross_entropy(logits_adv, labels) + \
                       F.nll_loss(torch.log(1.0001 - probs_adv + 1e-12), new_y)

        # Caculate KLLoss
        probs_clean = F.softmax(logits_clean, dim=1)
        log_prob_adv = torch.log(probs_adv + 1e-12)
        loss_kl = torch.sum(nn.KLDivLoss(reduction='none')(log_prob_adv, probs_clean),
                            dim=1)
        true_probs = torch.gather(probs_clean, 1, (labels.unsqueeze(1)).long()).squeeze()
        loss_weighted_kl = torch.mean(loss_kl * (1.0000001 - true_probs))

        cost = loss_bce_adv + self.beta * loss_weighted_kl

        self.record_dict["Loss"] = cost.item()
        self.record_dict["BALoss"] = loss_bce_adv.item()
        self.record_dict["WKLoss"] = loss_weighted_kl.item()

        return cost
