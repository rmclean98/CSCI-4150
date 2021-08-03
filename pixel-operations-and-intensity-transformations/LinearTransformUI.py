from ImportFile import *
from Home import Home
from LinearTransformation import LinearTransformation

class LinearTransformUI(QWidget):

    # Creates UI elements
    def __init__(self, parent=None):
        super(LinearTransformUI, self).__init__(parent)
        self.txtFile = QLineEdit()
        self.file_button=QPushButton('Browse file')
        self.ok_button=QPushButton('Apply')
        self.cancel_button=QPushButton('cancel')
        self.lr1 = QLabel("r1 (Input intensity 1):")
        self.ls1 = QLabel("s1 (Output intensity 1):")
        self.lr2 = QLabel("r2 (Input intensity 2):")
        self.ls2 = QLabel("s2 (Output intensity 2):")
        self.vr1 = QLabel()
        self.vs1 = QLabel()
        self.vr2 = QLabel()
        self.vs2 = QLabel()
        self.r1 = QSlider(Qt.Horizontal)
        self.r1.setMinimum(0)
        self.r1.setMaximum(255)
        self.r1.valueChanged.connect(self.vr1.setNum)
        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(0)
        self.s1.setMaximum(255)
        self.s1.valueChanged.connect(self.vs1.setNum)
        self.r2 = QSlider(Qt.Horizontal)
        self.r2.setMinimum(10)
        self.r2.setMaximum(255)
        self.r2.valueChanged.connect(self.vr2.setNum)
        self.s2 = QSlider(Qt.Horizontal)
        self.s2.setMinimum(0)
        self.s2.setMaximum(255)
        self.s2.valueChanged.connect(self.vs2.setNum)
        #self.file_button.setFixedSize(200, 20)
        #self.cancel_button.setFixedSize(200, 20)
        #self.ok_button.setFixedSize(200, 20)
        self.txtFile.setMaxLength(200)
        self.startWindow()


    # Adds UI elements to the layout
    def startWindow(self):
        PageName=QLabel()
        PageName.setText("Linear Transformation")
        filePathLabel=QLabel()
        filePathLabel.setText("Input File Path:")
        filePathGroup = QWidget()
        buttonsGroup = QWidget()
        sliderGroup = QWidget()
        sub_layout1 = QVBoxLayout(filePathGroup)
        sub_layout2 = QVBoxLayout(buttonsGroup)
        sub_layout3 = QVBoxLayout(sliderGroup)
        layout=QVBoxLayout()
        sub_layout1.addWidget(PageName)
        sub_layout1.addWidget(filePathLabel)
        sub_layout1.addWidget(self.txtFile)
        sub_layout1.addWidget(self.file_button)
        sub_layout2.addWidget(self.ok_button)
        sub_layout2.addWidget(self.cancel_button)
        sub_layout3.addWidget(self.lr1)
        sub_layout3.addWidget(self.vr1)
        sub_layout3.addWidget(self.r1)
        sub_layout3.addWidget(self.ls1)
        sub_layout3.addWidget(self.vs1)
        sub_layout3.addWidget(self.s1)
        sub_layout3.addWidget(self.lr2)
        sub_layout3.addWidget(self.vr2)
        sub_layout3.addWidget(self.r2)
        sub_layout3.addWidget(self.ls2)
        sub_layout3.addWidget(self.vs2)
        sub_layout3.addWidget(self.s2)
        #fb=layout.addWidget(QPushButton('Top'))
        #layout.addWidget(QPushButton('Bottom'))
        #e4.textChanged().connect(textchanged)
        layout.addWidget(filePathGroup)
        layout.addWidget(buttonsGroup)
        layout.addWidget(sliderGroup)
        #layout.addRow(self.fb,self.cb)
        self.file_button.clicked.connect(self.fileSelected)
        self.ok_button.clicked.connect(self.processTransform)
        self.cancel_button.clicked.connect(self.noFileSelected)
        self.setLayout(layout)
        #self.show()



    #Open FileDialog to select and image path
    def fileSelected(self):
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
                LinearTransformation.ProcessTransformation(self.txtFile.text(), self.r1.value(),  self.s1.value(), self.r2.value(), self.s2.value(),)
        else:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
       #print("contents of text box:" +Text)
