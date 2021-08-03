from ImportFile import *
from Home import Home
from BitPlaneTransformation import BitPlaneTransformation

class BitPlaneTransformUI(QWidget):

    # Creates UI elements
    def __init__(self, parent=None):
        super(BitPlaneTransformUI, self).__init__(parent)
        self.txtFile = QLineEdit()
        self.file_button=QPushButton('Browse file')
        self.ok_button=QPushButton('Apply')
        self.cancel_button=QPushButton('cancel')
        #self.file_button.setFixedSize(200, 20)
        #self.cancel_button.setFixedSize(200, 20)
        #self.ok_button.setFixedSize(200, 20)
        self.txtFile.setMaxLength(200)
        self.startWindow()


    # Adds UI elements to the layout
    def startWindow(self):
        PageName=QLabel()
        PageName.setText("Bit-Plane Transformation")
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
        #fb=layout.addWidget(QPushButton('Top'))
        #layout.addWidget(QPushButton('Bottom'))
        #e4.textChanged().connect(textchanged)
        layout.addWidget(filePathGroup)
        layout.addWidget(buttonsGroup)
        #layout.addRow(self.fb,self.cb)
        self.file_button.clicked.connect(self.fileSelected)
        self.ok_button.clicked.connect(self.processTransform)
        self.cancel_button.clicked.connect(self.noFileSelected)
        self.setLayout(layout)
        #self.show()



    #Open FileDialog to select and image path
    def fileSelected(self):
        f = None
        Text=self.txtFile.text()
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        self.txtFile.setText("")
        #dlg.setFilter("Text files (*.txt)")
        #filenames = QStringList()

        if dlg.exec_():

           filenames = dlg.selectedFiles()
           f = open(filenames[0], 'r')

        #if len(self.txtFile.text())>0:
        if f is not None:
            with f:
                data = f.name
                self.txtFile.setText("")
                if len(data)>0:
                    self.txtFile.setText(data)
           #print("contents of text box:" +Text)



    #Handling no file selected
    def noFileSelected(self):
        mainWindow=self.parentWidget().parentWidget()
        #mainWindow.show()
        #mainWindow.setCentralWidget(mainWindow.home)
        mainWindow.InitiateApp()


    #Checks which checkboxes are check then calls ProcessTransformation
    def processTransform(self):
        if len(self.txtFile.text())>0:
            if os.path.isfile(self.txtFile.text()):
                BitPlaneTransformation.ProcessTransformation(self.txtFile.text())
        else:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
       #print("contents of text box:" +Text)
