from ImportFile import *
from Home import Home
import argparse
import textwrap
from ImageNegativeUI import ImageNegativeUI
from PowerTransformUI import PowerTransformUI
from LogTransformUI import LogTransformUI
from BitPlaneTransformUI import BitPlaneTransformUI
from ArithmeticTransformUI import ArithmeticTransformUI
from LinearTransformUI import LinearTransformUI
from SetTransformUI import SetTransformUI
from BinarizationTransformUI import BinarizationTransformUI
from LogicalTransformUI import LogicalTransformUI


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.InitiateApp()

    def keyPressEvent(self, event):
        if event.key()==81:
            self.close()


    # Add HomeLayout to the MainWindow
    def InitiateApp(self):
        self.setStyleSheet(open('pixel_ops.css').read())
        self.setFixedSize(QDesktopWidget().width() *0.33, QDesktopWidget().height() *0.78)      
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.home=Home(self)

        # Trigger Actions when user selects the required transformations
        self.central_widget.addWidget(self.home)
        self.home.imgNegButton.toggled.connect(self.btnstate) #Trigger for ImageNegative
        self.home.bitPlaneButton.toggled.connect(self.btnstate) #Trigger for BitPlane
        self.home.logButton.toggled.connect(self.btnstate) #Trigger for Logarithmic
        self.home.PowerButton.toggled.connect(self.btnstate) #Trigger for Power Law
        self.home.linearButton.toggled.connect(self.btnstate) #Trigger for Linear
        self.home.arithmeticButton.toggled.connect(self.btnstate) #Trigger for Arithmetic
        self.home.setButton.toggled.connect(self.btnstate) #Trigger for SetOperations
        self.home.binarizationButton.toggled.connect(self.btnstate) #Trigger for binarization/Threshold
        self.home.logicalButton.toggled.connect(self.btnstate) #Trigger for Logical



    # This method calls the appropriate methods for transformation selected by the user
    def btnstate(self):

        if self.home.imgNegButton.isChecked() == True:
            self.imgNegativeTransform=ImageNegativeUI(self)
            self.central_widget.removeWidget(self.home)
            self.central_widget.addWidget(self.imgNegativeTransform)


        if self.home.bitPlaneButton.isChecked() == True:
            self.bitPlaneTransform=BitPlaneTransformUI(self)
            self.central_widget.removeWidget(self.home)
            self.central_widget.addWidget(self.bitPlaneTransform)

        if self.home.logButton.isChecked() == True:
            self.logTransform=LogTransformUI(self)
            self.central_widget.removeWidget(self.home)
            self.central_widget.addWidget(self.logTransform)

        if self.home.PowerButton.isChecked() == True:
            self.PowerTransform=PowerTransformUI(self)
            self.central_widget.removeWidget(self.home)
            self.central_widget.addWidget(self.PowerTransform)

        if self.home.linearButton.isChecked() == True:
            self.LinearTransform=LinearTransformUI(self)
            self.central_widget.removeWidget(self.home)
            self.central_widget.addWidget(self.LinearTransform)

        if self.home.arithmeticButton.isChecked() == True:
            self.ArithmeticTransform=ArithmeticTransformUI(self)
            self.central_widget.removeWidget(self.home)
            self.central_widget.addWidget(self.ArithmeticTransform)

        if self.home.setButton.isChecked() == True:
            self.SetTransform=SetTransformUI(self)
            self.central_widget.removeWidget(self.home)
            self.central_widget.addWidget(self.SetTransform)

        if self.home.binarizationButton.isChecked() == True:
            self.BinarizationTransform=BinarizationTransformUI(self)
            self.central_widget.removeWidget(self.home)
            self.central_widget.addWidget(self.BinarizationTransform)


        if self.home.logicalButton.isChecked() == True:
            self.LogicalTransform=LogicalTransformUI(self)
            self.central_widget.removeWidget(self.home)
            self.central_widget.addWidget(self.LogicalTransform)

# Main Function where we handle commandline help and Initiate the Application UI
if __name__ == '__main__':
    parser = argparse.ArgumentParser(epilog=textwrap.dedent('Please read the user instructions document \"ReadMe.pdf\" for more details'),formatter_class=argparse.RawTextHelpFormatter)
    args = parser.parse_args()
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.setWindowTitle('Image Transformation')
    mainWindow.show()
    app.exec_()
