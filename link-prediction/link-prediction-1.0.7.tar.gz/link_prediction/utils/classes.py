from math import dist
from typing import Optional, Union
from dataclasses import dataclass


@dataclass
class Source:
    id: int
    page_id: int

    def to_dict(self):
        return {
            "id": self.id,
            "pageId": self.page_id,
        }


@dataclass
class Link:
    source: Source
    target_id: int
    id: Optional[int] = None

    def to_dict(self):
        return {
            "id": self.id,
            "source": self.source.to_dict(),
            "targetId": self.target_id,
        }


@dataclass
class Bounds:
    x: int
    y: int
    width: int
    height: int

    def from_dict(ui_element_dict):
        return Bounds(
            x=ui_element_dict["x"],
            y=ui_element_dict["y"],
            width=ui_element_dict["width"],
            height=ui_element_dict["height"],
        )


@dataclass
class Point:
    x: Union[int, float]
    y: Union[int, float]


@dataclass
class UIElement:
    id: str
    name: str
    type: str
    bounds: Bounds
    children: Optional[list] = None  # Optional[list[UIElement]]
    characters: Optional[str] = None
    evaluation_id: Optional[int] = None
    is_clickable: bool = True
    is_visible: bool = True

    def from_dict(ui_element_dict):
        children: list[UIElement] = (
            [
                UIElement.from_dict(child_element_dict)
                for child_element_dict in ui_element_dict["children"]
            ]
            if "children" in ui_element_dict
            else []
        )
        return UIElement(
            id=ui_element_dict["id"],
            name=ui_element_dict["name"],
            type=ui_element_dict["type"],
            bounds=Bounds.from_dict(ui_element_dict["bounds"]),
            characters=ui_element_dict["characters"]
            if "characters" in ui_element_dict
            else None,
            evaluation_id=ui_element_dict["evaluationId"]
            if "evaluationId" in ui_element_dict
            else None,
            children=children,
        )

    @property
    def elements_with_evaluation_id(self):
        elements: list[UIElement] = [
            element for element in self.elements if element.evaluation_id
        ]
        return elements

    @property
    def elements(self):
        """Returns flat list of children elements"""
        if not self.children:
            return []
        ui_elements: list[UIElement] = []
        elements_to_search: list[UIElement] = self.children.copy()
        while len(elements_to_search) > 0:
            top_element = elements_to_search.pop()
            ui_elements.append(top_element)
            if top_element.children:
                for child_element in top_element.children:
                    elements_to_search.append(child_element)
        return ui_elements

    @property
    def texts(self) -> Optional[list[str]]:
        all_texts = []
        if self.children:
            all_children_texts = [
                ui_element.characters
                for ui_element in self.elements
                if ui_element.characters
            ]
            all_texts += all_children_texts
        if self.characters:
            all_texts.append(self.characters)
        if len(all_texts) == 0:
            return None
        flat_list_of_words = [
            word
            for text_per_element in all_texts
            for word in text_per_element.split(" ")
        ]
        return flat_list_of_words

    @property
    def center(self) -> Point:
        return Point(
            x=self.bounds.x + self.bounds.width / 2,
            y=self.bounds.y + self.bounds.height / 2,
        )


@dataclass
class Page:
    id: str
    name: str
    height: int
    width: int
    children: list[UIElement]
    evaluation_id: Optional[int] = None

    def from_dict(page_dict):
        children: list[UIElement] = [
            UIElement.from_dict(ui_element_dict)
            for ui_element_dict in page_dict["children"]
        ]
        return Page(
            id=page_dict["id"],
            name=page_dict["name"],
            height=page_dict["height"],
            width=page_dict["width"],
            children=children,
            evaluation_id=page_dict["evaluationId"]
            if "evaluationId" in page_dict
            else None,
        )

    def find_by_id(self, element_id: str) -> Optional[UIElement]:
        elements_to_search = self.children.copy()
        while len(elements_to_search) > 0:
            top_element = elements_to_search.pop()
            if top_element.id == element_id:
                return top_element
            if top_element.children:
                for child_element in top_element.children:
                    elements_to_search.append(child_element)
        return None

    @property
    def elements_with_evaluation_id(self) -> list[UIElement]:
        return [element for element in self.elements if element.evaluation_id]

    @property
    def elements_with_text(self) -> list[UIElement]:
        return [element for element in self.elements if element.characters]

    @property
    def leaf_elements(self) -> list[UIElement]:
        return [element for element in self.elements if not element.children]

    @property
    def elements(self) -> list[UIElement]:
        """Returns flat list of children elements"""
        ui_elements = self.children.copy() + [
            element
            for elements in [direct_child.elements for direct_child in self.children]
            for element in elements
        ]
        return ui_elements

    def copy(self):
        return Page(
            id=self.id,
            name=self.name,
            height=self.height,
            width=self.width,
            children=self.children,
            evaluation_id=self.evaluation_id,
        )

    @property
    def texts(self) -> list[str]:
        all_texts = [
            direct_child.texts for direct_child in self.children if direct_child.texts
        ]
        flat_list_of_words = [
            word for text_per_element in all_texts for word in text_per_element
        ]
        return flat_list_of_words

    def get_closest_neighbors(
        self, element_id: str, number_of_neighbors=4, include_non_text=True
    ) -> Optional[list[UIElement]]:
        """
        Returns a list of the up to n closest leaf nodes to the UI element
        with the specified ID measured by Euclidean distance between
        the center points.
        """
        base_element = self.find_by_id(element_id=element_id)
        ui_elements = self.elements
        if len(ui_elements) == 0:
            return None
        if include_non_text:
            leaf_nodes = [element for element in ui_elements if not element.children]
        else:
            text_nodes = [element for element in ui_elements if element.characters]
            leaf_nodes = text_nodes
        if len(leaf_nodes) == 0:
            return None
        base_element_center = base_element.center
        elements_and_distances = []
        for leaf_node in leaf_nodes:
            if leaf_node.id == base_element.id:
                continue
            if base_element.children and leaf_node.id in [
                child_element.id for child_element in base_element.elements
            ]:
                continue
            elements_and_distances.append(
                {
                    "element": leaf_node,
                    "distance": dist(
                        (base_element_center.x, base_element_center.y),
                        (leaf_node.center.x, leaf_node.center.y),
                    ),
                }
            )
        sorted_elements = sorted(
            elements_and_distances,
            key=lambda element_and_distance: element_and_distance["distance"],
        )
        closest_elements = sorted_elements[:number_of_neighbors]
        return [
            element_and_distance["element"] for element_and_distance in closest_elements
        ]

    def get_element_at(self, point: Point) -> Optional[UIElement]:
        """Returns the lowest level visible UI element at the given coordinates"""
        elements_sorted_by_hierarchy = sorted(
            [element for element in self.elements if element.is_visible],
            key=lambda ui_element: len(ui_element.children)
            if ui_element.children
            else 0,
        )
        for ui_element in elements_sorted_by_hierarchy:
            point_inside_bounds = (
                ui_element.bounds.x < point.x
                and ui_element.bounds.y < point.y
                and ui_element.bounds.x + ui_element.bounds.width > point.x
                and ui_element.bounds.y + ui_element.bounds.height > point.y
            )
            if point_inside_bounds:
                return ui_element
        return None


@dataclass
class Design:
    pages: list[Page]

    def from_dict(design_dict):
        pages: list[Page] = []
        for page_dict in design_dict["pages"]:
            page = Page.from_dict(page_dict)
            pages.append(page)
        return Design(pages=pages)

    def find_by_id(self, page_id: str, element_id: str) -> UIElement:
        page = self.find_page_by_id(page_id=page_id)
        element = page.find_by_id(element_id=element_id)
        return element

    def find_page_by_id(self, page_id: str) -> Page:
        try:
            return [page for page in self.pages if page.id == page_id][0]
        except Exception as e:
            return None


@dataclass
class Application:
    id: int
    design: Design
    links: list[Link]

    def to_dict(self):
        return {"id": self.id, "links": [link.to_dict() for link in self.links]}

    def copy(self):
        return Application(id=self.id, design=self.design, links=self.links)
