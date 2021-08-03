from ImportFile import *
class Home(QWidget):

    # Add UI elements to the Home Layout
   def __init__(self, parent=None):
       super(Home, self).__init__(parent)

       #self.histEquivButton = QRadioButton("Histogram Equalization")
       self.fileNameLabel = QLabel("Enter File Name to Save:")
       self.txtFile = QLineEdit()       
       self.txtFile.setMaxLength(200)       
       self.ok_button=QPushButton('Ok')
       self.cancel_button=QPushButton('cancel')
       # self.histSpecButton = QRadioButton("Histogram Matching/Specification")
       self.startWindow()
       
   def startWindow(self):
       layout=QFormLayout()
       buttonsGroup = QWidget()
       #sub_layout2 = QVBoxLayout(buttonsGroup)
       layout.addWidget(self.fileNameLabel)
       layout.addWidget(self.txtFile)
       layout.addWidget(self.ok_button)
       layout.addWidget(self.cancel_button)
       #layout.addWidget(buttonsGroup)
       #layout.addWidget(self.cancel_button)
       self.ok_button.clicked.connect(self.EnterFileName)
       self.cancel_button.clicked.connect(self.noFileSelected)
       self.setLayout(layout)
       
       

     #Handling no file selected
   def noFileSelected(self):
        mainWindow=self.parentWidget().parentWidget()
        f = open("fileNameTracker.txt","w")
        f.write('cancel')
        f.close()
        mainWindow=self.parentWidget().parentWidget()
        mainWindow.closeApp()
        


    #Calls ProcessTransformation
   def EnterFileName(self):
        if len(self.txtFile.text())>0:
            f = open("fileNameTracker.txt","w+")
            f.write(self.txtFile.text())
            f.close()
            mainWindow=self.parentWidget().parentWidget()
            mainWindow.closeApp()
        else:
            MessageBox.showMessageBox('info','Enter a Valid File Name')
