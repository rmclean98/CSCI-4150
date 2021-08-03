import cv2
from PIL import Image
from MessageBox import MessageBox


class SetTransformation:

    def ProcessTransformation(inputFile1, inputFile2, checked):

        try:
            im1 = Image.open(inputFile1)
            im2 = Image.open(inputFile2)
            img1 = cv2.imread(inputFile1)
            img2 = cv2.imread(inputFile2)

            if checked[0] is True:
                img_uni = cv2.add(img1, img2)
                cv2.imshow("UnionImage", img_uni)
            if checked[1] is True:
                img_inter = cv2.multiply(img1, img2)
                cv2.imshow("IntersectionImage", img_inter)
            if checked[2] is True:
                img_diff = cv2.subtract(img1, img2)
                cv2.imshow("DifferenceImage", img_diff)
            if checked[3] is True:
                img_comp = 255 - img1
                cv2.imshow("ComplementImage", img_comp)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except IOError:
            MessageBox.showMessageBox('info', 'Please provide a valid Image File Path to Transform')
