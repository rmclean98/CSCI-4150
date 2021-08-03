from ImportFile import *

class MessageBox:

    def showMessageBox(type,message):
       msg = QMessageBox()
       
       if type=='info':
           msg.setIcon(QMessageBox.Information)    
           msg.setText(message)
           #msg.setInformativeText("This is additional information")
           msg.setWindowTitle("MessageBox")
           #msg.setDetailedText("The details are as follows:")
           msg.setStandardButtons(QMessageBox.Ok)
           msg.exec_()
           
    
       