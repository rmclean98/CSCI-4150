from ImportFile import *
class Home(QWidget):

    # Add UI elements to the Home Layout
   def __init__(self, parent=None):
       super(Home, self).__init__(parent)

       self.harrisButton = QRadioButton("Harris Corner Detection")
       self.manualRegButton = QRadioButton("Manual Registration")
       self.autoRegButton = QRadioButton("Automatic Registration")
       layout=QFormLayout()
       layout.addWidget(self.harrisButton)
       layout.addWidget(self.manualRegButton)
       layout.addWidget(self.autoRegButton)
       self.setLayout(layout)
