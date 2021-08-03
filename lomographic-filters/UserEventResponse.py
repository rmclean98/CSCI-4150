from ImportFile import *
from MainWindow import MainWindow

class UserEventResponse:
    def userEvent():
        if cv2.waitKey(0) == ord('q'):
            print('exitting loop')

        if cv2.waitKey(0) == ord('s'):
            app = QApplication([])
            mainWindow = MainWindow()
            mainWindow.setWindowTitle('File Save Dialog')
            mainWindow.show()
            app.exec_()
