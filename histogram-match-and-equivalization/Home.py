from ImportFile import *
class Home(QWidget):

    # Add UI elements to the Home Layout
   def __init__(self, parent=None):
       super(Home, self).__init__(parent)

       self.histEquivButton = QRadioButton("Histogram Equalization")
       self.histSpecButton = QRadioButton("Histogram Matching/Specification")
       layout=QFormLayout()
       layout.addWidget(self.histEquivButton)
       layout.addWidget(self.histSpecButton)
       self.setLayout(layout)
