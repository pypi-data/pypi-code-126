import logging

from cobrseo.api.dataforseo_organic import save_dataforseo_organic_serps
from cobrseo.api.dataforseo_labs import save_ranked_keywords
from cobrseo.json.serp_processing import get_organic_info
from cobrseo.json.labs_processing import get_ranked_keywords

logger = logging.getLogger(__name__)


def get_parent_keywords(
    keywords: list,
    token: str,
    serp_dir: str,
    ranked_dir: str,
    rewrite: bool,
    lang: str,
    loc: int
) -> dict:
    """Returns parent keywords.

    Args:
        keywords (list): List of keywords to find parent keywords for
        token (str): DataForSeo API_KEY
        serp_dir (str): Directory with serps
        ranked_dir (str): Directory with ranked keywords
        rewrite (bool): Rewrite existing DataForSeo results
        lang (str): DataForSeo lang parameter
        loc (int): DataForSeo loc parameter

    Returns:
        dict: Dict with parent keywords
    """
    logger.debug('Getting serps...')
    all_serps = save_dataforseo_organic_serps(keywords,
                                              lang=lang,
                                              loc=loc,
                                              destination_path=serp_dir,
                                              token=token,
                                              rewrite_serp=rewrite)

    parent_keywords_dict = dict()
    for serp in all_serps:
        organic_info = get_organic_info(serp['path'])
        child_keyword = serp['keyword']
        logger.debug(f'Processing [{child_keyword}]...')
        try:
            first_url = list(organic_info.values())[0]['url']
        except IndexError:
            logger.warning(
                f'No first url found in serp for [{child_keyword}] child keyword. Parent keyword = None.')
            parent_keywords_dict[child_keyword] = None
            continue

        logger.debug(f'Getting ranked keywords from first url...')
        ranked_keywords_json = save_ranked_keywords(
            url=first_url,
            destination_path=ranked_dir,
            rewrite=rewrite,
            token=token,
            lang=lang,
            loc=loc
        )

        ranked_keywords = get_ranked_keywords(ranked_keywords_json[0]['path'])

        try:
            parent_keyword = ranked_keywords[0][0]
            logger.info(f'"{child_keyword}" : "{parent_keyword}"')
        except IndexError:
            logger.warning(
                f'No ranked keywords found for [{child_keyword}] child keyword. Parent keyword = None.')
            parent_keywords_dict[child_keyword] = None
            continue

        parent_keywords_dict[child_keyword] = parent_keyword

    return parent_keywords_dict
