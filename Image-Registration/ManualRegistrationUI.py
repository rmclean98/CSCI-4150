from PyQt5.QtWidgets import QCheckBox

from ImportFile import *
import cv2
from Home import Home
from ProcessManualRegistration import ProcessManualRegistration

img= None

class ManualRegistrationUI(QWidget):
    
    
    
    # function to display the coordinates of 
    # of the points clicked on the image  
    # def click_event(event, x, y, flags, params): 
    #     global img
      
    #     # checking for left mouse clicks 
    #     if event == cv2.EVENT_LBUTTONDOWN: 
      
    #         # displaying the coordinates 
    #         # on the Shell 
    #         print(x, ' ', y) 
      
    #         # displaying the coordinates 
    #         # on the image window 
    #         font = cv2.FONT_HERSHEY_SIMPLEX 
    #         cv2.putText(img, str(x) + ',' +
    #                     str(y), (x,y), font, 
    #                     1, (255, 0, 0), 2) 
    #         cv2.imshow('image', img) 
      
    #     # checking for right mouse clicks      
    #     if event==cv2.EVENT_RBUTTONDOWN: 
      
    #         # displaying the coordinates 
    #         # on the Shell 
    #         print(x, ' ', y) 
      
    #         # displaying the coordinates 
    #         # on the image window 
    #         font = cv2.FONT_HERSHEY_SIMPLEX 
    #         b = img[y, x, 0] 
    #         g = img[y, x, 1] 
    #         r = img[y, x, 2] 
    #         cv2.putText(img, str(b) + ',' +
    #                     str(g) + ',' + str(r), 
    #                     (x,y), font, 1, 
    #                     (255, 255, 0), 2) 
    #         cv2.imshow('image', img) 

    # Creates UI elements
    def __init__(self, parent=None):
        super(ManualRegistrationUI, self).__init__(parent)
        self.txtFile = QLineEdit()
        
        self.file_button = QPushButton('Open Reference Image File to Choose Points')
        self.txtFile2 = QLineEdit()
        self.file_button2 = QPushButton('Open Target Image File to Choose Points')
        self.ok_button = QPushButton('Perform Manual Registration')
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
        PageName.setText("Manual Registration")
        filePathLabel = QLabel()
        filePathLabel.setText("Input File Path:")
        filePathGroup = QWidget()
        buttonsGroup = QWidget()
        sub_layout1 = QVBoxLayout(filePathGroup)
        sub_layout2 = QVBoxLayout(buttonsGroup)
        layout = QVBoxLayout()
        sub_layout1.addWidget(PageName)
        sub_layout1.addWidget(filePathLabel)
        #sub_layout1.addWidget(self.imgSize)
        sub_layout1.addWidget(self.txtFile)
        sub_layout1.addWidget(self.file_button)
        sub_layout1.addWidget(self.txtFile2)
        sub_layout1.addWidget(self.file_button2)
        sub_layout2.addWidget(self.ok_button)
        sub_layout2.addWidget(self.cancel_button)        
        layout.addWidget(filePathGroup)
        layout.addWidget(buttonsGroup)
        self.file_button.clicked.connect(self.fileSelected)
        self.file_button2.clicked.connect(self.fileSelected2)
        self.ok_button.clicked.connect(self.processTransform)
        self.cancel_button.clicked.connect(self.noFileSelected)
        self.setLayout(layout)
        

    #Open FileDialog to select and image path for first image
    def fileSelected(self):
        global img
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
        if len(self.txtFile.text()) > 0 and len(self.txtFile2.text()) > 0:
            if os.path.isfile(self.txtFile.text()):
                if len(self.txtFile2.text()) > 0:
                    if os.path.isfile(self.txtFile2.text()):
                        ProcessManualRegistration.ProcessTransformation(self.txtFile.text(), self.txtFile2.text())
                        
        else:
            MessageBox.showMessageBox('info', 'Please provide a valid Image File Path to Transform')
    
    
