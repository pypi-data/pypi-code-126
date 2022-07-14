from pathlib import Path

import thriftpy2

cli_thrift = thriftpy2.load(
    str(Path(__file__).parent / "cli.thrift"), module_name="cli_thrift"
)
