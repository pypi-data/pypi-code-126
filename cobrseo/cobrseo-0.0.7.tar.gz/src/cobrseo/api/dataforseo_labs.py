from urllib.parse import urlparse
import json
import os
import hashlib
import logging
from cobrseo.api.RestClient import RestClient

logger = logging.getLogger(__name__)


def check_kw_in_dir(url, json_name, directory, json_paths_mapped):
    files = [f for f in os.listdir(directory) if os.path.isfile(
        os.path.join(directory, f))]

    if json_name in files:
        json_paths_mapped.append(
            {'url': url, 'path': os.path.join(directory, json_name)})
        return True

    return False


def save_ranked_keywords(
    url: str,
    destination_path: str,
    rewrite: bool,
    token: str,
    lang: str = 'en',
    loc: int = 2840,
):

    destination_path = f'{destination_path}/{lang}/{loc}'
    os.makedirs(destination_path, exist_ok=True)
    json_name = hashlib.md5(url.encode('utf-8')).hexdigest() + '.json'
    json_paths_mapped = list()

    if not rewrite and check_kw_in_dir(url, json_name, destination_path, json_paths_mapped):
        logger.warning(f'Already exists. url = {url}, file = {json_name}.')
        return json_paths_mapped

    client = RestClient(token)

    post_data = dict()

    domain = urlparse(url).netloc
    domain_parts = domain.split('.')
    domain = '.'.join([domain_parts[-2], domain_parts[-1]])
    path = urlparse(url).path

    post_data[len(post_data)] = dict(
        target=domain,
        language_code=lang,
        location_code=loc,
        filters=[
            'ranked_serp_element.serp_item.relative_url',
            '=',
            path
        ],
        order_by=[
            'keyword_data.keyword_info.search_volume,desc'
        ]
    )

    response = client.post(
        '/v3/dataforseo_labs/google/ranked_keywords/live', post_data)
    if response['status_code'] == 20000:
        json_path = os.path.join(destination_path, json_name)
        with open(json_path, 'w') as f:
            json.dump(response['tasks'][0], f)

        json_paths_mapped.append({'url': url, 'path': json_path})
    else:
        logger.error(
            f"GET error. Code: {response['status_code']} Message: {response['status_message']}")
        return json_paths_mapped

    logger.info(f'Saving json... url = {url}, file = {json_path}.')
    return json_paths_mapped
