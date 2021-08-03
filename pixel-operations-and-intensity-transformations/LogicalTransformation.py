import cv2
from PIL import Image
from MessageBox import MessageBox

class LogicalTransformation:



    def ProcessTransformation(inputFile1, inputFile2, checked):

        try:
            im1 = Image.open(inputFile1)
            im2 = Image.open(inputFile2)
            img1 = cv2.imread(inputFile1)
            img2 = cv2.imread(inputFile2)

            if checked[0] is True:
                img_and = cv2.bitwise_and(img1, img2)
                cv2.imshow("ANDimage", img_and)
            if checked[1] is True:
                img_or = cv2.bitwise_or(img1, img2)
                cv2.imshow("ORimage", img_or)
            if checked[2] is True:
                img_xor = cv2.bitwise_xor(img1, img2)
                cv2.imshow("XORimage", img_xor)
            if checked[3] is True:
                img_not = cv2.bitwise_not(img1, img2)
                cv2.imshow("Notimage", img_not)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # do stuff
        except IOError:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
