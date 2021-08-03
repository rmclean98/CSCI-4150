from ImportFile import *
from Home import Home
from LogTransformation import LogTransformation

class LogTransformUI(QWidget):
    
    # Creates UI elements
    def __init__(self, parent=None):
        super(LogTransformUI, self).__init__(parent)
        self.txtFile = QLineEdit()
        self.file_button=QPushButton('Browse file')
        self.ok_button=QPushButton('Apply')
        self.cancel_button=QPushButton('cancel')        
        self.txtFile.setMaxLength(200)         
        self.startWindow()
        
        
    # Adds UI elements to the layout
    def startWindow(self):
        PageName=QLabel()
        PageName.setText("Logarithmic Transformation")
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
        layout.addWidget(filePathGroup)
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
            if os.path.isfile(self.txtFile.text()):                
                LogTransformation.ProcessTransformation(self.txtFile.text())                
        else:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
      
