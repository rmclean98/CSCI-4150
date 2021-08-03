import cv2
from PIL import Image
from MessageBox import MessageBox

class BinarizationTransformation:



    def ProcessTransformation(inputFile, checked):

        try:
            im=Image.open(inputFile)
            img1 = cv2.imread(inputFile, 0)
            cv2.imshow("original", img1)

            if checked[0] is True:
                ret, th1 = cv2.threshold(img1, 120, 255, cv2.THRESH_BINARY)
                cv2.imshow("Binary Threshold", th1)
            if checked[1] is True:
                ret, th2 = cv2.threshold(img1, 120, 255, cv2.THRESH_BINARY_INV)
                cv2.imshow("Binary Threshold Inverted", th2)
            if checked[2] is True:
                ret, th3 = cv2.threshold(img1, 120, 255, cv2.THRESH_TRUNC)
                cv2.imshow("Truncated Threshold", th3)
            if checked[3] is True:
                ret, th4 = cv2.threshold(img1, 120, 255, cv2.THRESH_TOZERO)
                cv2.imshow("Set to 0", th4)
            if checked[4] is True:
                ret, th5 = cv2.threshold(img1, 120, 255, cv2.THRESH_TOZERO_INV)
                cv2.imshow("Set to 0 Inverted", th5)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        except IOError:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
