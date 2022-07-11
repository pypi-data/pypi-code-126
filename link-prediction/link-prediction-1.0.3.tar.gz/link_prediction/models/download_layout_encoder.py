"""Download the pre-trained RICO layout autoencoder model."""

import os
import requests
from tqdm import tqdm


def main() -> None:
    """Download the pre-trained RICO layout autoencoder model."""
    # Download the RICO layout autoencoder
    rico_layout_autoencoder_url = (
        "http://basalt.amulet.cs.cmu.edu/screen2vec/layout_encoder.ep800"
    )
    model_file_name = rico_layout_autoencoder_url.split("/")[-1]
    models_dir_path = "models"
    rico_layout_autoencoder_file = f"{models_dir_path}/{model_file_name}"
    if not os.path.exists(rico_layout_autoencoder_file):
        response = requests.get(rico_layout_autoencoder_url, stream=True)
        with tqdm.wrapattr(
            open(rico_layout_autoencoder_file, "wb"),
            "write",
            miniters=1,
            desc="Downloading RICO layout autoencoder",
            total=int(response.headers.get("content-length", 0)),
        ) as fout:
            for chunk in response.iter_content(chunk_size=4096):
                fout.write(chunk)
    else:
        print("RICO layout autoencoder already downloaded.")


if __name__ == "__main__":
    main()
