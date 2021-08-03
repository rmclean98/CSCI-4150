from PyQt5.QtWidgets import QCheckBox

from ImportFile import *
from Home import Home
from SetTransformation import SetTransformation

class SetTransformUI(QWidget):

    # Creates UI elements
    def __init__(self, parent=None):
        super(SetTransformUI, self).__init__(parent)
        self.txtFile = QLineEdit()
        self.file_button = QPushButton('Browse file 1')
        self.txtFile2 = QLineEdit()
        self.file_button2 = QPushButton('Browse file 2')
        self.ok_button = QPushButton('Apply')
        self.cancel_button = QPushButton('cancel')
        self.union_check = QCheckBox('Union')
        self.intersection_check = QCheckBox('Intersection')
        self.difference_check = QCheckBox('Difference')
        self.complement_check = QCheckBox('Complement')
        self.switch = QCheckBox('Switch Images Paths')
        self.imgSize = QLabel()
        self.imgSize.setText('Image size should be the same')
        self.imgSize.setStyleSheet('color: red')

        self.union_check.setChecked(False)
        self.intersection_check.setChecked(False)
        self.difference_check.setChecked(False)
        self.complement_check.setChecked(False)
        self.switch.setChecked(False)

        self.txtFile.setMaxLength(200)
        self.startWindow()

    # Adds UI elements to the layout
    def startWindow(self):
        PageName=QLabel()
        PageName.setText("Set Transformation")
        filePathLabel = QLabel()
        filePathLabel.setText("Input File Path:")
        filePathGroup = QWidget()
        buttonsGroup = QWidget()
        sub_layout1 = QVBoxLayout(filePathGroup)
        sub_layout2 = QVBoxLayout(buttonsGroup)
        layout = QVBoxLayout()
        sub_layout1.addWidget(PageName)
        sub_layout1.addWidget(filePathLabel)
        sub_layout1.addWidget(self.imgSize)
        sub_layout1.addWidget(self.txtFile)
        sub_layout1.addWidget(self.file_button)
        sub_layout1.addWidget(self.txtFile2)
        sub_layout1.addWidget(self.file_button2)
        sub_layout2.addWidget(self.ok_button)
        sub_layout2.addWidget(self.cancel_button)
        sub_layout2.addWidget(self.union_check)
        sub_layout2.addWidget(self.intersection_check)
        sub_layout2.addWidget(self.difference_check)
        sub_layout2.addWidget(self.complement_check)
        sub_layout2.addWidget(self.switch)

        layout.addWidget(filePathGroup)
        layout.addWidget(buttonsGroup)
        self.file_button.clicked.connect(self.fileSelected)
        self.file_button2.clicked.connect(self.fileSelected2)
        self.ok_button.clicked.connect(self.processTransform)
        self.cancel_button.clicked.connect(self.noFileSelected)
        self.setLayout(layout)

    # Open FileDialog to select and image path for first image
    def fileSelected(self):
        f = None
        Text = self.txtFile.text()
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        self.txtFile.setText("")

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')


        if f is not None:
            with f:
                data = f.name
                self.txtFile.setText("")
                if len(data) > 0:
                    self.txtFile.setText(data)

    # Open FileDialog to select and image path for second image
    def fileSelected2(self):
        f = None
        Text = self.txtFile2.text()
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        self.txtFile2.setText("")

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')


        if f is not None:
            with f:
                data = f.name
                self.txtFile2.setText("")
                if len(data) > 0:
                    self.txtFile2.setText(data)

    # Handling no file selected
    def noFileSelected(self):
        mainWindow = self.parentWidget().parentWidget()
        mainWindow.InitiateApp()

    # Checks which checkboxes are check then calls ProcessTransformation
    def processTransform(self):
        checked = [False, False, False, False]
        if self.union_check.isChecked():
            checked[0] = True
        if self.intersection_check.isChecked():
            checked[1] = True
        if self.difference_check.isChecked():
            checked[2] = True
        if self.complement_check.isChecked():
            checked[3] = True
        if len(self.txtFile.text()) > 0:
            if os.path.isfile(self.txtFile.text()):
                if len(self.txtFile2.text()) > 0:
                    if os.path.isfile(self.txtFile2.text()):
                       if (self.switch.isChecked()):
                           SetTransformation.ProcessTransformation(self.txtFile2.text(), self.txtFile.text(),
                                                                      checked)
                       else:
                           SetTransformation.ProcessTransformation(self.txtFile.text(), self.txtFile2.text(),
                                                                      checked)
        else:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
       