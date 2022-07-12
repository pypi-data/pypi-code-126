# Copyright 2021 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from flask_babel import lazy_gettext as _l
from flask_login import current_user

import kadi.lib.constants as const
from kadi.ext.db import db
from kadi.lib.db import escape_like
from kadi.lib.licenses.models import License
from kadi.lib.permissions.core import get_permitted_objects
from kadi.lib.tags.models import Tag
from kadi.lib.web import url_for
from kadi.modules.collections.models import Collection
from kadi.modules.collections.schemas import CollectionSchema
from kadi.modules.groups.models import Group
from kadi.modules.groups.schemas import GroupSchema
from kadi.modules.groups.utils import get_user_groups
from kadi.modules.records.models import Record
from kadi.modules.records.schemas import RecordSchema
from kadi.modules.templates.models import Template
from kadi.modules.templates.schemas import TemplateSchema


def get_tags(filter_term="", resource_type=None, user=None):
    """Get all distinct tags of resources a user can access.

    :param filter_term: (optional) A (case insensitive) term to filter the tags by their
        name.
    :param resource_type: (optional) A resource type to limit the tags to. One of
        ``"record"`` or ``"collection"``.
    :param user: (optional) The user that will be checked for access permissions.
        Defaults to the current user.
    :return: The tags as query, ordered by their name in ascending order.
    """
    user = user if user is not None else current_user

    tag_queries = []

    if resource_type == "record":
        models = [Record]
    elif resource_type == "collection":
        models = [Collection]
    else:
        models = [Record, Collection]

    for model in models:
        tags_query = Tag.query.join(model.tags).filter(
            model.state == const.MODEL_STATE_ACTIVE,
            model.id.in_(
                get_permitted_objects(user, "read", model.__tablename__).with_entities(
                    model.id
                )
            ),
        )
        tag_queries.append(tags_query)

    tags_query = (
        tag_queries[0]
        .union(*tag_queries[1:])
        .filter(Tag.name.ilike(f"%{escape_like(filter_term)}%"))
        .distinct()
        .order_by(Tag.name)
    )

    return tags_query


def get_licenses(filter_term=""):
    """Get all licenses.

    :param filter_term: (optional) A (case insensitive) term to filter the licenses by
        their title or name.
    :return: The licenses as query, ordered by their title in ascending order.
    """
    return License.query.filter(
        db.or_(
            License.title.ilike(f"%{escape_like(filter_term)}%"),
            License.name.ilike(f"%{escape_like(filter_term)}%"),
        )
    ).order_by(License.title)


_RESOURCE_TYPES = {
    "record": {
        "title": _l("Records"),
        "model": Record,
        "schema": RecordSchema,
        "endpoint": "records.records",
    },
    "collection": {
        "title": _l("Collections"),
        "model": Collection,
        "schema": CollectionSchema,
        "endpoint": "collections.collections",
    },
    "template": {
        "title": _l("Templates"),
        "model": Template,
        "schema": TemplateSchema,
        "endpoint": "templates.templates",
    },
    "group": {
        "title": _l("Groups"),
        "model": Group,
        "schema": GroupSchema,
        "endpoint": "groups.groups",
    },
}


def _get_resource_data(resource_config, user):
    resource_type = resource_config["resource"]
    resource_type_meta = _RESOURCE_TYPES[resource_type]

    model = resource_type_meta["model"]
    schema = resource_type_meta["schema"]

    endpoint_args = {}

    if resource_config["creator"] == "any":
        # Only include groups with membership in this case.
        if resource_type == "group":
            resources_query = get_user_groups(user)
            endpoint_args["member_only"] = True
        else:
            resources_query = get_permitted_objects(user, "read", resource_type)
    else:
        resources_query = model.query.filter(model.user_id == user.id)
        endpoint_args["user"] = user.id

    if resource_config["visibility"] != "all":
        resources_query = resources_query.filter(
            model.visibility == resource_config["visibility"]
        )
        endpoint_args["visibility"] = resource_config["visibility"]

    resources = (
        resources_query.filter(model.state == const.MODEL_STATE_ACTIVE)
        .order_by(model.last_modified.desc())
        .limit(resource_config["max_items"])
        .all()
    )

    if not resources:
        return None

    return {
        "title": str(resource_type_meta["title"]),
        "url": url_for(resource_type_meta["endpoint"], **endpoint_args),
        "items": schema(many=True, _internal=True).dump(resources),
    }


def get_home_page_resources(user=None):
    """Get a list of serialized resources according to the configured home page layout.

    Uses the home page layout as configured via the user-specific ``"HOME_LAYOUT"``
    config item.

    :param: (user) The user the layout belongs to. Defaults to the current user.
    :return: The serialized resources as a list of dictionaries per resource type, each
        containing the localized resource title (``"title"``), the resource search url
        (``"url"``) and the serialized resources themselves (``"items"``).
    """
    user = user if user is not None else current_user

    home_layout = user.get_config(
        const.USER_CONFIG_HOME_LAYOUT, default=const.USER_CONFIG_HOME_LAYOUT_DEFAULT
    )
    resources = []

    for resource_config in home_layout:
        resource_data = _get_resource_data(resource_config, user)

        if resource_data is not None:
            resources.append(resource_data)

    return resources
