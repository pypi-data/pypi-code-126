"""
Class to parse and analyze MSCZ (MuseScore) data files
"""
from lxml import etree
class Mscz:
    """ Class to parse MSCZ (MuseScore) data files """
    Clefs = ["G", "F"]
    def __init__ (self, filepath):
        self.root = etree.parse(filepath)

    def __handle (self, tag, root=None):
        """
        Returns handle pointer to child matching given tag
        """
        if root is None:
            root = self.root
        for child in root.iter():
            if child.tag == tag:
                return child
        return None

    def score (self):
        """
        Returns handle to Score marker
        """
        return self.__handle("Score")

    def part (self):
        """
        Returns hande to Part marker
        """
        return self.__handle("Part", root=self.score())

    def style (self):
        """
        Returns handle to Style marker
        """
        return self.__handle("Style", root=self.score())

    def page_layout (self):
        """
        Returns handle to page layout
        """
        return self.__handle("page-layout", root=self.style())

    def page_geometry (self):
        """
        Returns Page geometry as (Height, Width) tuple
        """
        (height, width) = (None,None)
        for child in self.page_layout():
            if child.tag == "page-height":
                height = float(child.text)
            elif child.tag == "page-width":
                width = float(child.text)
        return (height, width)

    def page_geometry_advanced (self):
        """
        Returns Page geometry as complex dict, with margins
        """
        geo = {}
        (height, width) = self.page_geometry()
        geo['heigth'] = height
        geo['width'] = width
        geo['even'] = {}
        geo['odd'] = {}
        for child in self.__handle("page-margins", root=self.page_layout()):
            print(child.tag)
        return geo

    def __len__ (self):
        """
        Returns number of staffs contained in self
        """
        i = 0
        for child in self.part():
            if child.tag == "Staff":
                i += 1
        return i

    def staff (self, staffid):
        """
        Returns handle to desired track
        """
        for child in self.part():
            if child.tag == "Staff":
                if "id" in child.attribute:
                    if child.attribute["id"] == staffid:
                        return child
        return None

    def total_measures (self):
        """
        Returns total number of measures
        """
        total = 0
        for child in self.score().iter():
            if child.tag == "Measure":
                total += 1
        return total // len(self)
