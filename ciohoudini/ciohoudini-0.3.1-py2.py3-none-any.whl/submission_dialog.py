import hou
from PySide2 import QtWidgets
from PySide2 import QtWidgets, QtCore, QtGui

from ciohoudini.validation_tab import ValidationTab
from ciohoudini.progress_tab import ProgressTab
from ciohoudini.response_tab import ResponseTab
from ciohoudini import validation

class SubmissionDialog(QtWidgets.QDialog):

    def __init__(self, nodes, parent=None):
        super(SubmissionDialog, self).__init__(parent)
        self.setWindowTitle("Conductor Submission")
        self.setStyleSheet(hou.qt.styleSheet())
        self.layout = QtWidgets.QVBoxLayout()
        self.tab_widget = QtWidgets.QTabWidget()
        self.setLayout(self.layout)
        self.layout.addWidget(self.tab_widget)

        self.validation_tab = ValidationTab(self)
        self.tab_widget.addTab(self.validation_tab, "Validation")

        self.progress_tab = ProgressTab(self)
        self.tab_widget.addTab(self.progress_tab, "Progress")
 
        self.response_tab = ResponseTab(self)
        self.tab_widget.addTab(self.response_tab, "Response")
        self.setGeometry(300, 200, 1000, 600)
        # self.tab_widget.setTabEnabled(1, False)
        # self.tab_widget.setTabEnabled(2, False)

        self.nodes = nodes

        # self.initUI()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.run()
    
    def run(self):
        errors, warnings, notices =  validation.run(*(self.nodes))
        self.validation_tab.populate(errors, warnings, notices)
        self.progress_tab.populate()
        self.response_tab.populate({"response":"testing"})
        


    # def populate(self, errors, warnings, notices):
    #     pass

    # # @QtCore.pyqtSlot()
    def on_close(self):
        self.accept()




# class ValidationWindow(QtWidgets.QTabWidget):
#     """A Window to display views into the submission.

#     There are 3 tabs. One to show the whole object tree
#     including variables available to the user. The other to
#     show the JSON objects that will be submitted.
#     """

#     def __init__(self, parent=None):
#         QtWidgets.QTabWidget.__init__(self, parent)

#         self.validation = SubmissionTree()
#         self.dry_run = SubmissionDryRun()

#         self.addTab(self.tree, "Tree")
#         self.addTab(self.dry_run, "Dry run")

#         self.setGeometry(300, 200, 1000, 600)

#         self.setWindowTitle("Conductor submission preview")
#         self.setStyleSheet(hou.qt.styleSheet())
 

    # def initUI(self):
    #     endButton = QtWidgets.QPushButton('OK')
    #     endButton.clicked.connect(self.on_clicked)
    #     lay = QtWidgets.QVBoxLayout(self)
    #     lay.addWidget(endButton)
    #     # self.setWindowTitle(str(self.val))
