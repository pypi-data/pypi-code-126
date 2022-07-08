from torch.optim.lr_scheduler import OneCycleLR


class OneLongCycleLR(OneCycleLR):
    """
    Extends OneCycleLR and doesn't make it crash when the cycle is over.
    Instead, it keeps on returning the last value.
    """

    def get_lr(self):
        try:
            return super().get_lr()
        except ValueError:
            return self.get_last_lr()
