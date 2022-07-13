"""Convert an HDF5 file to a SPEC .dat file
"""

import os
import io
import logging

import numpy
from scipy.interpolate import interp1d
from silx.io.h5py_utils import retry, File

from . import dirutils
from . import specutils

logger = logging.getLogger(__name__)


def convert_h5(
    filename,
    outprefix=None,
    entries=None,
    outdirs=None,
    include_proposal_outdir=False,
    retry_timeout=10,
):
    """
    :param str filename: full path of the Nexus file
    :param str outprefix: something unique to the proposal/session
    :param list entries: for example ["1.1", "1.2", ...]
    :param dict outdirs:
    :param bool include_proposal_outdir:
    :returns dict:
    """
    filename = os.path.abspath(filename)
    outdirs = dirutils.prepare_outdirs(outdirs, filename, include_proposal_outdir)
    if "primary" not in outdirs:
        logger.warning("No primary output directory: not saving anything")
        return

    if entries:
        names = {}
        for name in entries:
            scannr = int(name.split(".")[0])
            names.setdefault(scannr, []).append(name)
    else:
        names = get_scan_names(filename, retry_timeout=retry_timeout)
    if not names:
        logger.warning("no scans to convert")
        return

    motor_names = [
        ["tth", "om", "manom", "mantth", "mantr", "Dh", "Dhd"],
        ["Dhm", "Dhu", "spinp", "bluspin", "t1h", "t1h1", "t1h2", "t1x"],
        ["t1y", "t1rz", "t1trans", "robtran", "s3vg", "s3vo", "s3hg", "s3ho"],
        ["s4vg", "s4vo", "s4hg", "s4ho", "u26b", "chi"],
        ["d2dtran", "Dy", "Dyu", "Dyd", "Drx", "Dry"],
        ["mos", "rst", "rsg", "redtrans"],
        ["xtrans", "ytrans", "ztrans", "gasspin", "DET_Z", "DET_X", "DET_Y", "DET_RZ"],
    ]

    # Save SPEC header when no scans have been saved yet
    spec_filename = os.path.splitext(os.path.basename(filename))[0] + ".dat"
    if outprefix:
        spec_filename = outprefix + "_" + spec_filename

    saved = saved_scan_numbers(spec_filename, outdirs)
    if not saved:
        first_scan = sorted(names.items())[0][1][0]
        specdata = read_spec_header(
            filename, first_scan, motor_names, retry_timeout=retry_timeout
        )
        add_to_specfile(spec_filename, specdata, outdirs)

    # Save scans
    first_error = None
    for scannr, subscans in sorted(names.items()):
        if scannr in saved:
            # fscan already saved
            continue
        if len(subscans) != 2:
            # incomplete fscan
            continue
        # fscan with 2 complete subscans
        subscan1, subscan2 = subscans
        try:
            specdata = read_fscan_data(
                filename, subscan1, subscan2, motor_names, retry_timeout=retry_timeout
            )
        except Exception as e:
            if first_error is None:
                first_error = e
            continue
        add_to_specfile(spec_filename, specdata, outdirs)

    dirutils.copy_file(spec_filename, outdirs)

    if first_error is not None:
        raise first_error

    return sorted(
        f"{userhost}@{dirname}" if userhost else dirname
        for (userhost, dirname) in outdirs.values()
    )


@retry()
def get_scan_names(filename, title=None):
    """Get the subscan names for all scans in the Nexus file

    :param str filename:
    :param str title:id22
    :returns dict: scannr(int)->subscan_names(list)
    """
    with File(filename, mode="r") as h5file:
        names = list(h5file["/"])

        def include(name):
            try:
                scan = h5file[name]
            except Exception as e:
                logger.warning(
                    "cannot read scan " + repr(name) + " (cause: " + str(e) + ")"
                )
                return False
            if "end_time" not in scan:
                return False
            if "measurement" not in scan:
                return False
            if title:
                stitle = str_from_dataset(scan["title"])
                if not any(s in stitle for s in ["fscan", "f2scan"]):
                    return False
            return True

        scans = dict()
        for name in names:
            if include(name):
                scannr = int(float(name))
                scans.setdefault(scannr, []).append(name)

        return scans


def saved_scan_numbers(filename, outdirs):
    """Scans saved in the SPEC file.

    :param str filename:
    :param dict outdirs:
    :returns list(int):
    """
    local_filename = dirutils.primary_file(filename, outdirs)
    return specutils.saved_scan_numbers(local_filename)


def add_to_specfile(spec_filename, specdata, outdirs):
    """
    :param str spec_filename:
    :param list(2-tuple) specdata:
    :param dict outdirs:
    """
    if not outdirs:
        return
    local_filename = os.path.join(outdirs["primary"][1], spec_filename)
    dirname = os.path.dirname(local_filename)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    for mode, lines in specdata:
        with open(local_filename, mode) as f:
            f.writelines(lines)


def str_from_dataset(dataset):
    """Read dataset as a string

    :param h5py.Dataset dataset:
    :returns str:
    """
    if isinstance(dataset, str):
        return dataset
    if dataset is None:
        return "UNKNOWN"
    try:
        return dataset.asstr()[()]
    except (AttributeError, TypeError):
        return str(dataset[()])


def read_position(grp, key, fmt, modif=None):
    """Read a motor position from grp[key], return "-999" when missing.

    :param h5py.Group grp:
    :param str key:
    :param callable or None modif:
    :returns str:
    """
    if key in grp:
        pos = grp[key][()]
        if pos == "*DIS*":
            return str(-999)
        try:
            num = float(fmt.format(pos))
        except Exception as e:
            raise RuntimeError("Error in formatting motor position " + repr(key)) from e
        if modif:
            num = modif(num)
        return str(num)
    return str(-999)


@retry()
def read_spec_header(filename, first_scan, motor_names):
    """
    :param str filename:h5_to_spec_v5.py
    :param str first_scan:
    :param list(str) motor_names:
    :returns list(2-tuple):
    """
    with File(filename, mode="r") as h5file:
        start_time = str_from_dataset(h5file[first_scan]["start_time"])

    specdata = []
    lines = []
    specdata.append(("w", lines))

    lines.append("#F " + '"' + filename + '"' + "\n")
    lines.append("#D " + start_time + "\n")
    lines.append("#C exp  User = opid22" + "\n")
    lines.append("" + "\n")
    for i, names in enumerate(motor_names):
        lines.append("#o{} ".format(i) + " ".join(names) + "\n")
    lines.append("\n")
    return specdata


@retry()
def read_fscan_data(filename, subscan1, subscan2, motor_names):
    """
    :param str filename:
    :param str subscan1:
    :param str subscan2:
    :param list(str) motor_names:
    :returns list(2-tuple):
    """
    with File(filename, mode="r") as h5file:
        subscan1 = h5file[subscan1]
        subscan2 = h5file[subscan2]
        return _read_fscan_data(subscan1, subscan2, motor_names)


def min_npts_ctrs(group, ctrs):
    """Smallest number of points of a group of datasets.

    :param h5py.Group group:
    :param list(2-tuple) ctrs:
    :returns int:
    """
    npts = []
    for name, must_exist in ctrs:
        try:
            dset = group[name]
        except KeyError:
            if must_exist:
                raise
        else:
            npts.append(len(dset))
    return min(npts)


def read_ctrs(group, ctrs, npts):
    """Read datasets

    :param h5py.Group group:
    :param list(2-tuple) ctrs:
    :param int npts:
    :yield numpy.ndarray:
    """
    for i, (name, must_exist) in enumerate(ctrs):
        try:
            dset = group[name]
        except KeyError:
            if must_exist:
                raise
        else:
            try:
                data = dset[:npts]
            except Exception as e:
                logger.warning(
                    "skip counter data " + repr(name) + " (cause: " + str(e) + ")"
                )
            else:
                if not len(data):
                    logger.warning("no data in " + repr(name))
                    continue
                yield i, data


def _read_fscan_data(subscan1, subscan2, motor_names):
    """
    :param h5py.Group subscan1:
    :param h5py.Group subscan2:
    :param list(str) motor_names:
    :returns list(2-tuple):
    """
    specdata = []

    fast_data = subscan1["measurement"]
    slow_data = subscan2["measurement"]
    fscan_params = subscan1["instrument/fscan_parameters"]
    positioners_start = subscan1["instrument/positioners_start"]
    try:
        machine = subscan1["instrument/machine"]
    except KeyError:
        machine = {}
    try:
        robot = subscan1["instrument/robot"]
    except KeyError:
        robot = {}

    # Scan parameters
    scannr = subscan1.name[1:].split(".")[0]
    start_time = str_from_dataset(subscan1["start_time"])
    start_pos = float(fscan_params["start_pos"][()])
    step = float(fscan_params["step_size"][()])
    no_scan_points = float(fscan_params["npoints"][()])
    acq_time = float(fscan_params["acq_time"][()])
    end_pos = "{:.2f}".format(start_pos + step * no_scan_points)
    deg_per_min = "{:.2f}".format(step / acq_time * 60)

    # Scan header
    lines = []
    specdata.append(("a", lines))

    lines.append(
        "#S  "
        + scannr
        + "  hookscan "
        + str_from_dataset(fscan_params["motor"])
        + " "
        + read_position(fscan_params, "start_pos", "{:.2f}")
        + " "
        + end_pos
        + " "
        + deg_per_min
        + " "
        + read_position(fscan_params, "acq_time", "{:.5f}", modif=lambda x: x * 1000)
        + " "
        + "\n"
    )
    lines.append("#D " + start_time + "\n")
    lines.append(
        "#T " + read_position(fscan_params, "acq_time", "{:.5f}") + " (Seconds)\n"
    )
    lines.append("#Q \n")

    for i, names in enumerate(motor_names):
        positions = " ".join(
            [read_position(positioners_start, name, "{:.4f}") for name in names]
        )
        lines.append("#P{} ".format(i) + positions + "\n")

    lines.append("#UMI0    Current     AutoM      Shutter      U26B_GAP     \n")
    lines.append(
        "#UMI1"
        + " "
        + read_position(machine, "current", "{:.4f}")
        + " "
        + str_from_dataset(machine.get("automatic_mode"))
        + " "
        + str_from_dataset(machine.get("front_end"))
        + " "
        + read_position(positioners_start, "u26b", "{:.4f}")
        + "\n"
    )

    lines.append(
        "#UMI2"
        + " Refill in "
        + str_from_dataset(machine.get("refill_countdown"))
        + " sec,"
        + " Fill Mode: "
        + str_from_dataset(machine.get("mode"))
        + ","
        + " Op. Message: "
        + str_from_dataset(machine.get("message"))
        + "\n"
    )

    lines.append(
        "#CR"
        + " Last robot sample loaded: "
        + str_from_dataset(robot.get("sample_label"))
        + "\n"
    )

    # Slow counters
    slow_ctrs_spec = [
        "blowerT",
        "Cryostream",
        "Cryostat",
        "Press_in",
        "Press_out",
        "monin",
        "bmon",
    ]
    slow_ctrs_fmt = ["%4.3f", "%4.3f", "%4.3f", "%7.4f", "%7.4f", "%.5e", "%.5e"]
    slow_ctrs = [
        ("epoch", True),  # not saved, used as X for interpolation
        ("blower_input", False),
        ("ox700_input", False),
        ("ls340_input", False),
        ("pace_press_input", False),
        ("pace_press_output", False),
        ("monin", False),
        ("bmon", False),
    ]
    nslow_ctrs = len(slow_ctrs_spec)
    npts_slow = min_npts_ctrs(slow_data, slow_ctrs)

    # Fast counters
    if "eiger" in fast_data:
        prefix = "eiger_roi"
        channels = 13
    else:
        prefix = "ma"
        channels = 9

    fast_ctrs_spec = (
        ["2_theta"]
        + ["MA{}".format(i) for i in range(channels)]
        + ["Monitor", "Epoch", "Omega"]
    )
    fast_ctrs_fmt = ["%3.8f"] + ["%i"] * channels + ["%i", "%15.8f", "%3.8f"]

    # fast_ctrs = ["tth"] + [prefix + str(i) for i in range(channels)] + ["mon", "epoch_trig"]
    fast_ctrs1 = (
        ["tth"] + [prefix + str(i) for i in range(channels)] + ["mon", "epoch_trig"]
    )
    ixfast = fast_ctrs1.index("epoch_trig")
    fast_ctrs2 = ["om"]
    fast_ctrs1 = [(name, True) for name in fast_ctrs1]
    fast_ctrs2 = [(name, False) for name in fast_ctrs2]
    fast_ctrs = fast_ctrs1 + fast_ctrs2
    # print(fast_ctrs)

    nfast_ctrs = len(fast_ctrs_spec)
    npts_fast = min_npts_ctrs(fast_data, fast_ctrs)

    # Prepare data
    nctrs = nfast_ctrs + nslow_ctrs
    data = numpy.zeros((npts_fast, nctrs))
    ctrs_spec = fast_ctrs_spec + slow_ctrs_spec
    ctrs_fmt = fast_ctrs_fmt + slow_ctrs_fmt

    # Read fast data
    for i, idata in read_ctrs(fast_data, fast_ctrs, npts_fast):
        data[:, i] = idata

    # Read slow data + interpolate at fast epoch
    xfast = data[:, ixfast]
    xslow = None
    slowoff = len(fast_ctrs)
    for i, idata in read_ctrs(slow_data, slow_ctrs, npts_slow):
        if i:
            func = interp1d(xslow, idata, kind="nearest", fill_value="extrapolate")
            try:
                data[:, slowoff + i - 1] = func(xfast)
            except Exception:
                pass
        else:
            xslow = idata

    # Scan data header
    lines = []
    specdata.append(("a", lines))
    lines.append("#N {}\n".format(nctrs))
    lines.append("#L  " + "  ".join(ctrs_spec) + "\n")

    # Scan data
    lines = []
    specdata.append(("ab", lines))
    f = io.BytesIO()
    numpy.savetxt(f, data, delimiter=" ", fmt=" ".join(ctrs_fmt))
    lines.append(f.getbuffer())
    lines.append(b"\n")

    return specdata
