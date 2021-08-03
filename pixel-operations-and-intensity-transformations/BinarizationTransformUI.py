from PyQt5.QtWidgets import QCheckBox

from ImportFile import *
from Home import Home
from BinarizationTransformation import BinarizationTransformation

class BinarizationTransformUI(QWidget):
    
    # Creates UI elements
    def __init__(self, parent=None):
        super(BinarizationTransformUI, self).__init__(parent)
        self.txtFile = QLineEdit()
        self.file_button=QPushButton('Browse file')
        self.ok_button=QPushButton('Apply')
        self.cancel_button=QPushButton('cancel')
        self.th1_check = QCheckBox('Binary Threshold')
        self.th2_check = QCheckBox('Binary Threshold Inverted')
        self.th3_check = QCheckBox('Truncated Threshold')
        self.th4_check = QCheckBox('Set to 0')
        self.th5_check = QCheckBox('Set to 0 Inverted')

        self.th1_check.setChecked(False)
        self.th2_check.setChecked(False)
        self.th3_check.setChecked(False)
        self.th4_check.setChecked(False)
        self.th5_check.setChecked(False)
        self.txtFile.setMaxLength(200)
        self.startWindow()
        
        
    # Adds UI elements to the layout
    def startWindow(self):
        PageName=QLabel()
        PageName.setText("Binarization/Thresholding Transformation")
        filePathLabel=QLabel()
        filePathLabel.setText("Input File Path:")
        filePathGroup = QWidget()
        buttonsGroup = QWidget()
        sub_layout1 = QVBoxLayout(filePathGroup)
        sub_layout2 = QVBoxLayout(buttonsGroup)
        layout=QVBoxLayout()
        sub_layout1.addWidget(PageName)
        sub_layout1.addWidget(filePathLabel)  
        sub_layout1.addWidget(self.txtFile)        
        sub_layout1.addWidget(self.file_button)
        sub_layout2.addWidget(self.ok_button)
        sub_layout2.addWidget(self.cancel_button)
        sub_layout2.addWidget(self.th1_check)
        sub_layout2.addWidget(self.th2_check)
        sub_layout2.addWidget(self.th3_check)
        sub_layout2.addWidget(self.th4_check)
        sub_layout2.addWidget(self.th5_check)

        layout.addWidget(filePathGroup)
        layout.addWidget(buttonsGroup)
        self.file_button.clicked.connect(self.fileSelected)
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
        
      
        
    
    # Handling no file selected
    def noFileSelected(self):        
        mainWindow=self.parentWidget().parentWidget()
        mainWindow.InitiateApp()
        

    # Checks which checkboxes are check then calls ProcessTransformation
    def processTransform(self):
        checked = [False, False, False, False, False]
        if self.th1_check.isChecked():
            checked[0] = True
        if self.th2_check.isChecked():
            checked[1] = True
        if self.th3_check.isChecked():
            checked[2] = True
        if self.th4_check.isChecked():
            checked[3] = True
        if self.th5_check.isChecked():
            checked[4] = True
        if len(self.txtFile.text())>0:
            if os.path.isfile(self.txtFile.text()):                
                BinarizationTransformation.ProcessTransformation(self.txtFile.text(), checked)
        else:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
       