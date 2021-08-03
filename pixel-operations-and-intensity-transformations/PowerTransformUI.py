from ImportFile import *
from Home import Home
from PowerLawTransformation import PowerLawTransformation

class PowerTransformUI(QWidget):
    
    # Creates UI elements
    def __init__(self, parent=None):
        super(PowerTransformUI, self).__init__(parent)
        self.txtFile = QLineEdit()
        self.file_button=QPushButton('Browse file')
        self.gamma = QLineEdit()
        self.gamma.setValidator(QtGui.QDoubleValidator(-999, 999, 3))
        self.ok_button=QPushButton('Apply')
        self.cancel_button=QPushButton('cancel')    
        self.startWindow()
        
        
    # Adds UI elements to the layout
    def startWindow(self):
        PageName=QLabel()
        PageName.setText("Power-Law (Gamma)Transformation")
        filePathLabel=QLabel()
        filePathLabel.setText("Input File Path:")
        gammaLabel = QLabel("Enter Gamma Value:")
        self.gamma.setAlignment(Qt.AlignCenter)
        filePathGroup = QWidget()
        buttonsGroup = QWidget()
        gammaGroup = QWidget()        
        sub_layout1 = QVBoxLayout(filePathGroup)
        sub_layout2 = QVBoxLayout(buttonsGroup)
        sub_layout3 =QFormLayout(gammaGroup)
        layout=QVBoxLayout()
        sub_layout1.addWidget(PageName)
        sub_layout1.addWidget(filePathLabel)  
        sub_layout1.addWidget(self.txtFile)        
        sub_layout1.addWidget(self.file_button)
        sub_layout2.addWidget(self.ok_button)
        sub_layout2.addWidget(self.cancel_button)
        sub_layout3.addRow(gammaLabel,self.gamma)       
        layout.addWidget(filePathGroup)
        layout.addWidget(gammaGroup)        
        layout.addWidget(buttonsGroup)        
        self.file_button.clicked.connect(self.fileSelected)
        self.ok_button.clicked.connect(self.processTransform) 
        self.cancel_button.clicked.connect(self.noFileSelected)          
        self.setLayout(layout)
        
        
        
    
    #Open FileDialog to select and image path for the image
    def fileSelected(self):
        Text=self.txtFile.text()
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        self.txtFile.setText("")
         
        if dlg.exec_():
           
           filenames = dlg.selectedFiles()
           f = open(filenames[0], 'r')
			
        with f:
            data = f.name
            self.txtFile.setText("")
            if len(data)>0:
               self.txtFile.setText(data)
       
      
    #Handling no file selected    
    def noFileSelected(self):        
        mainWindow=self.parentWidget().parentWidget()
        mainWindow.InitiateApp()

    
     #Calls ProcessTransformation
    def processTransform(self):
        if len(self.txtFile.text())>0:
            if len(self.gamma.text())>0:            
                if os.path.isfile(self.txtFile.text()):                
                    PowerLawTransformation.ProcessTransformation(self.txtFile.text(),self.gamma.text())
            else:
                MessageBox.showMessageBox('info','Please provide a gamma value')
        else:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
       
