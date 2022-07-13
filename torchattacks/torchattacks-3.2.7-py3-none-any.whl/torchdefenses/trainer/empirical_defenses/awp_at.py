import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from torchattacks import PGD

from ..advtrainer import AdvTrainer

from collections import OrderedDict
import copy


EPS = 1E-20


def diff_in_weights(model, proxy):
    diff_dict = OrderedDict()
    model_state_dict = model.state_dict()
    proxy_state_dict = proxy.state_dict()
    for (old_k, old_w), (new_k, new_w) in zip(model_state_dict.items(), proxy_state_dict.items()):
        if len(old_w.size()) <= 1:
            continue
        if 'weight' in old_k:
            diff_w = new_w - old_w
            diff_dict[old_k] = old_w.norm() / (diff_w.norm() + EPS) * diff_w
    return diff_dict


def add_into_weights(model, diff, coeff=1.0):
    names_in_diff = diff.keys()
    with torch.no_grad():
        for name, param in model.named_parameters():
            if name in names_in_diff:
                param.add_(coeff * diff[name])


class AdvWeightPerturb(object):
    def __init__(self, model, proxy, proxy_optim, gamma):
        super(AdvWeightPerturb, self).__init__()
        self.model = model
        self.proxy = proxy
        self.proxy_optim = proxy_optim
        self.gamma = gamma

    def calc_awp(self, inputs_adv, targets):
        self.proxy.load_state_dict(self.model.state_dict())
        self.proxy.train()
        
        loss = - F.cross_entropy(self.proxy(inputs_adv), targets)

        self.proxy_optim.zero_grad()
        loss.backward()
        self.proxy_optim.step()

        # the adversary weight perturb
        diff = diff_in_weights(self.model, self.proxy)
        return diff

    def perturb(self, diff):
        add_into_weights(self.model, diff, coeff=1.0 * self.gamma)

    def restore(self, diff):
        add_into_weights(self.model, diff, coeff=-1.0 * self.gamma)
        
        
class AWP_AT(AdvTrainer):
    r"""
    Adversarial training in 'Adversarial Weight Perturbation Helps Robust Generalization' 
    [https://arxiv.org/pdf/2004.05884]
    [https://github.com/csdongxian/AWP]

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
        self.record_keys : names of items returned by do_iter.

    Arguments:
        rmodel (nn.Module): rmodel to train.
        eps (float): strength of the attack or maximum perturbation.
        alpha (float): step size.
        steps (int): number of steps.
        awp_gamma (float): regularization parameter for AWP.
        proxy_lr (float): learning rate of proxy model in AWP.
        random_start (bool): using random initialization of delta.
    """
    def __init__(self, rmodel, eps, alpha, steps, awp_gamma=0.01, proxy_lr = 0.01, random_start=True):
        super().__init__("AWP_AT", rmodel)
        self.atk = PGD(rmodel, eps, alpha, steps, random_start)

        self.proxy = copy.deepcopy(self.rmodel.model)
        self.proxy_opt = torch.optim.SGD(self.proxy.parameters(), lr=proxy_lr)
        self.awp_adversary = AdvWeightPerturb(model=self.rmodel.model, proxy=self.proxy, proxy_optim=self.proxy_opt, gamma=awp_gamma)

    def _do_iter(self, train_data):
        r"""
        Overridden.
        """
        images, labels = train_data
        images = images.to(self.device)
        labels = labels.to(self.device)

        adv_images = self.atk(images, labels)

        awp = self.awp_adversary.calc_awp(inputs_adv=adv_images,
                                          targets=labels)
        self.awp_adversary.perturb(awp)

        logits_adv = self.rmodel(adv_images)
        cost = nn.CrossEntropyLoss()(logits_adv, labels)

        self.optimizer.zero_grad()
        cost.backward()
        self.optimizer.step()

        self.awp_adversary.restore(awp)

        self.record_dict["CALoss"] = cost.item()
