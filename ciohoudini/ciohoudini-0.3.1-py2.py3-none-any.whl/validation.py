import os
import hou
import sys
from ciopath.gpath import Path
from ciopath.gpath_list import GLOBBABLE_REGEX, PathList
from ciocore.validator import ValidationError, Validator

from ciocore import data as coredata


DASHES = "-" * 30

class ValidateUploadDaemon(Validator):
    def run(self, _):
        node = self._submitter
        use_daemon = node.parm("use_daemon").eval()
        if not use_daemon:
            return

        msg = "This submission expects an uploader daemon to be running.\n"
        msg += 'After you press submit you can open a shell and type:\nconductor uploader'

        location = node.parm("location_tag").eval().strip()
        if location:
            msg = "This submission expects an uploader daemon to be running and set to a specific location tag."
            msg += 'After you press submit you can open a shell and type:\nnconductor uploader --location "{}"\n'.format(
                location
            )
        self.add_notice(msg)


class ValidateTaskCount(Validator):
    def run(self, _):
        node = self._submitter
        tasks = node.parm("frame_task_county").eval()
        if tasks > 2000:
            self.add_error(
                "This submission contains over 1000 tasks ({}). You'll need to either increase chunk_size or send several job?".format(
                    tasks
                )
            )

 
class ValidateScoutFrames(Validator):
    def run(self, _):
        """
        Add a validation warning for a potentially costly scout frame configuration.
        """
        node = self._submitter
        scout_count = node.parm("scout_frame_task_countx").eval()
        frame_count = node.parm("frame_task_countx").eval()

        if frame_count < 5:
            return

        if scout_count < 5 and scout_count > 0:
            return

        if scout_count == 0 or scout_count == frame_count:
            msg = "All tasks will start rendering."
            msg += " To avoid unexpected costs, we strongly advise you to configure scout frames so that most tasks are initially put on hold. This allows you to check a subset of frames and estimate costs before you commit a whole sequence."
            self.add_warning(msg)

        if  node.parm("chunk_size").eval() > 1:
            msg = "You have chunking set higher than 1."
            msg += " This can cause more scout frames to be rendered than you might expect. ({} scout frames).".format(
                scout_count
            )
            self.add_warning(msg)


# Implement more validators here
####################################
####################################


def run(*nodes):
    print("validation.run", nodes)
    errors, warnings, notices = [], [], []
    for node  in nodes:
        er, wn, nt = _run_validators(node)
        
        errors.extend(er)
        warnings.extend(wn)
        notices.extend(nt)
    print(errors)
    print(warnings)
    print(notices)
    
    errors, warnings, notices = _run_validators(node)
    title = "Validation"
    if errors:
        title = "Some errors would cause the submission to fail. Submission is onot possible in this state.\n\n{}\n"
    elif warnings:
        title = "Some issues could cause the submission to fail or incur extra costs. Please carefully check the warnings below.\n\n{}\n"
    elif notices:
        title = "Some information could be useful for the submission. Please carefully check the notices below.\n\n{}\n"
    
    return errors, warnings, notices

    # for issue in errors + warnings + notices:
    #     print(issue)

    # # Code to display the issues and ask the user whether to continue with the submission.

    # submission_dialog = SubmissionDialog()
    # submission_dialog.populate(errors, warnings, notices)
    # # submission_dialog.show()
    # hou.session.conductor_validation = submission_dialog
    # if submission_dialog.exec_() == QtWidgets.QDialog.Accepted:
    #     print(submission_dialog.val)
    # return False
 

def _run_validators(node):

    takename =  node.name()
    validators = [plugin(node) for plugin in Validator.plugins()]
    for validator in validators:
        validator.run(takename)

    errors = list(set.union(*[validator.errors for validator in validators]))
    warnings = list(set.union(*[validator.warnings for validator in validators]))
    notices = list(set.union(*[validator.notices for validator in validators]))
    return errors, warnings, notices
