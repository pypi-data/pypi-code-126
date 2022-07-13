import torch
import torch.nn as nn
from typing import Any, Optional, Sequence, Union, Dict

from ding.model.common import ReparameterizationHead, DiscreteHead, MultiHead, DuelingHead, RegressionHead
from .rnn_model import LSTMSeqModel, GRUSeqModel


class DiscretePGModel(nn.Module):

    def __init__(
            self,
            obs_shape: int,
            action_shape: int,
            hidden_dim: int,
            sequence_len: int,
            num_layers: int = 1,
            model_type: str = 'lstm',
            dueling: bool = True,
            head_hidden_size: Optional[int] = None,
            head_layer_num: int = 1,
            activation: Optional[nn.Module] = nn.ReLU(),
            norm_type: Optional[str] = None,
    ) -> None:
        super().__init__()
        self._obs_shape = obs_shape
        self._action_shape = action_shape
        self.input_layer = nn.Linear(self._obs_shape, hidden_dim * num_layers)
        assert model_type in ['lstm', 'gru'], model_type
        if model_type == 'lstm':
            self.encoder = LSTMSeqModel(hidden_dim, sequence_len, num_layers)
        elif model_type == 'gru':
            self.encoder = GRUSeqModel(hidden_dim, sequence_len, num_layers)

        head_hidden_size = hidden_dim

        if dueling:
            head_cls = DuelingHead
        else:
            head_cls = DiscreteHead
        multi_head = not isinstance(action_shape, int)
        if multi_head:
            self.head = MultiHead(
                head_cls,
                head_hidden_size,
                action_shape,
                layer_num=head_layer_num,
                activation=activation,
                norm_type=norm_type
            )
        else:
            self.head = head_cls(
                head_hidden_size, action_shape, head_layer_num, activation=activation, norm_type=norm_type
            )

    def forward(self, x: torch.Tensor) -> Dict:
        x = self.input_layer(x)
        x = x.unsqueeze(1)
        x, h = self.encoder(x, None)
        x = self.head(x)
        return x


class ContinuousPGModel(nn.Module):

    def __init__(
        self,
        obs_shape: int,
        action_shape: int,
        hidden_dim: int,
        sequence_len: int,
        action_space: str = 'regression',
        num_layers: int = 1,
        model_type: str = 'lstm',
        head_hidden_size: Optional[int] = None,
        head_layer_num: int = 1,
        activation: Optional[nn.Module] = nn.ReLU(),
        norm_type: Optional[str] = None,
        bound_type: Optional[str] = None,
    ) -> None:
        super().__init__()
        self._obs_shape = obs_shape
        self._action_shape = action_shape
        self._action_space = action_space
        self.input_layer = nn.Linear(self._obs_shape, hidden_dim * num_layers)
        assert model_type in ['lstm', 'gru'], model_type
        if model_type == 'lstm':
            self.encoder = LSTMSeqModel(hidden_dim, sequence_len, num_layers)
        elif model_type == 'gru':
            self.encoder = GRUSeqModel(hidden_dim, sequence_len, num_layers)
        assert self._action_space in ['regression', 'reparameterization']
        if self._action_space == 'regression':
            self.head = RegressionHead(
                head_hidden_size,
                action_shape,
                head_layer_num,
                final_tanh=True,
                activation=activation,
                norm_type=norm_type
            )
        elif self._action_space == 'reparameterization':
            self.head = ReparameterizationHead(
                head_hidden_size,
                action_shape,
                head_layer_num,
                sigma_type='conditioned',
                activation=activation,
                norm_type=norm_type,
                bound_type=bound_type
            )

    def forward(self, inputs: Union[torch.Tensor, Dict[str, torch.Tensor]]) -> Dict[str, torch.Tensor]:
        x = self.input_layer(inputs)
        x = x.unsqueeze(1)
        x, h = self.encoder(x, None)
        if self._action_space == 'regression':
            x = self.head(x)
            return {'action': x['pred']}
        elif self._action_space == 'reparameterization':
            x = self.head(x)
            return {'logit': [x['mu'], x['sigma']]}
