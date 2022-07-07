#!/usr/bin/env python

__version__ = '0.0.0'

from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Set

from .api import Stream, StreamPages, format_response_replication, format_response_sub_stream, main

CONFIG_KEYS_REQUIRED: Set[str] = {
    'endpoint',
    'access_token'
}


def set_streams() -> Dict:
    utcnow: datetime = datetime.now(timezone.utc)
    return {
        # NOTE: Full Paginated API Responses
        'people': StreamPages(
            'people', key_properties=['id'], replication_method='FULL_TABLE',
            # format_response_function=lambda response, params: [r for i in response for r in i.get(params.get('path'), {}).values()],
            format_response_function=format_response_replication,
            format_response_params={'path': 'people'},
            params={'offset_key': 'offset', 'limit_key': 'limit', 'filters': {
                'limit': 20,  # NOTE: 20 responses are returned by default, but the maximum value is 500
                'included_deleted': 'true'}}),

        # NOTE: Full Non-Paginated API Responses
        'agent_states': Stream(
            'agent_states', key_properties=['agent_import_id'], replication_method='FULL_TABLE',
            parent={'tap_stream_id': 'people', 'key_properties': ['agent_id']},
            format_response_function=format_response_sub_stream,
            format_response_params={'path': 'agent_states'},
            params={'url': 'agents/{agent_id}/state', 'ignore_status': [404]}),

        'activity_types': Stream(
            'activity_types', key_properties=['id'], replication_method='FULL_TABLE',
            format_response_function=format_response_replication,
            format_response_params={'path': 'activity_types'}),

        'activities': Stream(
            'activities', key_properties=['id'], replication_method='FULL_TABLE',
            format_response_function=format_response_replication,
            format_response_params={'path': 'activities'},
            params={'filters': {'start_time': 0, 'end_time': int(utcnow.timestamp())}}),

        'requirement_types': Stream(
            'requirement_types', key_properties=['id'], replication_method='FULL_TABLE',
            format_response_function=format_response_replication,
            format_response_params={'path': 'requirement_types'}),

        # NOTE: Incremental Non-Paginated API Responses
        'queues': Stream(
            'queues', key_properties=['id'], replication_method='INCREMENTAL', replication_key='updated_at',
            format_response_function=format_response_replication,
            format_response_params={'path': 'queues'}),
        'sites': Stream(
            'sites', key_properties=['id'], replication_method='INCREMENTAL', replication_key='updated_at',
            format_response_function=format_response_replication,
            format_response_params={'path': 'sites'}),
        'teams': Stream(
            'teams', key_properties=['id'], replication_method='INCREMENTAL', replication_key='updated_at',
            format_response_function=format_response_replication,
            format_response_params={'path': 'teams'}),
        'skills': Stream(
            'skills', key_properties=['id'], replication_method='INCREMENTAL', replication_key='updated_at',
            format_response_function=format_response_replication,
            format_response_params={'path': 'skills'}),

        # NOTE: Incremental Non-Paginated API Responses - Reports
        'forecasts': Stream(
            'forecasts', key_properties=['id'], replication_method='FULL_TABLE',
            format_response_function=format_response_replication,
            format_response_params={'path': 'forecasts'},
            params={'filters': {
                    'start_time': int(utcnow.timestamp()) - (28 * 24 * 60 * 60),
                    'end_time': int(utcnow.timestamp()),
                    'channel': 'chat'}}),
        'reports_adherence': Stream(
            'reports_adherence', replication_method='FULL_TABLE',
            key_properties=['start_time', 'end_time', 'interval', 'channel', 'queue_id', 'agent_id'],
            format_response_function=format_response_replication,
            format_response_params={'path': 'adherence'},
            params={
                'url': 'reports/adherence',
                'filters': {
                    'start_time': int(utcnow.timestamp()) - (28 * 24 * 60 * 60),
                    'end_time': int(utcnow.timestamp()),
                    'interval': '1w',
                    'channel': 'chat'}}),
    }


if __name__ == '__main__':
    main(schemas_dir=Path(__file__).parent / 'schemas', set_streams=set_streams, config_keys_required=CONFIG_KEYS_REQUIRED)
