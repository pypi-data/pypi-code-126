"""Figma-related data definitions and loaders."""

from __future__ import annotations
import json
import os
import requests
import pandas as pd
import tarfile
from typing import Optional
from link_prediction.utils.classes import Design
from dataclasses import dataclass, asdict

FIGMA_APPLICATIONS = ["shaeds", "monet", "jet", "atlas"]


@dataclass
class FigmaDataPoint:
    """Represents a link in a Figma design."""

    @dataclass
    class SourceData:
        """Represents the source of a link in a Figma design."""

        id: str
        page_id: str

        def from_dict(data: dict) -> FigmaDataPoint.SourceData:
            """Returns a SourceData instance from the provided data."""
            return FigmaDataPoint.SourceData(
                id=data["id"],
                page_id=data["page_id"],
            )

    def __init__(
        self,
        application_id: int,
        source: SourceData,
        target_id: str,
        id: Optional[int] = None,
        is_link: bool = False,
    ) -> None:
        self.application_id = application_id
        self.source = source
        self.target_id = target_id
        self.id = id
        self.is_link = is_link
        with open(
            f"data/external/figma/view_hierarchies/{FIGMA_APPLICATIONS[application_id - 1]}.json"
        ) as f:
            design_dict = json.load(f)
        design = Design.from_dict(design_dict)
        self.source_page = design.find_page_by_id(source.page_id)
        self.source_element = self.source_page.find_by_id(source.id)
        self.target_page = design.find_page_by_id(target_id)

    def from_dict(data: dict) -> FigmaDataPoint:
        """Returns a FigmaDataPoint instance from the provided data."""
        return FigmaDataPoint(
            application_id=data["application_id"],
            id=data["id"],
            source=FigmaDataPoint.SourceData.from_dict(data["source"]),
            target_id=data["target_id"],
            is_link=data["is_link"] if "is_link" in data else False,
        )

    def to_dict(self) -> dict:
        """Returns a dictionary representation of the instance."""
        data_point_dict = {}
        for attribute in ["application_id", "target_id", "id", "is_link"]:
            data_point_dict[attribute] = getattr(self, attribute)
        data_point_dict["source"] = asdict(self.source)
        return data_point_dict


def load_figma_links(
    return_X_y=False, number_of_data_points=100, download_external_data=False
):
    """Load and return the Figma link dataset (classification)."""
    if download_external_data:
        download_figma_data()
    figma_links_df = pd.read_csv("data/processed/figma-links.csv")
    raw_links_data = [
        {
            "id": int(row["link_id"]) if row["link_id"] != "-99" else None,
            "application_id": FIGMA_APPLICATIONS.index(row["application_name"]) + 1,
            "is_link": int(row["label"]) == 1,
            "target_id": row["target_screen_id"],
            "source": {
                "page_id": row["source_screen_id"],
                "id": row["source_element_id"],
            },
        }
        for _, row in figma_links_df.iterrows()
    ]
    figma_data_points: list[FigmaDataPoint] = [
        FigmaDataPoint.from_dict(raw_link_data)
        for raw_link_data in raw_links_data[:number_of_data_points]
    ]
    if return_X_y:
        y = [int(figma_data_point.is_link) for figma_data_point in figma_data_points]
        return figma_data_points, y
    return figma_data_points


def download_figma_data():
    """Download all required Figma data."""
    # Download the Figma view hierarchies
    url = "https://github.com/christophajohns/figma-links/raw/main/view_hierarchies.tar.gz"
    figma_dir_path = "data/raw/figma"
    figma_file_path = f"{figma_dir_path}/view_hierarchies.tar.gz"
    if not os.path.exists(figma_dir_path):
        os.makedirs(figma_dir_path)
    if not os.path.exists(figma_file_path):
        print("Downloading Figma view hierarchies...")
        response = requests.get(url, stream=True)
        with open(figma_file_path, "wb") as f:
            f.write(response.content)
        print("Done downloading Figma view hierarchies.")
    else:
        print("Figma view hierarchies already downloaded.")

    # Extract the Figma view hierarchies
    if not os.path.exists(f"{figma_dir_path}/view_hierarchies"):
        print("Extracting Figma view hierarchies...")
        file = tarfile.open(figma_file_path)
        file.extractall(figma_dir_path)
        file.close()
        print("Done extracting Figma view hierarchies.")
    else:
        print("Figma view hierarchies already extracted.")

    # Download Figma_links dataset IDs
    url = "https://raw.githubusercontent.com/christophajohns/figma-links/main/figma-links.csv"
    processed_data_dir = "data/processed/"
    figma_links_file_path = f"{processed_data_dir}/figma-links.csv"
    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)
    if not os.path.exists(figma_links_file_path):
        print("Downloading Figma_links dataset IDs...")
        response = requests.get(url)
        with open(figma_links_file_path, "w") as f:
            f.write(response.text)
        print("Done downloading Figma_links dataset IDs.")
    else:
        print("Figma_links dataset IDs already extracted.")


def main() -> None:
    """Load Figma data."""
    download_figma_data()


if __name__ == "__main__":
    main()
