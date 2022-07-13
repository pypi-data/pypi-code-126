import os
import logging
from ewokscore import Task
import pyopencl
from multianalyzer.app.rebin import rebin_file
from silx.io.h5py_utils import retry, File, safe_top_level_names

from . import dirutils
from .roitools import unscramble_roi_collection

HDF5_PLUGIN_PATH = os.environ.get("HDF5_PLUGIN_PATH")
if HDF5_PLUGIN_PATH:
    del os.environ["HDF5_PLUGIN_PATH"]


logger = logging.getLogger(__name__)


@retry(retry_period=0.5, retry_timeout=30)
def read_data(filename, unscramble_method=None, entries=None, exclude_entries=None):
    res = {}
    with File(filename, mode="r") as fh:
        if entries:
            entries = set(entries)
        else:
            entries = {k for k, v in fh.items() if v.attrs.get("NX_class") == "NXentry"}
        if exclude_entries:
            entries -= set(exclude_entries)
        entries = sorted(entries)
        entries = [entry for entry in entries if entry.endswith(".1")]
        print(f"Reading and unscrambling {len(entries)} entries: {entries}")
        for entry in entries:
            title = entry + "/title"
            if title not in fh:
                continue
            title = fh[title][()]
            try:
                title = title.decode()
            except Exception:
                pass
            if not title.startswith("fscan"):
                continue
            channel_data = {}
            scalar_data = {}
            try:
                entry_grp = fh[entry]
                channel_data["x"] = entry_grp[
                    "instrument/eiger_roi_collection/selection/x"
                ][()]
                channel_data["y"] = entry_grp[
                    "instrument/eiger_roi_collection/selection/y"
                ][()]
                channel_data["roicol"] = entry_grp["measurement/eiger_roi_collection"][
                    ()
                ]
                channel_data["arm"] = entry_grp["measurement/tth"][()]
                channel_data["mon"] = entry_grp["measurement/mon"][()]
                scalar_data["tha"] = entry_grp["instrument/positioners/manom"][()]
                scalar_data["thd"] = entry_grp["instrument/positioners/mantth"][()]
            except KeyError as e:
                logger.warning(str(e))
                continue

            if unscramble_method == "xy":
                keys = "x", "y"
            elif unscramble_method == "yx":
                keys = "y", "x"
            else:
                keys = None

            if keys:
                channel_data = unscramble_roi_collection(channel_data, keys)

                # Check the sorting
                # with File("/users/opid22/test.h5", "w") as fh:
                #    fh["x"] = channel_data["x"]
                #    fh["y"] = channel_data["y"]

            res[entry] = {**channel_data, **scalar_data}
    return res


class ID22Rebin(
    Task,
    input_names=["filename", "parsfile"],
    optional_input_names=[
        "entries",
        "debug",
        "wavelength",
        "energy",
        "step",
        "range",
        "phi",
        "iter",
        "startp",
        "endp",
        "pixel",
        "width",
        "delta2theta",
        "device",
        "outdirs",
        "include_proposal_outdir",
        "outprefix",
        "unscramble_method",
    ],
    output_names=["outfile"],
):
    def run(self):
        outdirs = dirutils.prepare_outdirs(
            self.inputs.outdirs,
            self.inputs.filename,
            self.inputs.include_proposal_outdir,
        )

        options = {
            "pars": self.inputs.parsfile,
            "debug": self.get_input_value("debug", False),
            "wavelength": self.get_input_value("wavelength", None),
            "energy": self.get_input_value("energy", None),
            "step": self.get_input_value("step", None),
            "range": self.get_input_value("range", [0, float("inf")]),
            "phi": self.get_input_value("phi", None),
            "iter": self.get_input_value("iter", None),
            "startp": self.get_input_value("startp", None),
            "endp": self.get_input_value("endp", None),
            "pixel": self.get_input_value("pixel", None),
            "width": self.get_input_value("width", None),
            "delta2theta": self.get_input_value("delta2theta", 0.0),
            "device": self.get_input_value("device", None),
        }

        sdelta2theta = str(options["delta2theta"]).replace(".", "")
        outfilename = (
            os.path.splitext(os.path.basename(self.inputs.filename))[0]
            + f"_w{sdelta2theta}.h5"
        )
        if not self.missing_inputs.outprefix:
            outfilename = self.inputs.outprefix + "_" + outfilename
        outfile = dirutils.primary_file(outfilename, outdirs)
        options["output"] = outfile

        if options["device"] is not None:
            options["device"] = str(options["device"])
        cl_platforms = pyopencl.get_platforms()
        for i, p in enumerate(cl_platforms):
            for j, d in enumerate(p.get_devices()):
                print(f"{i},{j}: {d}")

        filename = self.inputs.filename
        entries = self.get_input_value("entries", None)
        unscramble_method = self.get_input_value("unscramble_method", "xy")
        if True:
            print(f"Unscrambling of ROI collection: {unscramble_method}")
            if os.path.exists(outfile):
                exclude_entries = safe_top_level_names(outfile)
            else:
                exclude_entries = None
            options["hdf5_data"] = read_data(
                filename,
                unscramble_method=unscramble_method,
                entries=entries,
                exclude_entries=exclude_entries,
            )
        else:
            # Let multianalyzer read the data
            options["filename"] = filename
            options["entries"] = entries

        rebin_file(**options)

        dirutils.copy_file(outfilename, outdirs)

        self.outputs.outfile = outfile
