import json
from typing import List, Tuple
import logging

logger = logging.getLogger(__name__)


def read_json(json_path: str) -> dict:
    """
    Reads given json.

    Args:
        json_path (str): Json file path.

    Returns:
        dict: Data from json file.
    """
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)

    except Exception as e:
        logger.exception(f'File [{json_path}].', exc_info=e)
        raise

    logger.debug(f'File [{json_path}] was read successfully.')

    return data


def get_ranked_keywords(json_path: str) -> List[Tuple[str, float]]:

    data = read_json(json_path)

    ranked_keywords = list()
    try:
        for kw in data['result'][0]['items']:
            ranked_keywords.append(
                (kw['keyword_data']['keyword'], kw['ranked_serp_element']['serp_item']['etv']))

    except TypeError:
        logger.warning(f'File [{json_path}]. No ranked keywords found.')
        return ranked_keywords

    ranked_keywords.sort(key=lambda x: x[1], reverse=True)
    logger.debug(
        f'File [{json_path}]. Found {len(ranked_keywords)} ranked_keywords.')
    return ranked_keywords
