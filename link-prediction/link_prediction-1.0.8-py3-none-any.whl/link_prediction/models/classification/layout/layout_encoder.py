"""Models to encode a screen's layout."""

import torch
import torch.nn as nn
import torch.nn.functional as F
import os
from link_prediction.models.download_layout_encoder import download_state_dict


class LayoutEncoder(nn.Module):
    def __init__(
        self,
        autoencoder_state_dict_path="models/layout_encoder.ep800",
    ):
        """RICO layout autoencoder."""
        super(LayoutEncoder, self).__init__()

        self.e1 = nn.Linear(11200, 2048)
        self.e2 = nn.Linear(2048, 256)
        self.e3 = nn.Linear(256, 64)

        if not os.path.exists(autoencoder_state_dict_path):
            download_state_dict()

        autoencoder_state_dict = torch.load(
            autoencoder_state_dict_path,
            map_location=torch.device("cpu"),
        )
        encoder_state_dict = {
            key.split("enc.")[-1]: value
            for key, value in autoencoder_state_dict.items()
            if key.startswith("enc.")
        }
        self.load_state_dict(encoder_state_dict)

    def forward(self, input: torch.FloatTensor):
        encoded = F.relu(self.e3(F.relu(self.e2(F.relu(self.e1(input))))))
        return encoded
