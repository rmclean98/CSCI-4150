import cv2
from PIL import Image
from MessageBox import MessageBox

class ArithmeticTransformation:

    # applys Add, Subtract, Multiply, Division to the two input images
    def ProcessTransformation(inputFile, inputFile2, checked):

        try:

            im=Image.open(inputFile)
            im2=Image.open(inputFile2)
            img = cv2.imread(inputFile)
            img2 = cv2.imread(inputFile2)

            img1Size = img.shape
            img2Size = img2.shape

            # makes sure the resolution of the two images is the same size and if its not sends a message
            if (img1Size[0] == img2Size[0] and img1Size[1] == img2Size[1]):
                if checked[0] is True:
                    add = cv2.add(img, img2)
                    cv2.imshow("Addition", add)
                if checked[1] is True:
                    sub = cv2.subtract(img, img2)
                    cv2.imshow("Subtraction", sub)
                if checked[2] is True:
                    multi = img
                    multi = cv2.multiply(img, img2, multi)
                    cv2.imshow("Multiplation", multi)
                if checked[3] is True:
                    div = img
                    div = cv2.divide(img, img2, div)
                    cv2.imshow("Division", div)
            else:
                MessageBox.showMessageBox('info','Pictures need to be the same size')

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # do stuff
        except IOError:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
