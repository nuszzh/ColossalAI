#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .amp_type import AMP_TYPE
from colossalai.context import Config
import torch.nn as nn
from torch.optim import Optimizer
from torch.nn.modules.loss import _Loss
from .torch_amp import convert_to_torch_amp
from .apex_amp import convert_to_apex_amp
from .naive_amp import convert_to_naive_amp


def convert_to_amp(model: nn.Module,
                   optimizer: Optimizer,
                   criterion: _Loss,
                   mode: AMP_TYPE,
                   amp_config: Config = None):
    assert isinstance(mode, AMP_TYPE), \
        f'expected the argument mode be AMP_TYPE, but got {type(mode)}'

    if amp_config is None:
        amp_config = Config()

    if mode == AMP_TYPE.TORCH:
        model, optimizer, criterion = convert_to_torch_amp(model, optimizer, criterion, amp_config)
    elif mode == AMP_TYPE.APEX:
        model, optimizer = convert_to_apex_amp(model, optimizer, amp_config)
    elif mode == AMP_TYPE.NAIVE:
        model, optimizer = convert_to_naive_amp(model, optimizer, amp_config)

    return model, optimizer, criterion