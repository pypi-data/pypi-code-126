## P1 Form ID
"""
This workflow action deletes a form by ID.
If the id looks like a URL, it is parsed from
the last segment.
"""
try:
    from accpac import *
except ImportError:
    pass

import base64

from remote_actions.services.fleeting_forms import FormClient
from remote_actions import get_logger

VERSION = '6.0.18'


def workflow(e):
    """Execute the workflow step.

    This function is invoked by the workflow engine.  It is called
    with ``accpac.WorkflowArgs`` and must return ``0`` on success and
    ``1`` on failed.

    :param e: the workflow arguments for this action.
    :type e: ``accpac.WorkflowArgs``
    :returns: 0/1
    :rtype: int
    """

    wiid = e.wi.viworkih.get("WIID")
    if not wiid:
        error("Failed to get workflow ID.")
        return 1

    logger = get_logger("DeleteRemoteActionForm wiid({})".format(wiid))

    _id = e.resolve(e.p1)
    if '/' in _id:
        _id = _id.strip('/').split('/')[-1]

    logger.info("deleting form with id {}".format(_id))

    try:
        client = FormClient()
        client.delete(_id)
    except Exception as e:
        logger.error("error deleting {}: {}".format(_id, e))
        return 1

    return 0
