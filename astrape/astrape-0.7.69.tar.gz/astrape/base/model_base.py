import torch
import torch.nn as nn
from torch.optim.lr_scheduler import OneCycleLR, StepLR, ExponentialLR, ConstantLR
from torch.optim.lr_scheduler import LinearLR,  ReduceLROnPlateau
import pytorch_lightning as pl
from astrape.utilities.utils import *
from astrape.exceptions.exceptions import *
from astrape.constants.astrape_constants import *
from typing import Union, List, Dict, Any, Optional, cast, Tuple
import math 
import numpy as np

from astrape.utilities.utils import rearrange_dims

applicable_val_metric_list = APPLICABLE_VAL_METRIC_LIST
applicable_optimizer_type_list = APPLICABLE_OPTIMIZER_TYPE_LIST


    
class BaseNet(pl.LightningModule):
    r"""BaseNet. Use this for models that don't deal with image data. 

        Attributes:
            
            dims (int or tuple of int): Dimension of data with # of samples removed.
            
            n_classes (int or None): Number of classes in classification task. None if it is a regression task.
            
            config (dict): Hyperparameter configurations.

            sample_weight (torch.Tensor or np.ndarray): Sample weights.

            **kwargs (Any): Attributes of LightningModule

        Note:

            BaseNet is the parent class for MLPs(MLP, ContractingMLP, CustomMLP). It is also
            compatible with other MLPs that are written in pytorch_lightning.

            When inheriting BaseNet, you only need to specify the structure of your MLP because 
            other magics are defined in BaseNet.  

            BaseNet can perform both classification and regression tasks. If you specify n_classes, 
            BaseNet will recognize the task as a classification problem. If n_classes is not passed
            as a parameter for BaseNet, it will understand that the task is a regression problem.
    """

    def __init__(
        self,
        dims : Union[int, Tuple[int]],
        n_classes : Optional[int],
        l1_strength : float = 0.0,
        sample_weight : Optional[Union["np.ndarray", "torch.Tensor"]] = None,
        **config : Any
    ) -> None:
        r"""
         Args: 
            
            dims (int or tuple of int): The dimension of the data. e.g., 4, (8,8,1)

            n_classes (int, optional): Number of classes (labels) in the classification task. Do not specify this argument (set is as None) when you are performing regression tasks.

            **config (Any) : Hyperparameters that can be shared among different models. e.g., optimizer_type, lr, weight_decay, batch_size, bn, dropout_p, etc.
        """
        super(BaseNet, self).__init__()
        if isinstance(dims, tuple):
            flattened = 1
            for dim in dims:
                flattened *= dim
            dims = flattened 

        self.dims = dims
        self.n_classes = n_classes if n_classes is not None else None 
        self.config = config
        self.sample_weight = sample_weight

        config.update({'l1_strength' : l1_strength})
        if 'scheduler' not in config.keys():
            config.update({"scheduler" : OneCycleLR})
        self.save_hyperparameters(*config)
        
    def get_scheduler(self, optimizer, scheduler_class, **kwargs):

        if scheduler_class is None:
            return ConstantLR(optimizer, factor=1)
        if scheduler_class == OneCycleLR:
            if 'max_lr' not in kwargs.keys():
                kwargs.update({'max_lr' : 0.1})
            if 'epochs' not in kwargs.keys() and 'total_steps' not in kwargs.keys() and 'steps_per_epoch' not in kwargs.keys():
                kwargs.update({'total_steps' : self.trainer.max_steps})
            

        elif scheduler_class == StepLR:
            if 'step_size' not in kwargs.keys():
                kwargs.update({'step_size': 30})
            if 'gamma' not in kwargs.keys():
                kwargs.update({'gamma' : 0.1}) 
        elif scheduler_class == ConstantLR:
            pass
        elif scheduler_class == LinearLR:
            pass
        elif scheduler_class == ExponentialLR:
            if 'gamma' not in kwargs.keys():
                kwargs.update({'gamma':0.5})
        elif scheduler_class == ReduceLROnPlateau:
            pass

        scheduler = scheduler_class(optimizer=optimizer, **kwargs)
        return scheduler

    @property
    def criterion(self):
        r"""Criterion for loss function.

        Returns:

            See astrape.utilities.utils for details.
        """
        if self.n_classes is None:
            if 'regression_metric' in self.config.keys():
                if self.config['regression_metric'] == "mse":
                    criterion = MSELoss()
                elif self.config['regression_metric'] == "r2":
                    criterion = R2Score()
                elif self.config['regression_metric'] == "rmse":
                    criterion = RMSELoss()
                else:
                    raise NotImplementedError("Only MSE loss, R2 score, and RMSE are supported in expytorch_lightning v 0.0.0.")
            else:
                criterion = RMSELoss()
        else:
            criterion = CELossMetrics(self.n_classes) if self.n_classes > 2 else BCELossMetrics()
        return criterion

    def training_step(self, train_batch, batch_idx):

        x_batch, y_batch = train_batch
        Yhat = self.forward(x_batch)
        y_batch = self.sample_weight * y_batch
        

        if self.n_classes is None: # regression
            loss = self.criterion(Yhat.squeeze(), y_batch)
            # L1 regularizer
            if self.hparams.l1_strength > 0:
                l1_reg = self.linear.weight.abs().sum()
                loss += self.hparams.l1_strength * l1_reg
            self.log('train/loss', loss)
            return {'loss' : loss}
        else: # classification
            if self.n_classes > 2:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.long())
            else:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.float())

            self.log('train/loss', loss)
            self.log('train/acc', acc)
            self.log('train/auc', auc)
            log_dict = {'train/loss' : loss, 'train/acc' : acc, 'train/auc' : auc}
            return {'loss' : loss, 'acc' : acc, 'auc' : auc, "progress_bar" : log_dict}
    
    def validation_step(self, val_batch, batch_idx):
        x_batch, y_batch = val_batch
        
        Yhat = self.forward(x_batch)
        if self.n_classes is None:
            loss = self.criterion(Yhat.squeeze(), y_batch)
            # L1 regularizer
            if self.hparams.l1_strength > 0:
                l1_reg = self.linear.weight.abs().sum()
                loss += self.hparams.l1_strength * l1_reg

            
            self.log('val/loss', loss)
            return {'loss' : loss}
        else:    
            loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch)
            self.log('val/loss', loss)
            self.log('val/acc', acc)
            self.log('val/auc', auc)
            return {'loss' : loss, 'acc' : acc, 'auc' : auc}


    def predict_step(self, pred_batch, batch_idx, dataloader_idx=0):
        x_batch, y_batch = pred_batch
        
        Yhat = self.forward(x_batch)
        if self.n_classes is None:
            loss = self.criterion(Yhat.squeeze(), y_batch)
            # L1 regularizer
            if self.hparams.l1_strength > 0:
                l1_reg = self.linear.weight.abs().sum()
                loss += self.hparams.l1_strength * l1_reg

            
            self.log('predict/loss', loss)
            return {'loss' : loss}
        else:    
            if self.n_classes > 2:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.LongTensor))
            else:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.FloatTensor))
            self.log('predict/loss', loss)
            self.log('predict/acc', acc)
            self.log('predict/auc', auc)
            return {'loss' : loss, 'acc' : acc, 'auc' : auc}

    def test_step(self, test_batch, batch_idx, data_loader_idx=0):
        x_batch, y_batch = test_batch
        
        Yhat = self.forward(x_batch)
        if self.n_classes is None:
            loss = self.criterion(Yhat.squeeze(), y_batch)
            # L1 regularizer
            if self.hparams.l1_strength > 0:
                l1_reg = self.linear.weight.abs().sum()
                loss += self.hparams.l1_strength * l1_reg

            
            self.log('test/loss', loss)
            return {'loss' : loss}
        else:    
            if self.n_classes > 2:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.LongTensor))
            else:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.FloatTensor))
            self.log('test/loss', loss)
            self.log('test/acc', acc)
            self.log('test/auc', auc)
            return {'loss' : loss, 'acc' : acc, 'auc' : auc}

    def on_after_batch_transfer(self, batch, dataloader_idx=0):
        # modify this part if you want to perform model reweigthing.
        self.sample_weight = torch.ones_like(batch[1]).type_as(batch[1])
        return batch
        
    def reset_weights(self, module):
        if isinstance(module, nn.Linear):
            module.reset_parameters()
            
    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            nn.init.kaiming_normal_(module.weight)
        elif isinstance(module, nn.BatchNorm1d):
            nn.init.constant_(module.weight, 1)
            nn.init.constant_(module.bias, 0)

    def configure_optimizers(self):

        #optimizer_type_check(applicable_optimizer_type_list, self.config.optimizer_type)
        if self.hparams.optimizer_type == "adam":
            optimizer = torch.optim.Adam(self.parameters(),
                                     lr=self.hparams.lr,
                                     weight_decay=self.hparams.weight_decay)
        elif self.hparams.optimizer_type == "sgd":
            optimizer = torch.optim.SGD(self.parameters(),
                                        lr=self.hparams.lr,
                                        momentum=self.hparams.momentum,
                                        weight_decay=self.hparams.weight_decay)

        if 'scheduler' not in self.config.keys():
            self.config.update({'scheduler' : None})

        scheduler_dict = {
            "scheduler" : self.get_scheduler(optimizer=optimizer, scheduler_class=self.config["scheduler"]),
            "interval" : "step"
        }
        return {"optimizer": optimizer, "lr_scheduler":scheduler_dict}


class ConvNet(pl.LightningModule):
    r"""ConvNet. Use this when using CNNs. 

    Note:

        ConvNet is the parent class for CNNs(VGG, UNet). It is also compatible with other CNNs
        that are written in pytorch_lightning. 

        When inheriting ConvNet, you only need to specify the structure of your MLP because 
        other magics are defined in ConvNet. 

        Currently in expytorch_lightning v. 0.0.0, ConvNet only supports basic classification
        tasks such as classification using CE loss or dice loss. Other operations will be 
        updated soon(Be tuned!).

    Attributes:

        model_type (LightningModule): The class of the model that you will use.

        n_classes (int, optional): Number of classes in the classification task. Leave it as None in regression tasks.

        sample_weight (torch.Tensor or np.ndarray): Sample weights.

        config (dict) : Hyperparameters that can be shared among different models. e.g., optimizer_type, lr, weight_decay, batch_size, bn, dropout_p, etc.
"""
    def __init__(
        self,
        n_classes : Optional[int] = None,
        sample_weight : Optional[Union["np.ndarray", "torch.Tensor"]] = None,
        dataformats : Optional[str] = "NCHW",
        **config : Any
    )->None:
        r"""
        Args: 

            n_classes (int, optional): Number of classes in the classification task. Leave it as None in regression tasks.
                Default: ``None``
            
            sample_weight (torch.Tensor or np.ndarray): Sample weights.
                Default: ``None``

            **config (Any) : Hyperparameters that can be shared among different models. e.g., optimizer_type, lr, weight_decay, batch_size, bn, dropout_p, etc.
        """
        super(ConvNet, self).__init__()
        
        self.n_classes = n_classes
        self.sample_weight = sample_weight
        self.dataformats = dataformats
        self.config = config
        self.save_hyperparameters(*config)

    def get_scheduler(self, optimizer, scheduler_class, **kwargs):

        if scheduler_class is None:
            return ConstantLR(optimizer, factor=1)
        if scheduler_class == OneCycleLR:
            if 'max_lr' not in kwargs.keys():
                kwargs.update({'max_lr' : 0.1})
            if 'epochs' not in kwargs.keys() and 'total_steps' not in kwargs.keys() and 'steps_per_epoch' not in kwargs.keys():
                kwargs.update({'total_steps' : self.trainer.max_steps})
            

        elif scheduler_class == StepLR:
            if 'step_size' not in kwargs.keys():
                kwargs.update({'step_size': 30})
            if 'gamma' not in kwargs.keys():
                kwargs.update({'gamma' : 0.1}) 
        elif scheduler_class == ConstantLR:
            pass
        elif scheduler_class == LinearLR:
            pass
        elif scheduler_class == ExponentialLR:
            if 'gamma' not in kwargs.keys():
                kwargs.update({'gamma':0.5})
        elif scheduler_class == ReduceLROnPlateau:
            pass

        scheduler = scheduler_class(optimizer=optimizer, **kwargs)
        return scheduler

    @property
    def criterion(self):   
        r"""Criterion for loss function.

        Returns:

            See astrape.utilities.utils for details.
        """
        if self.n_classes is None:
            if 'regression_metric' in self.config.keys():
                if self.config['regression_metric'] == "mse":
                    criterion = MSELoss()
                elif self.config['regression_metric'] == "r2":
                    criterion = R2Score()
                elif self.config['regression_metric'] == "rmse":
                    criterion = RMSELoss()
                else:
                    raise NotImplementedError("Only MSE loss, R2 score, and RMSE are supported in expytorch_lightning v 0.0.0.")
            else:
                criterion = MSELoss()
        else:
            criterion = CELossMetrics(self.n_classes) if self.n_classes > 2 else BCELossMetrics()
        return criterion

    def reshape_x(self, x_batch):
        dims = x_batch.shape[1:]
        
        if len(dims) == 1:
            raise ValueError(f"Wrong dimension {dims} for the input.")
        elif len(dims) == 2:
            height = dims[0]
            width = dims[1]
            x_batch = x_batch.reshape(-1, 1, int(height), int(width))
        elif len(dims) == 3:
            dims = rearrange_dims(dims=dims, in_format=self.dataformats, dataformats="NCHW")
            x_batch = x_batch.reshape(-1, *dims)                
        else:
            raise ValueError(f"Wrong dimension {dims} for the input.")

        return x_batch
    
    def on_after_batch_transfer(self, batch, dataloader_idx=0):
        # modify this part if you want to perform model reweigthing.
        self.sample_weight = torch.ones_like(batch[1]).type_as(batch[1])
        return batch
    
    def training_step(self, train_batch, batch_idx):
        x_batch, y_batch = train_batch
        #x_batch = self.reshape_x(x_batch).type_as(x_batch)
        y_batch = self.sample_weight * y_batch
        Yhat = self.forward(x_batch)
        
        if self.n_classes is None:
            loss = self.criterion(Yhat.squeeze(), y_batch)
            self.log('train/loss', loss)
            return {'loss' : loss}
        else:    
            if self.n_classes > 2:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.LongTensor))
            else:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.FloatTensor))
            self.log('train/loss', loss)
            self.log('train/acc', acc)
            self.log('train/auc', auc)
            return {'loss' : loss, 'acc' : acc, 'auc' : auc}

    def validation_step(self, val_batch, batch_idx):
        x_batch, y_batch = val_batch
        #x_batch = self.reshape_x(x_batch).type_as(x_batch)
        Yhat = self.forward(x_batch)
        
        if self.n_classes is None:
            loss = self.criterion(Yhat.squeeze(), y_batch)
            self.log('val/loss', loss)
            return {'loss' : loss}
        else:    
            if self.n_classes > 2:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.LongTensor))
            else:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.FloatTensor))
            self.log('val/loss', loss)
            self.log('val/acc', acc)
            self.log('val/auc', auc)
            return {'loss' : loss, 'acc' : acc, 'auc' : auc}

    def predict_step(self, pred_batch, batch_idx, dataloader_idx=0):
        x_batch, y_batch = pred_batch
        #x_batch = self.reshape_x(x_batch).type_as(x_batch)
        Yhat = self.forward(x_batch)
        
        if self.n_classes is None:
            loss = self.criterion(Yhat.squeeze(), y_batch)
            self.log('pred/loss', loss)
            return {'loss' : loss}
        else:    
            if self.n_classes > 2:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.LongTensor))
            else:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.FloatTensor))
            self.log('pred/loss', loss)
            self.log('pred/acc', acc)
            self.log('pred/auc', auc)
            return {'loss' : loss, 'acc' : acc, 'auc' : auc}

    def test_step(self, test_batch, batch_idx):
        x_batch, y_batch = test_batch
        #x_batch = self.reshape_x(x_batch).type_as(x_batch)
        Yhat = self.forward(x_batch)
        
        if self.n_classes is None:
            loss = self.criterion(Yhat.squeeze(), y_batch)
            self.log('test/loss', loss)
            return {'loss' : loss}
        else:    
            if self.n_classes > 2:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.LongTensor))
            else:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.FloatTensor))
            self.log('test/loss', loss)
            self.log('test/acc', acc)
            self.log('test/auc', auc)
            return {'loss' : loss, 'acc' : acc, 'auc' : auc}

    def reset_weights(self, module):
        if isinstance(module, nn.Linear):
            module.reset_parameters()
            
    def _init_weights(self, module) -> None:
        if isinstance(module, nn.Linear):
            nn.init.kaiming_normal_(module.weight)
        elif isinstance(module, nn.BatchNorm1d):
            nn.init.constant_(module.weight, 1)
            nn.init.constant_(module.bias, 0)
        elif isinstance(module, nn.Conv2d):
            nn.init.kaiming_normal_(module.weight, mode="fan_out", nonlinearity="relu")
            if module.bias is not None:
                nn.init.constant_(module.bias, 0)

    def configure_optimizers(self):

        if self.hparams.optimizer_type == "adam":
            optimizer = torch.optim.Adam(self.parameters(),
                                     lr=self.hparams.lr,
                                     weight_decay=self.hparams.weight_decay)
        elif self.hparams.optimizer_type == "sgd":
            optimizer = torch.optim.SGD(self.parameters(),
                                        lr=self.hparams.lr,
                                        momentum=self.hparams.momentum,
                                        weight_decay=self.hparams.weight_decay)

        if 'scheduler' not in self.config.keys():
            self.config.update({'scheduler' : None})

        scheduler_dict = {
            "scheduler" : self.get_scheduler(optimizer=optimizer, scheduler_class=self.config["scheduler"]),
            "interval" : "step"
        }
        return {"optimizer": optimizer, "lr_scheduler":scheduler_dict}


class SegNet(pl.LightningModule):
    r"""SegNet. Use this when using CNNs to perform Image Segmentation. 

    Note:

        SegNet is the parent class for CNNs(VGG). It is also compatible with other CNNs
        that are written in pytorch_lightning. 

    Attributes:

        model_type (LightningModule): The class of the model that you will use.

        n_classes (int, optional): Number of classes in the classification task. Leave it as None in regression tasks.

        sample_weight (torch.Tensor or np.ndarray): Sample weights.

        config (dict) : Hyperparameters that can be shared among different models. e.g., optimizer_type, lr, weight_decay, batch_size, bn, dropout_p, etc.
"""
    def __init__(
        self,
        n_classes : Optional[int] = None,
        sample_weight : Optional[Union["np.ndarray", "torch.Tensor"]] = None,
        dataformats : Optional[str] = "NCHW",
        **config : Any
    )->None:
        r"""
        Args: 

            n_classes (int, optional): Number of classes in the classification task. Leave it as None in regression tasks.
                Default: ``None``
            
            sample_weight (torch.Tensor or np.ndarray): Sample weights.
                Default: ``None``

            **config (Any) : Hyperparameters that can be shared among different models. e.g., optimizer_type, lr, weight_decay, batch_size, bn, dropout_p, etc.
        """
        super(SegNet, self).__init__()
        
        self.n_classes = n_classes
        self.sample_weight = sample_weight
        self.dataformats = dataformats
        self.config = config
        self.save_hyperparameters(*config)
        

    @property
    def criterion(self):   
        r"""Criterion for loss function.

        Returns:

            See astrape.utilities.utils for details.
        """
        if self.n_classes is None:
            raise AssertionError(f"Please pass the # of classes.")
        else:
            criterion = SegCELossMetrics(self.n_classes)
        return criterion

    def reshape_x(self, x_batch):
        dims = x_batch.shape[1:]
        
        if len(dims) == 2:
            height = dims[0]
            width = dims[1]
            x_batch = x_batch.reshape(-1, 1, int(height), int(width))
        elif len(dims) == 3:
            dims = rearrange_dims(dims=dims, in_format=self.dataformats, dataformats="NCHW")
            x_batch = x_batch.reshape(-1, *dims)                
        else:
            raise ValueError(f"Wrong dimension {dims} for the input.")

        return x_batch

    def on_before_batch_transfer(self, batch: Any, dataloader_idx=0):
        batch[0] = self.reshape_x(batch[0])
        return batch
    
    def on_after_batch_transfer(self, batch, dataloader_idx=0):
        # modify this part if you want to perform model reweigthing.
        self.sample_weight = torch.ones_like(batch[1]).type_as(batch[1])
        return batch
    
    def training_step(self, train_batch, batch_idx):
        x_batch, y_batch = train_batch
        #x_batch = self.reshape_x(x_batch)
        y_batch = self.sample_weight * y_batch

        Yhat = self.forward(x_batch)
        if self.n_classes is None:
            loss = self.criterion(Yhat.squeeze(), y_batch)
            self.log('train/loss', loss)
            return {'loss' : loss}
        else:    
            if self.n_classes > 2:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.LongTensor))
            else:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.FloatTensor))
            self.log('train/loss', loss)
            self.log('train/acc', acc)
            self.log('train/auc', auc)
            log_dict = {'train/loss' : loss, 'train/acc' : acc, 'train/auc' : auc}
            return {'loss' : loss, 'acc' : acc, 'auc' : auc, "progress_bar" : log_dict}


        
    def validation_step(self, val_batch, batch_idx):
        x_batch, y_batch = val_batch
        #x_batch = self.reshape_x(x_batch)
        Yhat = self.forward(x_batch)
        if self.n_classes is None:
            loss = self.criterion(Yhat.squeeze(), y_batch)
            self.log('val/loss', loss)
            return {'loss' : loss}
        else:    
            if self.n_classes > 2:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.LongTensor))
            else:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.FloatTensor))
            self.log('val/loss', loss)
            self.log('val/acc', acc)
            self.log('val/auc', auc)
            log_dict = {'val/loss' : loss, 'val/acc' : acc, 'val/auc' : auc}
            return {'loss' : loss, 'acc' : acc, 'auc' : auc}


    def predict_step(self, pred_batch, batch_idx, dataloader_idx=0):
        x_batch, y_batch = pred_batch
        #x_batch = self.reshape_x(x_batch)
        Yhat = self.forward(x_batch)
        if self.n_classes is None:
            loss = self.criterion(Yhat.squeeze(), y_batch)
            self.log('pred/loss', loss)
            return {'loss' : loss}
        else:    
            if self.n_classes > 2:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.LongTensor))
            else:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.FloatTensor))
            self.log('pred/loss', loss)
            self.log('pred/acc', acc)
            self.log('pred/auc', auc)
            return {'loss' : loss, 'acc' : acc, 'auc' : auc}

    def test_step(self, test_batch, batch_idx):
        x_batch, y_batch = test_batch
        #x_batch = self.reshape_x(x_batch)
        Yhat = self.forward(x_batch)
        if self.n_classes is None:
            loss = self.criterion(Yhat.squeeze(), y_batch)
            self.log('test/loss', loss)
            return {'loss' : loss}
        else:    
            if self.n_classes > 2:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.LongTensor))
            else:
                loss, acc, auc = self.criterion(Yhat.squeeze(), y_batch.type(torch.FloatTensor))
            self.log('test/loss', loss)
            self.log('test/acc', acc)
            self.log('test/auc', auc)
            return {'loss' : loss, 'acc' : acc, 'auc' : auc}

    def reset_weights(self, module):
        if isinstance(module, nn.Linear):
            module.reset_parameters()
            
    def _init_weights(self, module) -> None:
        if isinstance(module, nn.Linear):
            nn.init.kaiming_normal_(module.weight)
        elif isinstance(module, nn.BatchNorm1d):
            nn.init.constant_(module.weight, 1)
            nn.init.constant_(module.bias, 0)
        elif isinstance(module, nn.Conv2d):
            nn.init.kaiming_normal_(module.weight, mode="fan_out", nonlinearity="relu")
            if module.bias is not None:
                nn.init.constant_(module.bias, 0)
    def get_scheduler(self, optimizer, scheduler_class, **kwargs):

        if scheduler_class is None:
            return ConstantLR(optimizer, factor=1)
        if scheduler_class == OneCycleLR:
            if 'max_lr' not in kwargs.keys():
                kwargs.update({'max_lr' : 0.1})
            if 'epochs' not in kwargs.keys() and 'total_steps' not in kwargs.keys() and 'steps_per_epoch' not in kwargs.keys():
                kwargs.update({'total_steps' : self.trainer.max_steps})
            

        elif scheduler_class == StepLR:
            if 'step_size' not in kwargs.keys():
                kwargs.update({'step_size': 30})
            if 'gamma' not in kwargs.keys():
                kwargs.update({'gamma' : 0.1}) 
        elif scheduler_class == ConstantLR:
            pass
        elif scheduler_class == LinearLR:
            pass
        elif scheduler_class == ExponentialLR:
            if 'gamma' not in kwargs.keys():
                kwargs.update({'gamma':0.5})
        elif scheduler_class == ReduceLROnPlateau:
            pass

        scheduler = scheduler_class(optimizer=optimizer, **kwargs)
        return scheduler

    def configure_optimizers(self):

        if self.hparams.optimizer_type == "adam":
            optimizer = torch.optim.Adam(self.parameters(),
                                     lr=self.hparams.lr,
                                     weight_decay=self.hparams.weight_decay)
        elif self.hparams.optimizer_type == "sgd":
            optimizer = torch.optim.SGD(self.parameters(),
                                        lr=self.hparams.lr,
                                        momentum=self.hparams.momentum,
                                        weight_decay=self.hparams.weight_decay)

        if 'scheduler' not in self.config.keys():
            self.config.update({'scheduler' : None})

        scheduler_dict = {
            "scheduler" : self.get_scheduler(optimizer=optimizer, scheduler_class=self.config["scheduler"]),
            "interval" : "step"
        }
        return {"optimizer": optimizer, "lr_scheduler":scheduler_dict}
"""
class GenerativeNet(pl.LightningModule):
    def __init__(
        self,
        dims : Union[int, Tuple[int]],
        sample_weight : Optional[Union["np.ndarray", "torch.Tensor"]] = None,
        **config : Any
    )->None:
        super(GenerativeNet, self).__init__()

        self.dims = dims
        self.config = config
        self.sample_weight = sample_weight
        self.save_hyperparameters(*config)


    def on_after_batch_transfer(self, batch, dataloader_idx=0):
        # modify this part if you want to perform model reweigthing.
        self.sample_weight = torch.ones_like(batch[1]).type_as(batch[1])
        return batch
        
    def reset_weights(self, module):
        if isinstance(module, nn.Linear):
            module.reset_parameters()
            
    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            nn.init.kaiming_normal_(module.weight)
        elif isinstance(module, nn.BatchNorm1d):
            nn.init.constant_(module.weight, 1)
            nn.init.constant_(module.bias, 0)

    def configure_optimizers(self):

        #optimizer_type_check(applicable_optimizer_type_list, self.config.optimizer_type)
        if self.hparams.optimizer_type == "adam":
            optimizer = torch.optim.Adam(self.parameters(),
                                     lr=self.hparams.lr
                                     )
        elif self.hparams.optimizer_type == "sgd":
            optimizer = torch.optim.SGD(self.parameters(),
                                        lr=self.hparams.lr)
        
        return optimizer
"""