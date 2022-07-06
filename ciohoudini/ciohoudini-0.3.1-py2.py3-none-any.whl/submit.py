"""Handle button presses to submit and test jobs.

preview: Open a window displaying the structure of the submission and
the JSON objects that will be sent to Conductor.

submit: Send jobs to Conductor
"""
import json
import os
import sys
import traceback
import webbrowser

import hou

from ciohoudini import payload
from contextlib import contextmanager
from ciocore import conductor_submit, config
from urllib import parse
from ciohoudini import validation
from ciohoudini.submission_dialog import SubmissionDialog
from PySide2 import QtWidgets
SUCCESS_CODES = [201, 204]


@contextmanager
def saved_scene(node=None):
    """Do stuff in the context of a saved scene.
    
    If the scene has not been modified, yield the filename of the scene.
    Otherwise, prompt to save.
    However, if a node is given and autosave is on, then save as that filename.
    """
    current_scene_name = hou.hipFile.name()
    use_autosave = node and node.parm("use_autosave").eval()
    modified = hou.hipFile.hasUnsavedChanges()

    try:
        fn = None 
        if modified:
            if use_autosave:
                fn = node.parm("autosave_scene").eval()
                try:
                    hou.hipFile.save(file_name=fn, save_to_recent_files=False)
                except hou.OperationFailed:
                    fn = None
            if not fn:
                fn = handle_manual_save()
        else:
            fn = hou.hipFile.path()
            # findFile will raise if the current file was deleted or something
            try:
                hou.findFile(fn)
            except:
                fn = handle_manual_save()
        yield fn

    finally:
        hou.hipFile.setName(current_scene_name)

def invoke_submission_dialog(*nodes, **kwargs):
    """
    Execute the modal submission dialog givebn nodes.
    """
    print("invoke_submission_dialog")

    submission_dialog = SubmissionDialog(nodes)
    hou.session.conductor_validation = submission_dialog
    result = submission_dialog.exec_()


    # errors,     warnings, notices == validation.run(*nodes)
    # print("validated", valid)
    
    # if not valid:
    #     return
    
    # If there is more than one node, don't provide any nodes to the save function, thereby ignoring autosave.
def tmp_submit(node):
    """Submit the given node."""
    
    node = nodes[0] if len(nodes) == 1 else None
    with saved_scene(node) as fn:
        if not fn:
            hou.ui.displayMessage(
                title="Canceled", text="Submission canceled ", severity=hou.severityType.ImportantMessage
            )
            return

        # Now we know all nodes are valid and the scene has been saved 
        results = [ _submit(node) for node in nodes ]
        successes = [result for result in results if result["response_code"] in SUCCESS_CODES]
        failures = [result for result in results if result["response_code"] not in SUCCESS_CODES]
        summary = ""
        buttons=("Close")
        if successes and failures:
            title = "Some successes and some failures"
        elif successes:
            title = "All submissions succeeded"
        elif failures:
            title = "All submissions failed"
        else:
            title = "No submissions"

        url = config.get()["url"]
        if successes:
            buttons=("Close", "Go to dashboard")
            if len(successes) == 1:
                success_uri = successes[0]["response"]["uri"].replace("jobs", "job")
                url = parse.urljoin(url, success_uri)
            summary = "Go to {} to monitor your job(s) on the dashboard?".format(url)
        
        details = []
        for success in successes:
            details.append("Success: {} {}".format(success["node"].name(), success["response"]["uri"]))
        for failure in failures:
            details.append("Failure: {} {} {}".format(failure["node"].name(), failure["response_code"], failure["response"]))
        details = "\n\n".join(details)

        result = hou.ui.displayMessage(
            title=title,
            text=summary,
            details_label="Submission details",
            details=details,
            buttons=buttons,
            severity=hou.severityType.Message,
        )

        if result == 1:
            webbrowser.open_new(url)

def get_submission_payload(node):
    """Get the submission payload for the given node."""
    kwargs = {}
    kwargs["do_asset_scan"] = True
    kwargs["task_limit"] = -1
    submission_payload = payload.resolve_payload(node, **kwargs)
    return submission_payload

def _submit(node):
    payload = get_submission_payload(node)
    remote_job = conductor_submit.Submit(payload)
    response, response_code = remote_job.main()
    return {"response": response, "response_code": response_code, "node": node}
 
def handle_manual_save():
    """Manual save-scene flow."""

    fn = hou.ui.selectFile(
        start_directory=os.path.dirname(hou.hipFile.path()),
        title="Save for Conductor submit",
        file_type=hou.fileType.Hip,
        pattern="*.hip,*.hiplc,*.hipnc,*.hip*",
        default_value=hou.hipFile.basename(),
        chooser_mode=hou.fileChooserMode.Write,
    )
    if fn:
        try:
            hou.hipFile.save(file_name=fn)
        except hou.OperationFailed:
            fn = None
    return fn
