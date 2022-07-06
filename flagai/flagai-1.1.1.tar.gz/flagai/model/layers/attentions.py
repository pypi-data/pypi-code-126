# Copyright © 2022 BAAI. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License")
# coding=utf-8
# Copyright (c) 2019, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""attentions."""
import os
import math
import torch
try:
    import deepspeed
except:
    pass
from torch import nn
import torch.nn.init as init
import torch.nn.functional as F
from torch.nn import Linear
from flagai.model.layers.layer_norm import BertLayerNorm
from flagai.model.layers.layer_norm import T5LayerNorm
from flagai.model.layers.feedforward import ColumnParallelLinear, RowParallelLinear
from flagai.model.utils import normal_init_method
from flagai.model.utils import divide
from flagai.model.utils import ensure_divisibility
from flagai.model.utils import split_tensor_along_last_dim

if os.getenv('ENV_TYPE') == 'deepspeed+mpu':
    from flagai.mpu import get_model_parallel_world_size
    from flagai.mpu import gather_from_model_parallel_region
    from flagai.mpu import get_cuda_rng_tracker


class GPT2Attention(nn.Module):

    def __init__(self,
                 nx,
                 n_ctx,
                 config,
                 scale=False,
                 init_method=init.xavier_normal_):
        super().__init__()

        n_state = nx  # in Attention: n_state=768 (nx=n_embd)
        # [switch nx => n_state from Block to Attention to keep identical to TF implem]
        assert n_state % config.n_head == 0
        # self.register_buffer(
        #     "bias",
        #     torch.tril(torch.ones((n_ctx, n_ctx),
        #                           dtype=torch.uint8)).view(1, 1, n_ctx, n_ctx))
        # self.register_buffer("masked_bias", torch.tensor(-1e4))
        self.n_head = config.n_head
        self.split_size = n_state
        self.scale = scale
        if os.getenv("ENV_TYPE") == 'deepspeed+mpu':
            world_size = get_model_parallel_world_size()
            self.split_size = divide(n_state, world_size)

            self.hidden_size_per_partition = divide(nx, world_size)
            self.hidden_size_per_attention_head = divide(nx, self.n_head)
            self.num_attention_heads_per_partition = divide(
                self.n_head, world_size)

            self.c_attn = ColumnParallelLinear(nx,
                                               3 * n_state,
                                               stride=3,
                                               gather_output=False,
                                               init_method=init_method)

            self.c_proj = RowParallelLinear(input_size=nx,
                                            output_size=n_state,
                                            bias=True,
                                            input_is_parallel=True,
                                            stride=1,
                                            init_method=init_method)
        else:
            self.c_attn = nn.Linear(nx, 3 * n_state)
            self.c_proj = nn.Linear(nx, n_state)
        self.attn_dropout = nn.Dropout(config.attn_pdrop)
        self.resid_dropout = nn.Dropout(config.resid_pdrop)
        self.pruned_heads = set()

    def _attn(self,
              q,
              k,
              v,
              attention_mask=None,
              head_mask=None,
              ):
        w = torch.matmul(q, k.transpose(-1, -2))

        if self.scale:
            w = w / (float(v.size(-1))**0.5)

        # if not self.is_cross_attention:
        # if only "normal" attention layer implements causal mask
        # mask = self.bias[:, :, ns - nd:ns, :ns]
        # w = torch.where(mask.bool(), w, self.masked_bias.to(w.dtype))

        if attention_mask is not None:
            # Apply the attention mask
            w = w + attention_mask

        w = nn.Softmax(dim=-1)(w)
        w = self.attn_dropout(w)

        # Mask heads if we want to
        if head_mask is not None:
            w = w * head_mask
        w = w.to(v.dtype)  #  fp16
        outputs = torch.matmul(w, v)

        return outputs, w

    def merge_heads(self, x):
        x = x.permute(0, 2, 1, 3).contiguous()
        new_x_shape = x.size()[:-2] + (x.size(-2) * x.size(-1), )
        return x.view(*new_x_shape)  # in Tensorflow implem: fct merge_states

    def split_heads(self, x):
        if os.getenv('ENV_TYPE') == 'deepspeed+mpu':
            new_x_shape = x.size()[:-1] + (
                self.num_attention_heads_per_partition,
                x.size(-1) // self.num_attention_heads_per_partition)
        else:
            new_x_shape = x.size()[:-1] + (self.n_head,
                                           x.size(-1) // self.n_head)
        x = x.view(*new_x_shape)  # in Tensorflow implem: fct split_states
        # if k:
        #     return x.permute(0, 2, 3,
        #                      1)  # (batch, head, head_features, seq_length)
        # else:
        return x.permute(0, 2, 1,
                         3)  # (batch, head, seq_length, head_features)

    def forward(
        self,
        hidden_states,
        layer_past=None,
        attention_mask=None,
        head_mask=None,
        use_cache=False,
        output_attentions=False,
    ):
        query, key, value = self.c_attn(hidden_states).split(self.split_size,
                                                             dim=2)

        query = self.split_heads(query)
        key = self.split_heads(key)
        value = self.split_heads(value)

        if layer_past is not None:
            past_key, past_value = layer_past
            key = torch.cat((past_key, key), dim=-2)
            value = torch.cat((past_value, value), dim=-2)

        if use_cache is True:
            present = (key, value
                       )
        else:
            present = None

        attn_outputs = self._attn(query, key, value, attention_mask, head_mask,
                                  )
        a = attn_outputs[0]
        if layer_past is not None:
            a = a[:, :, -1:]
        a = self.merge_heads(a)
        a = self.c_proj(a)
        a = self.resid_dropout(a)
        outputs = (a, present)
        if output_attentions:
            outputs += (attn_outputs[1])
        return outputs  # a, present, (attentions)


class T5Attention(nn.Module):

    def __init__(self, config, has_relative_attention_bias=False):
        super().__init__()
        self.is_decoder = config['is_decoder']
        self.has_relative_attention_bias = has_relative_attention_bias
        self.relative_attention_num_buckets = config[
            'relative_attention_num_buckets']
        self.d_model = config['d_model']
        self.key_value_proj_dim = config['d_kv']
        self.n_heads = config['num_heads']
        self.dropout = config['dropout_rate']
        self.inner_dim = self.n_heads * self.key_value_proj_dim

        if os.getenv('ENV_TYPE') == 'deepspeed+mpu':
            # Mesh TensorFlow initialization to avoid scaling before softmax
            self.q = ColumnParallelLinear(self.d_model,
                                          self.inner_dim,
                                          stride=1,
                                          gather_output=True,
                                          bias=False)
            self.k = ColumnParallelLinear(self.d_model,
                                          self.inner_dim,
                                          stride=1,
                                          gather_output=True,
                                          bias=False)
            self.v = ColumnParallelLinear(self.d_model,
                                          self.inner_dim,
                                          stride=1,
                                          gather_output=True,
                                          bias=False)
            self.o = RowParallelLinear(self.inner_dim,
                                       self.d_model,
                                       bias=False,
                                       input_is_parallel=False)
        else:
            self.q = nn.Linear(self.d_model, self.inner_dim, bias=False)
            self.k = nn.Linear(self.d_model, self.inner_dim, bias=False)
            self.v = nn.Linear(self.d_model, self.inner_dim, bias=False)
            self.o = nn.Linear(self.inner_dim, self.d_model, bias=False)

        if self.has_relative_attention_bias:
            self.relative_attention_bias = nn.Embedding(
                self.relative_attention_num_buckets, self.n_heads)

    @staticmethod
    def _relative_position_bucket(relative_position,
                                  bidirectional=True,
                                  num_buckets=32,
                                  max_distance=128):
        """
        Adapted from Mesh Tensorflow:
        https://github.com/tensorflow/mesh/blob/0cb87fe07da627bf0b7e60475d59f95ed6b5be3d/mesh_tensorflow/transformer/transformer_layers.py#L593
        Translate relative position to a bucket number for relative attention. The relative position is defined as
        memory_position - query_position, i.e. the distance in tokens from the attending position to the attended-to
        position. If bidirectional=False, then positive relative positions are invalid. We use smaller buckets for
        small absolute relative_position and larger buckets for larger absolute relative_positions. All relative
        positions >=max_distance map to the same bucket. All relative positions <=-max_distance map to the same bucket.
        This should allow for more graceful generalization to longer sequences than the model has been trained on
        Args:
            relative_position: an int32 Tensor
            bidirectional: a boolean - whether the attention is bidirectional
            num_buckets: an integer
            max_distance: an integer
        Returns:
            a Tensor with the same shape as relative_position, containing int32 values in the range [0, num_buckets)
        """
        relative_buckets = 0
        if bidirectional:
            num_buckets //= 2
            relative_buckets += (relative_position > 0).to(
                torch.long) * num_buckets
            relative_position = torch.abs(relative_position)
        else:
            relative_position = -torch.min(relative_position,
                                           torch.zeros_like(relative_position))
        # now relative_position is in the range [0, inf)

        # half of the buckets are for exact increments in positions
        max_exact = num_buckets // 2
        is_small = relative_position < max_exact

        # The other half of the buckets are for logarithmically bigger bins in positions up to max_distance
        relative_postion_if_large = max_exact + (
            torch.log(relative_position.float() / max_exact) /
            math.log(max_distance / max_exact) *
            (num_buckets - max_exact)).to(torch.long)
        relative_postion_if_large = torch.min(
            relative_postion_if_large,
            torch.full_like(relative_postion_if_large, num_buckets - 1))

        relative_buckets += torch.where(is_small, relative_position,
                                        relative_postion_if_large)
        return relative_buckets

    def compute_bias(self, query_length, key_length):
        """ Compute binned relative position bias """
        context_position = torch.arange(query_length, dtype=torch.long)[:,
                                                                        None]
        memory_position = torch.arange(key_length, dtype=torch.long)[None, :]
        relative_position = memory_position - context_position  # shape (query_length, key_length)
        relative_position_bucket = self._relative_position_bucket(
            relative_position,  # shape (query_length, key_length)
            bidirectional=(not self.is_decoder),
            num_buckets=self.relative_attention_num_buckets,
        )
        relative_position_bucket = relative_position_bucket.to(
            self.relative_attention_bias.weight.device)
        values = self.relative_attention_bias(
            relative_position_bucket
        )  # shape (query_length, key_length, num_heads)
        values = values.permute([2, 0, 1]).unsqueeze(
            0)  # shape (1, num_heads, query_length, key_length)
        return values

    def forward(
        self,
        hidden_states,
        mask=None,
        key_value_states=None,
        position_bias=None,
        past_key_value=None,
        layer_head_mask=None,
        query_length=None,
        use_cache=False,
        output_attentions=False,
    ):
        """
        Self-attention (if key_value_states is None) or attention over source sentence (provided by key_value_states).
        """
        # Input is (batch_size, seq_length, dim)
        # Mask is (batch_size, key_length) (non-causal) or (batch_size, key_length, key_length)
        # past_key_value[0] is (batch_size, n_heads, q_len - 1, dim_per_head)
        batch_size, seq_length = hidden_states.shape[:2]

        real_seq_length = seq_length

        if past_key_value is not None:
            assert (
                len(past_key_value) == 2
            ), "past_key_value should have 2 past states: keys and values. Got {} past states".format(
                len(past_key_value))
            real_seq_length += past_key_value[0].shape[
                2] if query_length is None else query_length

        key_length = real_seq_length if key_value_states is None else key_value_states.shape[
            1]

        def shape(states):
            """  projection """
            return states.view(batch_size, -1, self.n_heads,
                               self.key_value_proj_dim).transpose(1, 2)

        def unshape(states):
            """  reshape """
            return states.transpose(1, 2).contiguous().view(
                batch_size, -1, self.inner_dim)

        def project(hidden_states, proj_layer, key_value_states,
                    past_key_value):
            """ projects hidden states correctly to key/query states """
            if key_value_states is None:
                # self-attn
                # (batch_size, n_heads, seq_length, dim_per_head)
                hidden_states = shape(proj_layer(hidden_states))
            elif past_key_value is None:
                # cross-attn
                # (batch_size, n_heads, seq_length, dim_per_head)
                hidden_states = shape(proj_layer(key_value_states))

            if past_key_value is not None:
                if key_value_states is None:
                    # self-attn
                    # (batch_size, n_heads, key_length, dim_per_head)
                    hidden_states = torch.cat([past_key_value, hidden_states],
                                              dim=2)
                else:
                    # cross-attn
                    hidden_states = past_key_value
            return hidden_states

        ''' different from glm '''
        # get query states
        query_states = shape(self.q(
            hidden_states))  # (batch_size, n_heads, seq_length, dim_per_head)

        # get key/value states
        key_states = project(
            hidden_states, self.k, key_value_states,
            past_key_value[0] if past_key_value is not None else None)
        value_states = project(
            hidden_states, self.v, key_value_states,
            past_key_value[1] if past_key_value is not None else None)

        # compute scores
        scores = torch.matmul(
            query_states, key_states.transpose(3, 2)
        )  # equivalent of torch.einsum("bnqd,bnkd->bnqk", query_states, key_states), compatible with onnx op>9

        if position_bias is None:
            if not self.has_relative_attention_bias:
                position_bias = torch.zeros(
                    (1, self.n_heads, real_seq_length, key_length),
                    device=scores.device,
                    dtype=scores.dtype)
            else:
                position_bias = self.compute_bias(real_seq_length, key_length)

            # if key and values are already calculated
            # we want only the last query position bias
            if past_key_value is not None:
                position_bias = position_bias[:, :, -seq_length:, :]

            if mask is not None:
                position_bias = position_bias + mask  # (batch_size, n_heads, seq_length, key_length)
        scores += position_bias
        attn_weights = F.softmax(scores.float(), dim=-1).type_as(
            scores)  # (batch_size, n_heads, seq_length, key_length)
        attn_weights = F.dropout(
            attn_weights, p=self.dropout, training=self.training
        )  # (batch_size, n_heads, seq_length, key_length)

        # Mask heads if we want to
        if layer_head_mask is not None:
            attn_weights = attn_weights * layer_head_mask

        attn_output = unshape(torch.matmul(
            attn_weights, value_states))  # (batch_size, seq_length, dim)
        attn_output = self.o(attn_output)

        present_key_value_state = (key_states,
                                   value_states) if (self.is_decoder
                                                     and use_cache) else None
        outputs = (attn_output, ) + (present_key_value_state, ) + (
            position_bias, )

        if output_attentions:
            outputs = outputs + (attn_weights, )
        return outputs


class T5LayerSelfAttention(nn.Module):

    def __init__(self, config, has_relative_attention_bias=False):
        super().__init__()
        self.SelfAttention = T5Attention(
            config, has_relative_attention_bias=has_relative_attention_bias)
        self.layer_norm = T5LayerNorm(config['d_model'],
                                      eps=config['layer_norm_epsilon'])
        self.dropout = nn.Dropout(config['dropout_rate'])

    def forward(
        self,
        hidden_states,
        attention_mask=None,
        position_bias=None,
        layer_head_mask=None,
        past_key_value=None,
        use_cache=False,
        output_attentions=False,
    ):
        normed_hidden_states = self.layer_norm(hidden_states)
        attention_output = self.SelfAttention(
            normed_hidden_states,
            mask=attention_mask,
            position_bias=position_bias,
            layer_head_mask=layer_head_mask,
            past_key_value=past_key_value,
            use_cache=use_cache,
            output_attentions=output_attentions,
        )
        hidden_states = hidden_states + self.dropout(attention_output[0])
        outputs = (hidden_states,
                   ) + attention_output[1:]  # add attentions if we output them
        return outputs


class T5LayerCrossAttention(nn.Module):

    def __init__(self, config):
        super().__init__()
        self.EncDecAttention = T5Attention(config,
                                           has_relative_attention_bias=False)
        self.layer_norm = T5LayerNorm(config['d_model'],
                                      eps=config['layer_norm_epsilon'])
        self.dropout = nn.Dropout(config['dropout_rate'])

    def forward(
        self,
        hidden_states,
        key_value_states,
        attention_mask=None,
        position_bias=None,
        layer_head_mask=None,
        past_key_value=None,
        use_cache=False,
        query_length=None,
        output_attentions=False,
    ):
        normed_hidden_states = self.layer_norm(hidden_states)
        attention_output = self.EncDecAttention(
            normed_hidden_states,
            mask=attention_mask,
            key_value_states=key_value_states,
            position_bias=position_bias,
            layer_head_mask=layer_head_mask,
            past_key_value=past_key_value,
            use_cache=use_cache,
            query_length=query_length,
            output_attentions=output_attentions,
        )
        layer_output = hidden_states + self.dropout(attention_output[0])
        outputs = (layer_output,
                   ) + attention_output[1:]  # add attentions if we output them
        return outputs


class ParallelCrossAttention(torch.nn.Module):
    """Parallel cross-attention layer for Transformer"""

    def __init__(self,
                 hidden_size,
                 num_attention_heads,
                 attention_dropout_prob,
                 output_dropout_prob,
                 init_method,
                 output_layer_init_method=None):
        super(ParallelCrossAttention, self).__init__()
        # Set output layer initialization if not provided.
        if output_layer_init_method is None:
            output_layer_init_method = init_method
        # Per attention head and per partition values.
        if os.getenv("ENV_TYPE") == 'deepspeed+mpu':
            world_size = get_model_parallel_world_size()
            self.hidden_size_per_partition = divide(hidden_size, world_size)
            self.hidden_size_per_attention_head = divide(
                hidden_size, num_attention_heads)
            self.num_attention_heads_per_partition = divide(
                num_attention_heads, world_size)
            # Strided linear layer.
            self.query = ColumnParallelLinear(hidden_size,
                                              hidden_size,
                                              gather_output=False,
                                              init_method=init_method)
            self.key_value = ColumnParallelLinear(hidden_size,
                                                  2 * hidden_size,
                                                  stride=2,
                                                  gather_output=False,
                                                  init_method=init_method)
            # Output.
            self.dense = RowParallelLinear(
                hidden_size,
                hidden_size,
                input_is_parallel=True,
                init_method=output_layer_init_method)

        else:
            self.hidden_size_per_partition = hidden_size
            self.hidden_size_per_attention_head = divide(
                hidden_size, num_attention_heads)

            self.num_attention_heads_per_partition = num_attention_heads
            # Strided linear layer.
            self.query = Linear(hidden_size, hidden_size)

            self.key_value = Linear(hidden_size, 2 * hidden_size)
            self.dense = Linear(hidden_size, hidden_size)
        # Dropout. Note that for a single iteration, this layer will generate
        # different outputs on different number of parallel partitions but
        # on average it should not be partition dependent.
        self.attention_dropout = torch.nn.Dropout(attention_dropout_prob)

        self.output_dropout = torch.nn.Dropout(output_dropout_prob)

    def _transpose_for_scores(self, tensor):
        """Transpose a 3D tensor [b, s, np*hn] into a 4D tensor with
        size [b, np, s, hn].
        """
        new_tensor_shape = tensor.size()[:-1] + \
                           (self.num_attention_heads_per_partition,
                            self.hidden_size_per_attention_head)
        tensor = tensor.view(*new_tensor_shape)
        return tensor.permute(0, 2, 1, 3)

    def forward(self, hidden_states, encoder_states, cross_mask):
        # hidden_states: [b, s, h]
        # ltor_mask: [1, 1, s, s]

        # Attention heads. [b, s, hp]
        mixed_query_layer = self.query(hidden_states)
        mixed_x_layer = self.key_value(encoder_states)
        (mixed_key_layer,
         mixed_value_layer) = split_tensor_along_last_dim(mixed_x_layer, 2)

        # Reshape and transpose [b, np, s, hn]
        query_layer = self._transpose_for_scores(mixed_query_layer)
        key_layer = self._transpose_for_scores(mixed_key_layer)
        value_layer = self._transpose_for_scores(mixed_value_layer)
        # Raw attention scores. [b, np, s, s]
        attention_scores = torch.matmul(query_layer,
                                        key_layer.transpose(-1, -2))
        attention_scores = attention_scores / math.sqrt(
            self.hidden_size_per_attention_head)
        if cross_mask is not None:
            # Apply the left to right attention mask.
            attention_scores = torch.mul(attention_scores, cross_mask) - \
                               10000.0 * (1.0 - cross_mask)

        # Attention probabilities. [b, np, s, s]
        attention_probs = torch.nn.Softmax(dim=-1)(attention_scores)
        # This is actually dropping out entire tokens to attend to, which might
        # seem a bit unusual, but is taken from the original Transformer paper.
        with get_cuda_rng_tracker().fork():
            attention_probs = self.attention_dropout(attention_probs)

        # Context layer.
        # [b, np, s, hn]
        context_layer = torch.matmul(attention_probs, value_layer)
        # [b, s, np, hn]
        context_layer = context_layer.permute(0, 2, 1, 3).contiguous()
        new_context_layer_shape = context_layer.size()[:-2] + \
                                  (self.hidden_size_per_partition,)
        # [b, s, hp]
        context_layer = context_layer.view(*new_context_layer_shape)

        # Output. [b, s, h]
        output = self.dense(context_layer)
        output = self.output_dropout(output)

        return output


class ParallelSelfAttention(torch.nn.Module):
    """Parallel self-attention layer for GPT2.

    Self-attention layer takes input with size [b, s, h] where b is
    the batch size, s is the sequence lenght, and h is the hidden size
    and creates output of the same size.
    Arguments:
        hidden_size: total hidden size of the layer (h).
        num_attention_heads: number of attention heads (n). Note that we
                             require n to be divisible by number of GPUs
                             used to parallelize the model. Also, we
                             require hidden size to be divisible by n.
        attention_dropout_prob: dropout probability for the attention scores.
        init_method: weight initialization.
        output_layer_init_method: output layer initialization. If None, use
                                  `init_method`.
    We use the following notation:
        h: hidden_size
        n: num_attention_heads
        p: number of partitions
        np: n/p
        hp: h/p
        hn: h/n
        b: batch size
        s: sequence length
    """

    def __init__(self,
                 hidden_size,
                 num_attention_heads,
                 attention_dropout_prob,
                 output_dropout_prob,
                 init_method,
                 output_layer_init_method=None,
                 relative_encoding=False,
                 performer=False,
                 attention_scale=1.0):
        super(ParallelSelfAttention, self).__init__()
        self.performer = performer
        # Set output layer initialization if not provided.
        if output_layer_init_method is None:
            output_layer_init_method = init_method
        # Per attention head and per partition values.
        if os.getenv('ENV_TYPE') == 'deepspeed+mpu':
            world_size = get_model_parallel_world_size()
            self.hidden_size_per_partition = divide(hidden_size, world_size)
            self.hidden_size_per_attention_head = divide(
                hidden_size, num_attention_heads)
            self.num_attention_heads_per_partition = divide(
                num_attention_heads, world_size)
            self.relative_encoding = relative_encoding
            self.attention_scale = attention_scale
            # Strided linear layer.
            # get q, k, v
            self.query_key_value = ColumnParallelLinear(
                hidden_size,
                3 * hidden_size,
                stride=3,
                gather_output=False,
                init_method=init_method)
            if relative_encoding:
                self.relative = ColumnParallelLinear(hidden_size,
                                                     hidden_size,
                                                     gather_output=False,
                                                     init_method=init_method)
            # Dropout. Note that for a single iteration, this layer will generate
            # different outputs on different number of parallel partitions but
            # on average it should not be partition dependent.
            self.attention_dropout = torch.nn.Dropout(attention_dropout_prob)

            # Output.
            self.dense = RowParallelLinear(
                hidden_size,
                hidden_size,
                input_is_parallel=True,
                init_method=output_layer_init_method)
        else:
            self.hidden_size_per_partition = hidden_size
            self.hidden_size_per_attention_head = divide(
                hidden_size, num_attention_heads)

            self.num_attention_heads_per_partition = num_attention_heads
            self.relative_encoding = relative_encoding
            self.attention_scale = attention_scale
            # Strided linear layer.
            self.query_key_value = Linear(hidden_size, 3 * hidden_size)

            if relative_encoding:
                self.relative = Linear(hidden_size, hidden_size)
            # Dropout. Note that for a single iteration, this layer will generate
            # different outputs on different number of parallel partitions but
            # on average it should not be partition dependent.
            self.attention_dropout = torch.nn.Dropout(attention_dropout_prob)

            # Output.
            self.dense = Linear(hidden_size, hidden_size)
        self.output_dropout = torch.nn.Dropout(output_dropout_prob)
        if 'deepspeed' in os.getenv('env_type', ''):
            if deepspeed.checkpointing.is_configured():
                global get_cuda_rng_tracker, checkpoint
                get_cuda_rng_tracker = deepspeed.checkpointing.get_cuda_rng_tracker
                checkpoint = deepspeed.checkpointing.checkpoint

    def _transpose_for_scores(self, tensor):
        """Transpose a 3D tensor [b, s, np*hn] into a 4D tensor with
        size [b, np, s, hn].
        """
        new_tensor_shape = tensor.size()[:-1] + \
                           (self.num_attention_heads_per_partition,
                            self.hidden_size_per_attention_head)
        tensor = tensor.view(*new_tensor_shape)
        return tensor.permute(0, 2, 1, 3)

    @staticmethod
    def _rel_shift(x, zero_triu=False):
        # ql x kl x bsz x h
        # bsz x h x ql x kl
        zero_pad = torch.zeros((*x.size()[:-2], x.size(-2), 1),
                               device=x.device,
                               dtype=x.dtype)
        x_padded = torch.cat([zero_pad, x], dim=-1)

        x_padded = x_padded.view(*x.size()[:-2], x.size(-1) + 1, x.size(-2))

        x = x_padded[:, :, 1:].view_as(x)

        if zero_triu:
            ones = torch.ones((x.size(0), x.size(1)))
            x = x * torch.tril(ones, x.size(1) - x.size(0))[:, :, None, None]

        return x

    def forward(self,
                hidden_states,
                ltor_mask,
                position_embeddings=None,
                r_w_bias=None,
                r_r_bias=None,
                mem=None):
        # hidden_states: [b, s, h]
        # ltor_mask: [1, 1, s, s]

        # Attention heads. [b, s, hp]
        query_length = hidden_states.size(1)

        if mem is None:  # identical to the self-attention
            mixed_x_layer = self.query_key_value(hidden_states)
            (mixed_query_layer, mixed_key_layer,
             mixed_value_layer) = split_tensor_along_last_dim(
                 mixed_x_layer, 3)
        else:
            cat = torch.cat((mem, hidden_states), 1)
            mixed_x_layer = self.query_key_value(cat)
            (mixed_query_layer, mixed_key_layer,
             mixed_value_layer) = split_tensor_along_last_dim(
                 mixed_x_layer, 3)
            mixed_query_layer = mixed_query_layer[:, -query_length:]

        # Reshape and transpose [b, np, s, hn]
        query_layer = self._transpose_for_scores(mixed_query_layer)
        key_layer = self._transpose_for_scores(mixed_key_layer)
        value_layer = self._transpose_for_scores(mixed_value_layer)
        if self.relative_encoding:
            relative_layer = self.relative(position_embeddings)
            relative_layer = self._transpose_for_scores(
                relative_layer)  # 1 (bsz) x n_head x klen x d_head
            # Raw attention scores. [b, np, qs, ks]
            rw_head_q = query_layer + r_w_bias.unsqueeze(1)
            ac_score = torch.matmul(rw_head_q, key_layer.transpose(-1, -2))
            rr_head_q = query_layer + r_r_bias.unsqueeze(1)
            bd_score = torch.matmul(rr_head_q,
                                    relative_layer.transpose(-1, -2))
            bd_score = self._rel_shift(bd_score)  # qlen x klen x bsz x n_head
            # bd_score = bd_score.permute(2, 3, 0, 1) # bsz n_head qlen klen

            attention_scores = ac_score + bd_score
            attention_scores = attention_scores / math.sqrt(
                self.hidden_size_per_attention_head)
        else:
            if self.attention_scale > 1.0:
                # Raw attention scores. [b, np, s, s]
                attention_scores = torch.matmul(
                    query_layer / math.sqrt(self.attention_scale),
                    key_layer.transpose(-1, -2) /
                    math.sqrt(self.hidden_size_per_attention_head *
                              self.attention_scale))
            else:
                attention_scores = torch.matmul(
                    query_layer,
                    key_layer.transpose(-1, -2) /
                    math.sqrt(self.hidden_size_per_attention_head))

        # Apply the left to right attention mask.
        attention_scores = torch.mul(attention_scores, ltor_mask)
        if self.attention_scale > 1.0:
            max_attention_scores = attention_scores.max(dim=-1,
                                                        keepdim=True)[0]
            attention_scores -= max_attention_scores
            attention_scores *= self.attention_scale
        # if torch.distributed.get_rank() == 0:
        #     print(min_attention_scores, attention_scores.max().item())
        attention_scores = attention_scores + (-65504.0) * (1.0 - ltor_mask)
        # Attention probabilities. [b, np, s, s]
        attention_probs = torch.nn.Softmax(dim=-1)(attention_scores)
        # This is actually dropping out entire tokens to attend to, which might
        # seem a bit unusual, but is taken from the original Transformer paper.
        if os.getenv("ENV_TYPE") == 'deepspeed+mpu':
            with get_cuda_rng_tracker().fork():
                attention_probs = self.attention_dropout(attention_probs)
        else:
            attention_probs = self.attention_dropout(attention_probs)
        # Context layer.
        # [b, np, s, hn]
        context_layer = torch.matmul(attention_probs, value_layer)
        # [b, s, np, hn]
        context_layer = context_layer.permute(0, 2, 1, 3).contiguous()
        new_context_layer_shape = context_layer.size()[:-2] + \
                                  (self.hidden_size_per_partition,)
        # [b, s, hp]
        context_layer = context_layer.view(*new_context_layer_shape)

        # Output. [b, s, h]
        output = self.dense(context_layer)
        output = self.output_dropout(output)

        return output


class BertParallelSelfAttention(torch.nn.Module):
    """Parallel self-attention layer for BERT.
    Self-attention layer takes input with size [b, s, h] where b is
    the batch size, s is the sequence lenght, and h is the hidden size
    and creates output of the same size.
    Arguments:
        hidden_size: total hidden size of the layer (h).
        num_attention_heads: number of attention heads (n). Note that we
                             require n to be divisible by number of GPUs
                             used to parallelize the model. Also, we
                             require hidden size be divisible by n.
        dropout_prob: dropout probability for the attention scores.
        output_parallel: If true, no all-gather is done on the output and
                         the output values will be per partition.
    We use the following notation:
        h: hidden_size
        n: num_attention_heads
        p: number of partitions
        np: n/p
        hp: h/p
        hn: h/n
        b: batch size
        s: sequence length
    """

    def __init__(self,
                 hidden_size,
                 num_attention_heads,
                 dropout_prob,
                 output_parallel=False,
                 init_method=init.xavier_normal_):
        super(BertParallelSelfAttention, self).__init__()
        # Input configuration.
        self.hidden_size = hidden_size
        self.num_attention_heads = num_attention_heads
        self.dropout_prob = dropout_prob
        self.output_parallel = output_parallel
        if os.getenv("ENV_TYPE") == 'deepspeed+mpu':
            # Per attention head and per partition values.
            world_size = get_model_parallel_world_size()
            self.hidden_size_per_partition = divide(hidden_size, world_size)
            self.hidden_size_per_attention_head = divide(
                hidden_size, num_attention_heads)
            self.num_attention_heads_per_partition = divide(
                num_attention_heads, world_size)
            # Strided linear layer.
            self.query_key_value = ColumnParallelLinear(
                hidden_size,
                3 * hidden_size,
                stride=3,
                gather_output=False,
                init_method=init_method)
        else:
            self.hidden_size_per_partition = hidden_size
            self.hidden_size_per_attention_head = divide(
                hidden_size, num_attention_heads)
            self.num_attention_heads_per_partition = num_attention_heads
            # Strided linear layer.
            self.query_key_value = Linear(hidden_size, 3 * hidden_size)

        # Dropout. Note that for a single iteration, this layer will generate
        # different outputs on different number of parallel partitions but
        # on average it should not be partition dependent.
        self.dropout = torch.nn.Dropout(dropout_prob)

    def _transpose_for_scores(self, tensor):
        """Transpose a 3D tensor [b, s, np*hn] into a 4D tensor with
        size [b, np, s, hn].
        """
        new_tensor_shape = tensor.size()[:-1] + \
                           (self.num_attention_heads_per_partition,
                            self.hidden_size_per_attention_head)
        tensor = tensor.view(*new_tensor_shape)
        return tensor.permute(0, 2, 1, 3)

    def forward(self, hidden_states, attention_mask):

        # Attention heads. [b, s, hp]
        mixed_x_layer = self.query_key_value(hidden_states)
        (mixed_query_layer, mixed_key_layer,
         mixed_value_layer) = split_tensor_along_last_dim(mixed_x_layer, 3)

        # Reshape and transpose [b, np, s, hn]
        query_layer = self._transpose_for_scores(mixed_query_layer)
        key_layer = self._transpose_for_scores(mixed_key_layer)
        value_layer = self._transpose_for_scores(mixed_value_layer)

        # Raw attention scores. [b, np, s, s]
        norm_factor = math.sqrt(math.sqrt(self.hidden_size_per_attention_head))
        attention_scores = torch.matmul(
            query_layer / norm_factor,
            key_layer.transpose(-1, -2) / norm_factor)
        # Apply the attention mask.
        attention_scores += attention_mask

        # Attention probabilities. [b, np, s, s]
        attention_probs = torch.nn.Softmax(dim=-1)(attention_scores)
        # This is actually dropping out entire tokens to attend to, which might
        # seem a bit unusual, but is taken from the original Transformer paper.
        if os.getenv("ENV_TYPE") == 'deepspeed+mpu':
            with get_cuda_rng_tracker().fork():
                attention_probs = self.dropout(attention_probs)
        else:
            attention_probs = self.dropout(attention_probs)

        # Context layer.
        # [b, np, s, hn]
        context_layer = torch.matmul(attention_probs, value_layer)
        # [b, s, np, hn]
        context_layer = context_layer.permute(0, 2, 1, 3).contiguous()
        new_context_layer_shape = context_layer.size()[:-2] + \
                                  (self.hidden_size_per_partition,)
        # [b, s, hp]
        context_layer = context_layer.view(*new_context_layer_shape)

        # Output. [b, s, h]
        if self.output_parallel:
            output = context_layer
        else:
            if os.getenv("ENV_TYPE") == 'deepspeed+mpu':
                output = gather_from_model_parallel_region(context_layer)
            else:
                output = context_layer
        return output


class BertSelfOutput(torch.nn.Module):

    def __init__(self, hidden_size, initializer_range, layernorm_epsilon,
                 hidden_dropout_prob):
        super(BertSelfOutput, self).__init__()
        if os.getenv("ENV_TYPE") == 'deepspeed+mpu':
            init_method = normal_init_method(mean=0.0, std=initializer_range)
            self.dense = RowParallelLinear(input_size=hidden_size,
                                           output_size=hidden_size,
                                           bias=True,
                                           input_is_parallel=True,
                                           stride=1,
                                           init_method=init_method)
        else:
            self.dense = Linear(hidden_size, hidden_size)
        self.LayerNorm = BertLayerNorm(hidden_size, eps=layernorm_epsilon)
        self.dropout = torch.nn.Dropout(hidden_dropout_prob)

    def forward(self, hidden_states, input_tensor):
        hidden_states = self.dense(hidden_states)
        hidden_states = self.dropout(hidden_states)
        ln_input = hidden_states + input_tensor
        hidden_states = self.LayerNorm(ln_input)
        return hidden_states


class BertAttention(torch.nn.Module):

    def __init__(self, hidden_size, num_attention_heads,
                 attention_probs_dropout_prob, initializer_range,
                 layernorm_epsilon, hidden_dropout_prob):
        super(BertAttention, self).__init__()
        self.self = BertParallelSelfAttention(
            hidden_size=hidden_size,
            num_attention_heads=num_attention_heads,
            dropout_prob=attention_probs_dropout_prob,
            output_parallel=True,
            init_method=normal_init_method(mean=0.0, std=initializer_range))
        self.output = BertSelfOutput(hidden_size, initializer_range,
                                     layernorm_epsilon, hidden_dropout_prob)

    def forward(self, input_tensor, attention_mask):
        self_output = self.self(input_tensor, attention_mask)
        attention_output = self.output(self_output, input_tensor)
        return attention_output
