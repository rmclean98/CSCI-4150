from ImportFile import *
class Home(QWidget):

    # Add UI elements to the Home Layout
   def __init__(self, parent=None):
       super(Home, self).__init__(parent)

       self.imgNegButton = QRadioButton("Image Negative")
       self.bitPlaneButton = QRadioButton("Bit-Plane Transformation") 
       self.logButton = QRadioButton("Log Transformation")
       self.PowerButton = QRadioButton("Power-Law (Gamma)Transformation")
       self.linearButton = QRadioButton("Linear and piecewise-linear transformations")
       self.arithmeticButton = QRadioButton("Image arithmetic operations")
       self.setButton = QRadioButton("Image set operations")
       self.binarizationButton = QRadioButton("Binarization/thresholding")
       self.logicalButton = QRadioButton("Logical operations on binary images")

       layout=QFormLayout()
       layout.addWidget(self.imgNegButton)
       layout.addWidget(self.bitPlaneButton)
       layout.addWidget(self.logButton)
       layout.addWidget(self.PowerButton)
       layout.addWidget(self.linearButton)
       layout.addWidget(self.arithmeticButton)
       layout.addWidget(self.setButton)
       layout.addWidget(self.binarizationButton)
       layout.addWidget(self.logicalButton)

       self.setLayout(layout)
