from PyQt5.QtWidgets import QCheckBox

from ImportFile import *
from Home import Home
from LogicalTransformation import LogicalTransformation


class LogicalTransformUI(QWidget):

    # Creates UI elements
    def __init__(self, parent=None):
        super(LogicalTransformUI, self).__init__(parent)
        self.txtFile = QLineEdit()
        self.file_button = QPushButton('Browse file 1')
        self.txtFile2 = QLineEdit()
        self.file_button2 = QPushButton('Browse file 2')
        self.ok_button = QPushButton('Apply')
        self.cancel_button = QPushButton('cancel')
        self.and_check = QCheckBox('And')
        self.or_check = QCheckBox('Or')
        self.xor_check = QCheckBox('Xor')
        self.not_check = QCheckBox('Not')
        self.switch = QCheckBox('Switch Images Paths')
        self.imgSize = QLabel()
        self.imgSize.setText('Image size should be the same')
        self.imgSize.setStyleSheet('color: red')
        self.and_check.setChecked(False)
        self.or_check.setChecked(False)
        self.xor_check.setChecked(False)
        self.not_check.setChecked(False)
        self.switch.setChecked(False)
        self.txtFile.setMaxLength(200)
        self.startWindow()

    # Adds UI elements to the layout
    def startWindow(self):
        PageName=QLabel()
        PageName.setText("Logical Transformation")
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
        sub_layout2.addWidget(self.and_check)
        sub_layout2.addWidget(self.or_check)
        sub_layout2.addWidget(self.xor_check)
        sub_layout2.addWidget(self.not_check)
        sub_layout2.addWidget(self.switch)
        layout.addWidget(filePathGroup)
        layout.addWidget(buttonsGroup)
        self.file_button.clicked.connect(self.fileSelected)
        self.file_button2.clicked.connect(self.fileSelected2)
        self.ok_button.clicked.connect(self.processTransform)
        self.cancel_button.clicked.connect(self.noFileSelected)
        self.setLayout(layout)
        

    #Open FileDialog to select and image path for first image
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
       

    #Open FileDialog to select and image path for second image
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
        

    #Handling no file selected
    def noFileSelected(self):
        mainWindow = self.parentWidget().parentWidget()
        mainWindow.InitiateApp()

    #Checks which checkboxes are check then calls ProcessTransformation
    def processTransform(self):
        checked = [False, False, False, False]
        if self.and_check.isChecked():
            checked[0] = True
        if self.or_check.isChecked():
            checked[1] = True
        if self.xor_check.isChecked():
            checked[2] = True
        if self.not_check.isChecked():
            checked[3] = True
        if len(self.txtFile.text()) > 0:
            if os.path.isfile(self.txtFile.text()):
                if len(self.txtFile2.text()) > 0:
                    if os.path.isfile(self.txtFile2.text()):
                        if (self.switch.isChecked()):
                            LogicalTransformation.ProcessTransformation(self.txtFile2.text(), self.txtFile.text(),
                                                                       checked)
                        else:
                            LogicalTransformation.ProcessTransformation(self.txtFile.text(), self.txtFile2.text(),
                                                                       checked)
        else:
            MessageBox.showMessageBox('info', 'Please provide a valid Image File Path to Transform')
    
