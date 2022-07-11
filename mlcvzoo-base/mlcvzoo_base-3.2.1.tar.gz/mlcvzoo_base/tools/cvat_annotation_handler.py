import logging

from mlcvzoo_base.data_preparation.cvat_annotation_handler.cvat_annotation_handler import (
    CVATAnnotationHandler,
)
from mlcvzoo_base.tools.logger import Logger

logger = logging.getLogger(__name__)


def main() -> None:

    args = CVATAnnotationHandler.setup_argparse().parse_args()

    Logger.init_logging_basic(
        log_dir=args.log_dir,
        log_file_postfix="CVATAnnotationHandler",
        no_stdout=False,
        root_log_level=args.log_level,
    )

    cvat_annotation_handler = CVATAnnotationHandler()
    cvat_annotation_handler.run()


if __name__ == "__main__":
    main()
