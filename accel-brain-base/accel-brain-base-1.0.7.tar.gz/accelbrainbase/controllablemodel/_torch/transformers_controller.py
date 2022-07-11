# -*- coding: utf-8 -*-
from accelbrainbase.controllable_model import ControllableModel
from accelbrainbase.iteratabledata._torch.dataset_iterator import DatasetIterator
import numpy as np
from logging import getLogger
import torch
from torch import nn
from torch.optim.adamw import AdamW


class TransformersController(ControllableModel):
    '''
    Transformer.

    References:
        - Bahdanau, D., Cho, K., & Bengio, Y. (2014). Neural machine translation by jointly learning to align and translate. arXiv preprint arXiv:1409.0473.
        - Floridi, L., & Chiriatti, M. (2020). GPT-3: Its nature, scope, limits, and consequences. Minds and Machines, 30(4), 681-694.
        - Miller, A., Fisch, A., Dodge, J., Karimi, A. H., Bordes, A., & Weston, J. (2016). Key-value memory networks for directly reading documents. arXiv preprint arXiv:1606.03126.
        - Radford, A., Narasimhan, K., Salimans, T., & Sutskever, I. (2018) Improving Language Understanding by Generative Pre-Training. OpenAI (URL: https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)
        - Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). Language models are unsupervised multitask learners. OpenAI blog, 1(8), 9.
        - Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., & Polosukhin, I. (2017). Attention is all you need. arXiv preprint arXiv:1706.03762.

    '''
    # `bool` that means initialization in this class will be deferred or not.
    __init_deferred_flag = False

    def __init__(
        self,
        model,
        optimizer_f=None,
        learning_rate=6e-06,
        weight_decay=0.01,
        ctx="cpu",
    ):
        '''
        Init.

        Args:
            learning_rate:                  `float` of learning rate.
            ctx:                            `mx.cpu()` or `mx.gpu()`.

        '''
        super(TransformersController, self).__init__()

        self.__learning_rate = learning_rate
        self.__weight_decay = weight_decay
        self.__ctx = ctx

        logger = getLogger("accelbrainbase")
        self.logger = logger

        self.model = model
        self.model = self.model.to(ctx)
        self.__ctx = ctx

        if optimizer_f is not None:
            self.optimizer = optimizer_f(
                self.model.parameters(),
                lr=self.__learning_rate,
                weight_decay=weight_decay
            )
        else:
            self.optimizer = AdamW(
                self.model.parameters(),
                lr=self.__learning_rate,
                weight_decay=weight_decay
            )

        self.epoch = 0

    def learn(self, iteratable_data):
        '''
        Learn samples drawn by `IteratableData.generate_learned_samples()`.

        Args:
            iteratable_data:     is-a `DatasetIterator`.
        '''
        if isinstance(iteratable_data, DatasetIterator) is False:
            raise TypeError("The type of `iteratable_data` must be `DatasetIterator`.")

        self.__loss_list = []
        learning_rate = self.__learning_rate

        try:
            epoch = self.epoch
            iter_n = 0
            for training_batch_tuple, test_batch_tuple in iteratable_data.generate_learned_samples():
                self.epoch = epoch
                self.optimizer.zero_grad()

                pred_obj = self.model(*training_batch_tuple)
                loss = pred_obj.loss
                loss.backward()
                self.optimizer.step()

                if (iter_n+1) % int(iteratable_data.iter_n / iteratable_data.epochs) == 0:
                    if torch.inference_mode():
                        test_pred_obj = self.model(*test_batch_tuple)
                        test_loss = test_pred_obj.loss

                    _loss = loss.to('cpu').detach().numpy().copy()
                    _test_loss = test_loss.to('cpu').detach().numpy().copy()

                    self.__loss_list.append((_loss, _test_loss))
                    self.logger.debug("Epochs: " + str(epoch + 1) + " Train loss: " + str(_loss) + " Test loss: " + str(_test_loss))
                    epoch += 1
                iter_n += 1

        except KeyboardInterrupt:
            self.logger.debug("Interrupt.")

        self.logger.debug("end. ")
        self.epoch = epoch

    def extract_learned_dict(self):
        '''
        Extract (pre-) learned parameters.

        Returns:
            `dict` of the parameters.
        '''
        params_dict = {}
        for k in self.model.state_dict().keys():
            params_dict.setdefault(k, self.model.state_dict()[k])

        return params_dict

    def save_parameters(self, filename):
        '''
        Save parameters to files.

        Args:
            filename:       File name.
        '''
        torch.save(
            {
                'model_state_dict': self.model.state_dict(),
                'optimizer_state_dict': self.optimizer.state_dict(),
                'epoch': self.epoch,
                'loss': self.loss_arr,
            }, 
            filename
        )

    def load_parameters(self, filename, ctx=None, strict=True):
        '''
        Load parameters to files.

        Args:
            filename:       File name.
            ctx:            Context-manager that changes the selected device.
            strict:         Whether to strictly enforce that the keys in state_dict match the keys returned by this module’s state_dict() function. Default: `True`.
        '''
        checkpoint = torch.load(filename)
        self.model.load_state_dict(checkpoint['model_state_dict'], strict=strict)
        self.optimizer.load_state_dict(
            checkpoint['optimizer_state_dict']
        )
        self.epoch = checkpoint['epoch']
        self.__loss_list = checkpoint['loss'].tolist()
        if ctx is not None:
            self.model.to(ctx)
            self.__ctx = ctx

    def set_readonly(self, value):
        ''' setter '''
        raise TypeError("This property must be read-only.")

    def get_init_deferred_flag(self):
        ''' getter for `bool` that means initialization in this class will be deferred or not.'''
        return self.__init_deferred_flag
    
    def set_init_deferred_flag(self, value):
        ''' setter for `bool` that means initialization in this class will be deferred or not.'''
        self.__init_deferred_flag = value

    init_deferred_flag = property(get_init_deferred_flag, set_init_deferred_flag)

    def get_loss_arr(self):
        ''' getter '''
        return np.array(self.__loss_list)
    
    def set_loss_arr(self, value):
        ''' setter '''
        raise TypeError("This property must be read-only.")
    
    loss_arr = property(get_loss_arr, set_loss_arr)
