"""Classes to represent a screen's layout."""

import numpy as np
from link_prediction.utils.classes import Page, UIElement
from PIL import Image


class ScreenLayout:
    def __init__(self, page: Page):
        """Represents a screen's layout."""
        self.scaled_height = 100
        self.scaled_width = 56
        self.pixels = np.full((self.scaled_height, self.scaled_width, 2), 0, dtype=int)
        self.vert_scale = self.scaled_height / page.height
        self.horiz_scale = self.scaled_width / page.width
        self.set_pixels_to_page_content(page)

    def get_scaled_position(self, ui_element: UIElement):
        x_top = int(ui_element.bounds.x * self.horiz_scale)
        y_top = int(ui_element.bounds.y * self.vert_scale)
        x_bottom = int(ui_element.bounds.x + ui_element.bounds.width * self.horiz_scale)
        y_bottom = int(ui_element.bounds.y + ui_element.bounds.height * self.vert_scale)
        return x_top, y_top, x_bottom, y_bottom

    def set_pixels_to_page_content(self, page: Page):
        """
        Sets the blue/red channel on the scaled pixel values to 1 for each
        leaf element dependent on whether it contains text or not.
        """
        for leaf_element in page.leaf_elements:
            x_top, y_top, x_bottom, y_bottom = self.get_scaled_position(leaf_element)
            if (
                leaf_element.is_visible
                and leaf_element.characters
                and leaf_element.characters != ""
            ):
                # append in 'blue' ([0]) here
                self.pixels[y_top:y_bottom, x_top:x_bottom, 0] = 1
            else:
                # append in 'red' ([1]) here
                self.pixels[y_top:y_bottom, x_top:x_bottom, 1] = 1

    def convert_to_image(self):
        p = np.full((self.scaled_height, self.scaled_width, 3), 255, dtype=np.uint)
        for y in range(len(self.pixels)):
            for x in range(len(self.pixels[0])):
                if (self.pixels[y][x] == [1, 0]).all() or (
                    self.pixels[y][x] == [1, 1]
                ).all():
                    p[y][x] = [0, 0, 255]
                elif (self.pixels[y][x] == [0, 1]).all():
                    p[y][x] = [255, 0, 0]
        im = Image.fromarray(p.astype(np.uint8))
        im.save("example.png")
