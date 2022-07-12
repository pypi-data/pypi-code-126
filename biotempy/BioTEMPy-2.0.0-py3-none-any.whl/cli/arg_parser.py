import argparse
import os
import urllib
import tempfile
from TEMPy.protein.structure_parser import PDBParser, mmCIFParser
from TEMPy.maps.map_parser import MapParser


def _is_rcsb_link(path):
    return path.startswith("rcsb:")


def _is_emdb_link(path):
    return path.startswith("emdb:")


def _get_tempfile(filename):
    temp_dir = tempfile.gettempdir()
    return f"/{temp_dir}/{filename}"


def _read_from_rcsb(path):
    pdb_id = path[5:]
    local_file = _get_tempfile(f"rcsb_{pdb_id}.cif")
    if not os.path.isfile(local_file):
        url = f"http://www.rcsb.org/pdb/files/{pdb_id}.cif"
        print(f"Downloading {pdb_id} from RCSB")
        urllib.request.urlretrieve(url, filename=local_file)

    return mmCIFParser.read_mmCIF_file(local_file)


def _read_from_emdb(path):
    emdb_id = path[5:]
    local_file = _get_tempfile(f"emdb_{emdb_id}.mrc.gz")
    if not os.path.isfile(local_file):
        url = f"https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-{emdb_id}/map/emd_{emdb_id}.map.gz"
        print(f"Downloading {emdb_id} from EMDB")
        urllib.request.urlretrieve(url, filename=local_file)

    return MapParser.readMRC(local_file)


def _read_half_map_from_emdb(path, half):
    emdb_id = path[5:]
    local_file = _get_tempfile(f"emdb_{emdb_id}_{half}.mrc.gz")
    if not os.path.isfile(local_file):
        url = f"https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-{emdb_id}/other/emd_{emdb_id}_half_map_{half}.map.gz"
        print(f"Downloading half_map {emdb_id}_{half} from EMDB")
        urllib.request.urlretrieve(url, filename=local_file)

    return MapParser.readMRC(local_file)


def parse_model(path):
    """Given a path or PDB accession tries to return a map.

    Args:
        path (str): A filename or PDB accession in the form of rcsb:1ake
    Returns:
        Map:
    Raise:
        argparse.ArgumentTypeError
    """
    if _is_rcsb_link(path):
        try:
            return _read_from_rcsb(path)
        except Exception:
            raise argparse.ArgumentTypeError(f"Failed to get model with id: {path[5:]}")

    try:
        return PDBParser().read_PDB_file("test", path)
    except Exception:
        pass

    try:
        return mmCIFParser(path).read_mmCIF_file(path)
    except Exception:
        pass

    raise argparse.ArgumentTypeError(f"Failed to read model file: {path}")


def parse_map(path):
    """Given a path or EMDB accession tries to return a map.

    Args:
        path (str): A filename or EMDB accession in the form of emdb:1234
    Returns:
        Map:
    Raise:
        argparse.ArgumentTypeError
    """
    if _is_emdb_link(path):
        try:
            return _read_from_emdb(path)
        except Exception:
            raise argparse.ArgumentTypeError(f"Failed to get map with id: {path[5:]}")
    try:
        return MapParser.readMRC(path)
    except Exception:
        raise argparse.ArgumentTypeError(f"Failed to read map file: {path}")


def _parse_half_map(path, half):
    if _is_emdb_link(path):
        try:
            return _read_half_map_from_emdb(path, half)
        except Exception:
            raise argparse.ArgumentTypeError(f"Failed to get map with id: {path[5:]}")
    try:
        return MapParser.readMRC(path)
    except Exception:
        raise argparse.ArgumentTypeError(f"Failed to read map file: {path}")


def parse_half_map_1(path):
    return _parse_half_map(path, 1)


def parse_half_map_2(path):
    return _parse_half_map(path, 2)


class TEMPyArgParser:
    def __init__(self, script_name):
        self.parser = argparse.ArgumentParser(script_name)
        self.default_group = self.parser.add_argument_group("standard TEMPy arguments")

    def add_model_arg(self):
        self.default_group.add_argument(
            "-p",
            "--pdb",
            help="A model file in PDB, CIF or mmCIF formats. Alternatively, the accession number eg. rcsb:1234",
            dest="model",
            required=True,
            type=parse_model,
        )

    def add_map_arg(self):
        self.default_group.add_argument(
            "-m",
            "--map",
            help="A EM file in MRC format. Alternatively, the accession number eg. emdb:1234",
            dest="map",
            required=True,
            type=parse_map,
        )

    def add_half_map_args(self, required=True):
        self.default_group.add_argument(
            "-hm1",
            "--half-map-1",
            help="A EM half map file in MRC format. Alternatively, the accession number eg. emdb:1234",
            dest="hmap1",
            required=required,
            type=parse_half_map_1,
        )

        self.default_group.add_argument(
            "-hm2",
            "--half-map-2",
            help="A EM half map file in MRC format. Alternatively, the accession number eg. emdb:1234",
            dest="hmap2",
            required=required,
            type=parse_half_map_2,
        )

    def add_resolution_arg(self):
        self.default_group.add_argument(
            "-r",
            "--resolution",
            dest="resolution",
            help="Estimated resolution of EM map",
            required=True,
            type=float,
        )
