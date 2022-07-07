import logging

import pandas as pd

logger = logging.getLogger(__name__)


def xml_to_df(xml: bytes, xpath: str) -> pd.DataFrame:
    try:
        df = pd.read_xml(path_or_buffer=xml, xpath=xpath, parser="etree")
    except ValueError as e:
        # check for no match
        if "xpath does not return any nodes" in str(e):
            logger.warning("xpath did not return any nodes")
            return pd.DataFrame()
        else:
            raise
    return df
