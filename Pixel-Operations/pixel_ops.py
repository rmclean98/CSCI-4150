from PyQt5.QtWidgets import *

import sys

from random import randint


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.dialog = QFileDialog(self)
        self.dialog.setFileMode(QFileDialog.AnyFile)
        layout.addWidget(self.dialog)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.btn = QPushButton("QFileDialog static method demo")
        self.btn.clicked.connect(self.getfile)
        self.setLayout(layout)

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\',"Image files (*.jpg *.gif)")
        self.le.setPixmap(QPixmap(fname))

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

"""
import numpy as np
import cv2
import cvui

WINDOW1_NAME = 'Main Window'


# Update a window using cvui functions, then show it using cv2.imshow().
def window(name):
    # Create a frame for this window and fill it with a nice color
    frame = np.zeros((500, 200, 3), np.uint8)
    frame[:] = (49, 52, 49)

    # Inform cvui that the components to be rendered from now one belong to
    # a window in particular.
    #
    # If you don't inform that, cvui will assume the components belong to
    # the default window (informed in cvui.init()). In that case, the
    # interactions with all other windows being used will not work.
    cvui.context(name)

    # Show info regarding the window
    cvui.printf(frame, 5, 50, 'Pixel Operations and Intensity')

    # Buttons return true if they are clicked
    if cvui.button(frame, 30, 90, 'Image negative'):
        #cvui.printf(frame, 30, 95, '1Button clicked!')
        print('Button clicked on: ', name)

    if cvui.button(frame, 30, 130, 'Bit-plane images'):
        #cvui.printf(frame, 30, 135, '2Button clicked!')
        print('Button clicked on: ', name)

    if cvui.button(frame, 30, 160, 'Log transform'):
        #cvui.printf(frame, 30, 165, '3Button clicked!')
        print('Button clicked on: ', name)

    # Tell cvui to update its internal structures regarding a particular window.
    #
    # If cvui is being used in multiple windows, you need to enclose all component
    # calls between the pair cvui.context(NAME)/cvui.update(NAME), where NAME is
    # the name of the window being worked on.
    cvui.update(name)

    # Show the content of this window on the screen
    cvui.imshow(name, frame)


def main():
    # Init cvui. If you don't tell otherwise, cvui will create the required OpenCV
    # windows based on the list of names you provided.
    windows = [WINDOW1_NAME]
    cvui.init(windows, 1)

    while (True):
        # The functions below will update a window and show them using cv2.imshow().
        # In that case, you must call the pair cvui.context(NAME)/cvui.update(NAME)
        # to render components and update the window.
        window(WINDOW1_NAME)


        # Check if ESC key was pressed
        if cv2.waitKey(20) == 27:
            break

if __name__ == '__main__':
    main()
"""
