"""RICO-related data definitions and loaders."""

from __future__ import annotations
from dataclasses import MISSING, dataclass, field
import dataclasses
import json
import pandas as pd
import os
from typing import Literal, Optional
from uuid import uuid4
import requests
import tarfile
from tqdm import tqdm
from link_prediction.utils.classes import Bounds, Page, Point, UIElement


@dataclass
class Gesture:
    page: Page
    touchpoints: list[Point]

    @property
    def is_click(self) -> bool:
        return len(self.touchpoints) == 1

    @property
    def touched_element(self) -> Optional[UIElement]:
        return self.page.get_element_at(self.touchpoints[0])

    def get_gestures_from_dict(
        gestures_data: dict, view_hierarchies: list[ViewHierarchy]
    ) -> Optional[list[Gesture]]:
        """Returns a list of Gesture instances based on the provided data"""
        gestures = []
        for page_id, touchpoints in gestures_data.items():
            try:
                page = [
                    view_hierarchy
                    for view_hierarchy in view_hierarchies
                    if view_hierarchy.request_id == page_id
                ][0].to_page()
            except IndexError:
                continue
            if len(touchpoints) == 0:
                continue
            gesture = Gesture(
                page=page,
                touchpoints=[
                    Point(x=touchpoint[0] * 1440, y=touchpoint[1] * 2560)
                    for touchpoint in touchpoints
                ],
            )
            gestures.append(gesture)
        return gestures


@dataclass
class Interaction:
    gesture: Gesture
    source_page: Page
    target_page: Page


@dataclass
class RicoNode:
    is_clickable: bool
    is_visible: bool  # needs to be computed from draw, visibility, visible-to-user, bounds
    bounds: list[int]  # x_top, y_top, x_bottom, y_bottom
    ancestors: list[str]
    text: Optional[str] = None  # can also be ""
    children: Optional[list[RicoNode]] = None
    android_class: Optional[str] = None
    pointer: Optional[str] = None

    def to_ui_element(self) -> UIElement:
        """
        Returns a UIElement instance from the node's data
        """
        element_type = (
            self.android_class if self.android_class else "/".join(self.ancestors)
        )
        x_top, y_top, x_bottom, y_bottom = self.bounds
        bounds = Bounds(
            x=x_top, y=y_top, width=x_bottom - x_top, height=y_bottom - y_top
        )
        element_id = self.pointer if self.pointer else str(uuid4())
        children = (
            [child.to_ui_element() for child in self.children]
            if self.children
            else None
        )
        return UIElement(
            id=element_id,
            name=element_id,
            type=element_type,
            bounds=bounds,
            children=children,
            characters=self.text,
            is_clickable=self.is_clickable,
            is_visible=self.is_visible,
        )

    def from_dict(data: dict) -> RicoNode:
        """Returns a RicoNode instance from the provided data"""
        is_visible = False
        if "visibility" in data and data["visibility"] == "visible":
            is_visible = True
        if "visible-to-user" in data and data["visible-to-user"]:
            is_visible = True
        x_top, y_top, x_bottom, y_bottom = data["bounds"]
        element_is_left_of_view = x_top < 0 and x_bottom < 0
        element_is_right_of_view = x_top > 1440 and x_bottom > 1440
        element_is_over_view = y_top < 0 and y_bottom < 0
        element_is_under_view = y_top > 2560 and y_bottom > 2560
        element_is_out_of_view = any(
            [
                element_is_left_of_view,
                element_is_right_of_view,
                element_is_over_view,
                element_is_under_view,
            ]
        )
        if element_is_out_of_view:
            is_visible = False
        width = x_bottom - x_top
        height = y_bottom - y_top
        if width == 0 or height == 0:
            is_visible = False
        return RicoNode(
            is_clickable=data["clickable"],
            children=[
                RicoNode.from_dict(child_data)
                for child_data in data["children"]
                if child_data is not None
            ]
            if "children" in data
            else None,
            is_visible=is_visible,
            bounds=data["bounds"],
            android_class=data["class"] if "class" in data else None,
            ancestors=data["ancestors"],
            text=data["text"] if "text" in data else None,
            pointer=data["pointer"] if "pointer" in data else None,
        )


@dataclass
class Activity:
    root: RicoNode

    def from_dict(data: dict) -> Activity:
        """Returns a Activity instance from the provided data"""
        return Activity(root=RicoNode.from_dict(data["root"]))


@dataclass
class ViewHierarchy:
    activity_name: str
    activity: Activity
    request_id: str

    def to_page(self) -> Page:
        """
        Returns a Page instance from the view hierarchy's data
        """
        return Page(
            id=self.request_id,
            name=f"{self.activity_name}:{self.request_id}",
            height=2560,
            width=1440,
            children=[child.to_ui_element() for child in self.activity.root.children],
        )

    def from_dict(data: dict, request_id: Optional[str] = None) -> ViewHierarchy:
        """Returns a ViewHierarchy instance from the provided data"""
        return ViewHierarchy(
            activity_name=data["activity_name"],
            activity=Activity.from_dict(data["activity"]),
            request_id=request_id if request_id else data["request_id"],
        )

    def from_file(
        view_hierarchy_file: str, request_id: Optional[str] = None
    ) -> ViewHierarchy:
        with open(view_hierarchy_file) as f:
            view_hierarchy_data = json.load(f)
        return ViewHierarchy.from_dict(view_hierarchy_data, request_id=request_id)


@dataclass
class Trace:
    id: str
    gestures: list[Gesture]
    view_hierarchies: list[ViewHierarchy]  # has length = len(gestures) + 1

    def get_interactions(self) -> list[Interaction]:
        """
        Returns a list of interactions based on the trace's gestures
        and view hierarchies
        """
        interactions: list[Interaction] = []
        sorted_gestures = sorted(
            self.gestures, key=lambda gesture: int(gesture.page.id)
        )
        for i in range(len(sorted_gestures) - 1):
            gesture = self.gestures[i]
            gesture.page.id
            sorted_view_hierarchies = sorted(
                self.view_hierarchies,
                key=lambda view_hierarchy: int(view_hierarchy.request_id),
            )
            gesture_page_indices = [
                index
                for index, view_hierarchy in enumerate(sorted_view_hierarchies)
                if view_hierarchy.request_id == gesture.page.id
            ]
            if len(gesture_page_indices) == 0:
                # Source view hierarchy not found
                continue
            gesture_page_index = gesture_page_indices[0]
            if len(sorted_view_hierarchies) < gesture_page_index + 2:
                # Target view hierarchy not found
                continue
            target_view_hierarchy = sorted_view_hierarchies[gesture_page_index + 1]
            target_page = target_view_hierarchy.to_page()
            interaction = Interaction(
                gesture=gesture,
                source_page=gesture.page,
                target_page=target_page,
            )
            interactions.append(interaction)
        return interactions

    def from_directory(directory_path: str) -> Trace:
        """Returns a Trace instance based on the data in the provided directory"""
        view_hierarchies_dir = f"{directory_path}/view_hierarchies"
        view_hierarchy_files = [
            f"{view_hierarchies_dir}/{file}"
            for file in os.listdir(view_hierarchies_dir)
            if file.endswith(".json")
        ]
        view_hierarchies: list[ViewHierarchy] = []
        for view_hierarchy_file in view_hierarchy_files:
            with open(view_hierarchy_file) as f:
                view_hierarchy_data: dict = json.load(f)
            if view_hierarchy_data is not None:
                view_hierarchy = ViewHierarchy.from_dict(
                    view_hierarchy_data,
                    request_id=view_hierarchy_file.split("/")[-1].split(".")[-2],
                )
                view_hierarchies.append(view_hierarchy)
        gestures_file = f"{directory_path}/gestures.json"
        with open(gestures_file) as f:
            gestures_data: dict = json.load(f)
        gestures = Gesture.get_gestures_from_dict(
            gestures_data,
            view_hierarchies=view_hierarchies,
        )
        trace_id = directory_path.split("_")[-1]
        return Trace(id=trace_id, view_hierarchies=view_hierarchies, gestures=gestures)


@dataclass
class Application:
    traces: list[Trace]
    name: str

    def from_directory(directory_path: str) -> Application:
        """Returns an Application instance based on the data in the provided directory"""
        traces = [
            Trace.from_directory(f"{directory_path}/{directory}")
            for directory in os.listdir(directory_path)
            if directory.startswith("trace_")
        ]
        application_name = directory_path.split("/")[-1]
        return Application(traces=traces, name=application_name)


class RicoData:
    def get_applications_with_traces(
        filtered_traces_path="data/external/rico/filtered_traces",
        number_of_directories_to_iterate_over=10000,
    ) -> list[Application]:
        """
        Returns a list of applications based on the RICO interaction traces
        at the provided path
        """
        for directory in sorted(
            os.listdir(filtered_traces_path)[:number_of_directories_to_iterate_over]
        ):
            if directory != ".DS_Store":
                yield Application.from_directory(f"{filtered_traces_path}/{directory}")


@dataclass
class RicoDataPoint:
    """Represent a potential link data point from the RICO dataset."""

    @dataclass
    class RicoScreen:
        id: int

        @property
        def view_hierarchy_file(self):
            return f"view_hierarchies/{self.id}.json"

        @property
        def screenshot_file(self):
            return f"screenshots/{self.id}.jpg"

        def from_dict(data: dict):
            return RicoDataPoint.RicoScreen(id=data["id"])

        def to_dict(self):
            return dataclasses.asdict(self)

    @dataclass
    class RawSourceData(RicoScreen):
        element_id: str | None = None  # pointer (e.g., "2e18ce7")

        def from_dict(data: dict):
            return RicoDataPoint.RawSourceData(
                id=data["id"],
                element_id=data["element_id"] if "element_id" in data else None,
            )

    source: RawSourceData
    target: RicoScreen
    application_name: str
    trace_id: int
    data_type: Literal["link", "non-source", "non-target"]
    source_view_hierarchy: ViewHierarchy = field(kw_only=True)
    source_page: Page = field(init=False)
    target_view_hierarchy: ViewHierarchy = field(kw_only=True)
    target_page: Page = field(init=False)

    def __post_init__(self) -> None:
        if self.source_view_hierarchy == MISSING:
            self.source_view_hierarchy = ViewHierarchy.from_file(
                f"data/external/rico/filtered_traces/{self.source_view_hierarchy_file}",
                request_id=str(self.source.id),
            )
        self.source_page = self.source_view_hierarchy.to_page()
        if self.target_view_hierarchy == MISSING:
            self.target_view_hierarchy = ViewHierarchy.from_file(
                f"data/external/rico/filtered_traces/{self.target_view_hierarchy_file}",
                request_id=str(self.target.id),
            )
        self.target_page = self.target_view_hierarchy.to_page()

    @property
    def trace_dir(self):
        return f"{self.application_name}/trace_{self.trace_id}"

    @property
    def gestures_file(self):
        return f"{self.application_name}/trace_{self.trace_id}/gestures.json"

    @property
    def source_view_hierarchy_file(self):
        return f"{self.trace_dir}/{self.source.view_hierarchy_file}"

    @property
    def source_screenshot_file(self):
        return f"{self.trace_dir}/{self.source.screenshot_file}"

    @property
    def target_view_hierarchy_file(self):
        return f"{self.trace_dir}/{self.target.view_hierarchy_file}"

    @property
    def target_screenshot_file(self):
        return f"{self.trace_dir}/{self.target.screenshot_file}"

    @property
    def source_element(self) -> UIElement:
        element = self.source_page.find_by_id(self.source.element_id)
        if element is None:
            return self.source_page
        return element

    @property
    def is_link(self):
        return self.data_type == "link"

    def to_dict(self):
        return {
            "source": self.source.to_dict(),
            "target": self.target.to_dict(),
            "application_name": self.application_name,
            "trace_id": self.trace_id,
            "data_type": self.data_type,
        }

    def from_dict(data: dict):
        return RicoDataPoint(
            source=RicoDataPoint.RawSourceData.from_dict(data["source"]),
            target=RicoDataPoint.RicoScreen.from_dict(data["target"]),
            application_name=data["application_name"],
            trace_id=data["trace_id"],
            data_type=data["data_type"],
        )


def load_rico_links(
    return_X_y=False, number_of_data_points=1000, download_external_data=False
):
    """Load and return the RICO link dataset (classification)."""
    if download_external_data:
        download_rico_data()
    rico_links_df = pd.read_csv("data/processed/rico_links.csv")
    raw_links_data = [
        {
            "application_name": row["application_name"],
            "trace_id": row["interaction_trace_id"],
            "data_type": row["data_type"],
            "target": {
                "id": row["target_screen_id"],
            },
            "source": {
                "id": row["source_screen_id"],
                "element_id": row["source_element_id"],
            },
        }
        for _, row in rico_links_df.iterrows()
    ]
    rico_data_points: list[RicoDataPoint] = [
        RicoDataPoint.from_dict(raw_link_data)
        for raw_link_data in raw_links_data[:number_of_data_points]
    ]
    if return_X_y:
        y = [int(rico_data_point.is_link) for rico_data_point in rico_data_points]
        return rico_data_points, y
    return rico_data_points


def download_rico_data():
    """Download all required RICO data."""
    # Download the RICO interaction traces
    url = "https://storage.googleapis.com/crowdstf-rico-uiuc-4540/rico_dataset_v0.1/traces.tar.gz"
    rico_dir_path = "data/external/rico"
    rico_file_path = f"{rico_dir_path}/traces.tar.gz"
    if not os.path.exists(rico_dir_path):
        os.makedirs(rico_dir_path)
    if not os.path.exists(rico_file_path):
        response = requests.get(url, stream=True)
        with tqdm.wrapattr(
            open(rico_file_path, "wb"),
            "write",
            miniters=1,
            desc="Downloading interaction traces",
            total=int(response.headers.get("content-length", 0)),
        ) as fout:
            for chunk in response.iter_content(chunk_size=4096):
                fout.write(chunk)
    else:
        print("RICO traces already downloaded.")

    # Extract the RICO traces
    if not os.path.exists(f"{rico_dir_path}/filtered_traces"):
        print("Extracting RICO traces...")
        file = tarfile.open(rico_file_path)
        file.extractall(rico_dir_path)
        file.close()
        print("Done extracting RICO traces.")
    else:
        print("RICO traces already extracted.")

    # Download RICO_links dataset IDs
    url = "https://raw.githubusercontent.com/christophajohns/rico-links/main/rico_links.csv"
    processed_data_dir = "data/processed/"
    rico_links_file_path = f"{processed_data_dir}/rico_links.csv"
    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)
    if not os.path.exists(rico_links_file_path):
        print("Downloading RICO_links dataset IDs...")
        response = requests.get(url)
        with open(rico_links_file_path, "w") as f:
            f.write(response.text)
        print("Done downloading RICO_links dataset IDs.")
    else:
        print("RICO_links dataset IDs already extracted.")


def main() -> None:
    """Load RICO data."""
    download_rico_data()


if __name__ == "__main__":
    main()
