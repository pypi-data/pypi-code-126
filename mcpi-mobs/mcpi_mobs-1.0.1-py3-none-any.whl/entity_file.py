import io
import os
from amulet_nbt import *


class DummyFile:
    """
    A dummy file made to work with Amulet_NBT.
    """

    def __init__(self, contents=None):
        """
        Initialize with contents
        """
        self.contents = contents

    def write(self, to_write):
        """
        Replace contents with to_write.
        """
        self.contents = to_write


class EntityFile:
    """
    Wrapper around TextIOWrapper for interacting with entity data files.
    """

    def __init__(self, file_):
        """
        Initialize the file.
        file_ can be anything as long as it provides read(bytes) and the string variable file_.name.
        If the file is empty, a dummy file will be created.
        The NBT data is stored in self.contents, and is a NBTFile, from amulet_nbt. For more information see amulet_nbt's documentation.
        """

        if os.path.getsize(file_.name) == 0:
            self.contents = NBTFile(
                value = TAG_Compound({"Entities": TAG_List([]), "TileEntities": TAG_List([])})

            )
        else:
            self.header_constant = file_.read(8) # Read b"ENT\x00\x01\x00\x00\x00".
            self.header_length = file_.read(4)
            self.contents_raw = file_.read(int.from_bytes(self.header_length, "little"))
            print(self.contents_raw)
            print(self.header_length)
            print(self.header_constant)
            self.contents = load(self.contents_raw, little_endian = True, compressed = False)


    def save(self, file_):
        """
        Saves into the specified file_
        file_ can be anything providing write(data)
        This automatically adds the header.
        """
        header = b"ENT\x00\x01\x00\x00\x00"
        dummy = DummyFile()
        self.contents.save_to(dummy, little_endian = True, compressed = False)
        contents = header + len(dummy.contents).to_bytes(4, "little") + dummy.contents
        file_.write(contents)
