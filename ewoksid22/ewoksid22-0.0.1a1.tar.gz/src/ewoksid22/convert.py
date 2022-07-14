from ewokscore import Task
from .h5_to_spec import convert_h5


class ID22H5ToSpec(
    Task,
    input_names=["filename"],
    optional_input_names=[
        "entries",
        "outdirs",
        "include_proposal_outdir",
        "outprefix",
        "retry_timeout",
    ],
    output_names=["specfilenames"],
):
    def run(self):
        entries = self.get_input_value("entries", None)
        outdirs = self.get_input_value("outdirs", None)
        include_proposal_outdir = self.get_input_value("include_proposal_outdir", False)
        retry_timeout = self.get_input_value("retry_timeout", 10)

        self.outputs.specfilenames = convert_h5(
            self.inputs.filename,
            self.inputs.outprefix,
            entries=entries,
            outdirs=outdirs,
            include_proposal_outdir=include_proposal_outdir,
            retry_timeout=retry_timeout,
        )
