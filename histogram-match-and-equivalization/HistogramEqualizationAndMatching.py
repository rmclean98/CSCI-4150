from ImportFile import *
from Home import Home
import argparse
import textwrap
from HistogramEqualizationUI import HistogramEqualizationUI
from HistogramSpecificationUI import HistogramSpecificationUI


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
        self.home.histEquivButton.toggled.connect(self.btnstate) 
        self.home.histSpecButton.toggled.connect(self.btnstate) #Trigger for Logical



    # This method calls the appropriate methods for transformation selected by the user
    def btnstate(self):

        if self.home.histEquivButton.isChecked() == True:
            self.HistogramEqualization=HistogramEqualizationUI(self)
            self.central_widget.removeWidget(self.home)
            self.central_widget.addWidget(self.HistogramEqualization)



        if self.home.histSpecButton.isChecked() == True:
            self.HistogramSpecification=HistogramSpecificationUI(self)
            self.central_widget.removeWidget(self.home)
            self.central_widget.addWidget(self.HistogramSpecification)

# Main Function where we handle commandline help and Initiate the Application UI
if __name__ == '__main__':
    parser = argparse.ArgumentParser(epilog=textwrap.dedent('Please read the user instructions document \"ReadMe.pdf\" for more details'),formatter_class=argparse.RawTextHelpFormatter)
    args = parser.parse_args()
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.setWindowTitle('Histogram Equalization And Matching')
    mainWindow.show()
    app.exec_()
