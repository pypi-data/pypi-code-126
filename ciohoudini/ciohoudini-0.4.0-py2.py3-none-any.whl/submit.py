"""Handle button presses to submit and test jobs.

preview: Open a window displaying the structure of the submission and
the JSON objects that will be sent to Conductor.

submit: Send jobs to Conductor
"""
import os
import traceback

import hou

from ciohoudini import payload
from contextlib import contextmanager
from ciocore import conductor_submit
from ciohoudini.submission_dialog import SubmissionDialog
SUCCESS_CODES = [201, 204]


@contextmanager
def saved_scene(node=None):
    """Do stuff in the context of a saved scene.
    
    If the scene has not been modified, yield the filename of the scene.
    Otherwise, prompt to save.
    However, if a node is given and autosave is on, then save as that filename.
    """
    current_scene_name = hou.hipFile.name()
    always_use_autosave = node and node.parm("use_autosave").eval()
    modified = hou.hipFile.hasUnsavedChanges()

    try:
        fn = None 
        if modified or always_use_autosave:
            fn = node.parm("autosave_scene").eval()
            hou.hipFile.save(file_name=fn, save_to_recent_files=False)
        else:
            fn = hou.hipFile.path()
            # findFile will raise if the current file was dele ted or something
            hou.findFile(fn)
        yield fn
    finally:
        hou.hipFile.setName(current_scene_name)

def invoke_submission_dialog(*nodes, **kwargs):
    """
    Execute the modal submission dialog givebn nodes.
    """

    submission_dialog = SubmissionDialog(nodes)
    hou.session.conductor_validation = submission_dialog
    result = submission_dialog.exec_()
    
# If there is more than one node, don't provide any nodes to the save function, thereby ignoring autosave.
def run(*nodes):
    """Submit the given node."""
    
    result = []
    if not nodes:
        return result
    first_node = nodes[0]
    with saved_scene(first_node) as fn:
        if not fn:
            return result

        # Now we know all nodes are valid and the scene has been saved 
        return [ submit_one(node) for node in nodes ]


def get_submission_payload(node):
    """Get the submission payload for the given node."""
    kwargs = {}
    kwargs["do_asset_scan"] = True
    kwargs["task_limit"] = -1
    submission_payload = payload.resolve_payload(node, **kwargs)
    return submission_payload

def submit_one(node):
    try:
        payload = get_submission_payload(node)
        remote_job = conductor_submit.Submit(payload)
        response, response_code = remote_job.main()
    except:
        response = traceback.format_exc()
        response_code = 500
    return {"response": response, "response_code": response_code, "node": node}
 