from ast import Assert
from math import log, sqrt
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
import matplotlib.pyplot as plt
from torchmetrics import AUROC
from torchmetrics.functional import dice_score
from typing import Union, List, Dict, Any, Optional, Tuple
from torch.nn import functional as F
from itertools import permutations

def column_or_1d(y):
    y = torch.as_tensor(y)
    shape = y.shape
    if (len(shape) == 1) or (len(shape) == 2 and shape[1] == 1):
        return torch.ravel(y)
    
    raise ValueError(f"y should be a 1d tensor, got a tensor of shape {shape} instead.")

class BCELossMetrics():
    def __init__(self):
        self.loss_function = nn.BCELoss()
    
    @staticmethod
    def accuracy(y_hat, labels):
        with torch.no_grad():
            y_tilde = (y_hat > 0.5).int()
            accuracy = (y_tilde == labels.int()).float().mean().item()
        return accuracy

    @staticmethod
    def auc(y_hat, labels):
        with torch.no_grad():
            auc_fn = AUROC()
            auc = auc_fn(y_hat, labels.int()).float()
        return auc

    def __call__(
        self, 
        y_hat : "torch.Tensor", 
        labels : "torch.Tensor"
    ):
        y_hat = y_hat.type_as(labels)
        loss = self.loss_function(y_hat, labels.reshape(-1)).squeeze()
        accuracy = self.accuracy(y_hat, labels)
        auc = self.auc(y_hat, labels.int())
        return loss, accuracy, auc

class CELossMetrics():
    def __init__(self, n_classes):
        self.loss_function = nn.CrossEntropyLoss()
        self.n_classes = n_classes
    @staticmethod
    def accuracy(y_hat, labels):
        with torch.no_grad():
            y_tilde = y_hat.argmax(axis=1)
            accuracy = (y_tilde == labels).float().mean().item()
        return accuracy

    
    def auc(self,y_hat, labels):
        with torch.no_grad():
            auc_fn = AUROC(num_classes=self.n_classes)
            auc = auc_fn(y_hat, labels.int()).float()
        return auc
    
    def __call__(
        self, 
        y_hat, 
        labels : "torch.Tensor"
    ):
        y_hat = y_hat.type_as(y_hat)
        loss = self.loss_function(y_hat.type_as(labels.float()), labels.reshape(-1).long()).squeeze()
        accuracy = self.accuracy(y_hat.type_as(labels.float()), labels)
        auc = self.auc(y_hat.type_as(labels.float()), labels)
        return loss, accuracy, auc

class SegCELossMetrics():
    def __init__(self, n_classes):
        self.n_classes = n_classes
    @staticmethod
    def accuracy(y_hat, labels):
        with torch.no_grad():
            y_tilde = y_hat.argmax(axis=1)
            accuracy = (y_tilde == labels.long()).float().mean().item()
        return accuracy

    
    def auc(self,y_hat, labels):
        with torch.no_grad():
            auc_fn = AUROC(num_classes=self.n_classes)
            auc = auc_fn(y_hat, labels.int()).float()
        return auc
    
    def __call__(
        self, 
        y_hat, 
        labels : "torch.Tensor"
    ):
        
        loss = F.cross_entropy(y_hat, labels.long(), ignore_index=250).squeeze()
        accuracy = self.accuracy(y_hat, labels)
        auc = self.auc(y_hat, labels)
        return loss, accuracy, auc

class MSELoss():
    def __init__(self):
        pass
    def __call__(
        self,
        y_hat : "torch.Tensor", 
        labels : "torch.Tensor"
    ):
        criterion = nn.MSELoss()
        loss = criterion(y_hat, labels.reshape(-1)).squeeze()
        return loss
class RMSELoss():
    def __init__(self):
        pass

    def __call__(
        self,
        y_hat : "torch.Tensor", 
        labels : "torch.Tensor"
    ):        
        criterion = nn.MSELoss()
        loss = torch.sqrt(criterion(y_hat, labels.reshape(-1))).squeeze()
        return loss

class R2Score():
    def __init__(self):
        pass
    def __call__(
        self, 
        y_hat, 
        labels : "torch.Tensor", 
        sample_weight : Optional["torch.Tensor"] = None,
        multioutput : Union[str, "torch.Tensor"] = "uniform_average"
    ):
        if len(y_hat) < 2:
            raise ValueError("R^2 score is not well-defined with less than 2 samples.")
        if sample_weight is not None:
            sample_weight = column_or_1d(sample_weight).type_as(labels)
            weight = torch.unsqueeze(sample_weight, dim=1).type_as(labels)
        else:
            weight = torch.ones_like(labels).unsqueeze(dim=1).type_as(labels)

        numerator = torch.sum(weight * (labels - y_hat)**2, dim=0).float()
        weighted_sum = (weight * labels.unsqueeze(dim=1)).squeeze()
        denominator = weight * torch.sum(labels - torch.mean(weighted_sum, dim=0)**2, dim=0).float()
        
        nonzero_denominator = denominator != 0
        nonzero_numerator = numerator != 0
        valid_score = nonzero_denominator & nonzero_numerator
        output_scores = torch.ones(size=labels.shape[1])
        output_scores[valid_score] = 1 - (numerator[valid_score]/denominator[valid_score])
        # arbitrary set to zero to avoid -inf scores, having a constant
        # labels are not interesting for scoring a regression anyway
        output_scores[nonzero_numerator & ~nonzero_denominator] = 0.0
        if isinstance(multioutput, str):
            if multioutput == "raw_values":
                # return scores individually
                return output_scores
            elif multioutput == "uniform_average":
                # passing None as weights results is uniform mean
                avg_weights = None
            elif multioutput == "variance_weighted":
                avg_weights = denominator.type_as(weight)
                # avoid fail on constant y or one-element arrays
                if not np.any(nonzero_denominator):
                    if not np.any(nonzero_numerator):
                        return torch.ones_like(labels).type_as(labels)
                    else:
                        return torch.zeros_like(labels).type_as(labels)
        else:
            avg_weights = multioutput

        output_weighted_sum = avg_weights * output_scores
        loss = torch.mean(output_weighted_sum)
        return loss


class CEDiceLossMetrics():
    def __init__(self, n_classes):
        self.n_classes = n_classes
    @staticmethod
    def accuracy(y_hat, labels):
        with torch.no_grad():
            y_tilde = y_hat.argmax(axis=1)
            accuracy = (y_tilde == labels).float().mean().item()
        return accuracy

    
    def auc(self,y_hat, labels):
        with torch.no_grad():
            auc_fn = AUROC(num_classes=self.n_classes)
            auc = auc_fn(y_hat, labels.int()).float()
        return auc

    def __call__(
        self, 
        y_hat, 
        labels : "torch.Tensor"
    ):
        
        loss = F.cross_entropy(y_hat, labels.long().squeeze(), ignore_index=250).squeeze()
        
        accuracy = self.accuracy(y_hat, labels)
        auc = self.auc(y_hat, labels)
        return loss, accuracy, auc

def dice_coeff(
    input: Tensor,
    target: Tensor,
    reduce_batch_first: bool = False, epsilon=1e-6
):
    # Average of Dice coefficient for all batches, or for a single mask
    if (input.size() == target.size()):
        raise AssertionError("Size mismatch between input and target.")
    if (input.dim() == 2 and reduce_batch_first):
        raise ValueError(f'Dice: asked to reduce batch but got tensor without batch dimension (shape {input.shape})')

    if input.dim() == 2 or reduce_batch_first:
        inter = torch.dot(input.reshape(-1), target.reshape(-1))
        sets_sum = torch.sum(input) + torch.sum(target)

        if sets_sum.item() == 0:
            sets_sum = 2 * inter

        return (2 * inter + epsilon) / (sets_sum + epsilon)

    else:
        # compute and average metric for each batch element
        dice = 0
        for i in range(input.shape[0]):
            dice += dice_coeff(input[i, ...], target[i, ...])

        return dice / input.shape[0]


def multiclass_dice_coeff(
    input: Tensor, 
    target: Tensor, 
    reduce_batch_first: bool = False, 
    epsilon=1e-6
):
    # Average of Dice coefficient for all classes
    if (input.size() == target.size()):
        raise AssertionError("Size mismatch between input and target.")
    dice = 0
    for channel in range(input.shape[1]):
        dice += dice_coeff(input[:, channel, ...], target[:, channel, ...], reduce_batch_first, epsilon)

    return dice / input.shape[1]


def dice_loss(
    input: Tensor, 
    target: Tensor, 
    multiclass: bool = False
):
    # Dice loss (objective to minimize) between 0 and 1
    if (input.size() == target.size()):
        raise AssertionError("Size mismatch between input and target.")
    fn = multiclass_dice_coeff if multiclass else dice_coeff

    return 1 - fn(input, target, reduce_batch_first=True)
    


def plot_img_and_mask(img, mask):
    classes = mask.shape[0] if len(mask.shape) > 2 else 1
    fig, ax = plt.subplots(1, classes + 1)
    ax[0].set_title('Input image')
    ax[0].imshow(img)
    if classes > 1:
        for i in range(classes):
            ax[i + 1].set_title(f'Output mask (class {i + 1})')
            ax[i + 1].imshow(mask[1, :, :])
    else:
        ax[1].set_title(f'Output mask')
        ax[1].imshow(mask)
    plt.xticks([]), plt.yticks([])
    plt.show()


def log2(x):
    return log(x) / log(2)
    
# H(labels) with base 2
def entropy(labels):
    results = unique_counts(labels)
    ent = 0.0
    for r in results.keys():
        p = float(results[r]) / len(labels)
        ent = ent - p * log2(p)
    return ent

def rearrange_dims(dims, in_format, dataformats="NCHW"):
    def find_mapping(in_format, dataformats):
        mappings = list(permutations([0,1,2]))
        c_to_i = {"C" : 0, "H" : 1, "W" : 2}
        in_format_array = []
        dataformat_array = []
        for c_in, c_out in zip(in_format, dataformats):
            if c_in != "N" and c_out != "N":
                in_format_array.append(int(c_to_i[c_in]))
                dataformat_array.append(int(c_to_i[c_out]))
        for mapping in mappings:
            mapped = list((in_format_array[mapping[0]], in_format_array[mapping[1]], in_format_array[mapping[2]]))
            if mapped == dataformat_array:
                return mapping

    if isinstance(dims, int):
            raise ValueError(f"Wrong dimension {dims} for an input.")
    elif len(dims) == 2:
        height = dims[0]
        width = dims[1]
        dims = (1, height, width)
    elif len(dims) == 3:
        mapping = find_mapping(in_format, dataformats)
        dims = tuple([dims[mapping[0]], dims[mapping[1]], dims[mapping[2]]])
        
    else:
        raise ValueError(f"Wrong dimension {dims} for an input.")
    return dims

def conv_dim(
    in_dim, out_channels,
    padding, dilation, kernel_size, stride,
    dataformat="NCHW"
):

    if isinstance(padding, int):
        padding = (padding, padding)
    if isinstance(dilation, int):
        dilation = (dilation, dilation)
    if isinstance(kernel_size, int):
        kernel_size = (kernel_size, kernel_size)
    if isinstance(stride, int):
        stride = (stride, stride)
    
    c_in, h_in, w_in, c_out, h_out, w_out = None

    mapping_in = {"C":c_in, "H":h_in, "W":w_in}
    for idx, c in enumerate(dataformat):
        if c != "N":
            mapping_in[c] = in_dim[idx]
    
    h_num = h_in + 2 * padding[0] - dilation[0]*(kernel_size[0]-1)-1
    h_den = stride[0]
    h_out = int(h_num/h_den+1)

    w_num = w_in + 2 * padding[1] - dilation[1]*(kernel_size[1]-1)-1
    w_den = stride[1]
    w_out = int(w_num/w_den+1)

    c_out = out_channels
    
    out_dim = None 
    if dataformat == "NCHW":
        out_dim = (c_out, h_out, w_out)
    elif dataformat == "NCWH":
        out_dim = (c_out, w_out, h_out)
    elif dataformat == "NHWC":
        out_dim = (h_out, w_out, c_out)
    elif dataformat == "NHCW":
        out_dim = (h_out, c_out, w_out)
    elif dataformat == "NWHC":
        out_dim = (w_out, h_out, c_out)
    elif dataformat == "NWCH":
        out_dim = (w_out, c_out, h_out)
    else:
        raise ValueError(f"Wrong type of dataformat {dataformat}. It should start with 'N' and be followed by a permutation of 'HWC'.")
    
    return out_dim 