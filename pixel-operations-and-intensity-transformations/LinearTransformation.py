import cv2
from PIL import Image
from MessageBox import MessageBox
import numpy as np

class LinearTransformation:

    # Changes the pixel values based on the input and output intensity selected by the user.
    def pixelVal(pix, r1, s1, r2, s2):
        if (0 <= pix and pix <= r1):
            return (s1 / r1)*pix
        elif (r1 < pix and pix <= r2):
            return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
        else:
            return ((255 - s2)/(255 - r2)) * (pix - r2) + s2

    # Applys the transfomation then displays the original image and the images after the transfomation
    def ProcessTransformation(inputFile, r1, s1, r2, s2):

        try:
            im=Image.open(inputFile)
            img = cv2.imread(inputFile, 0)
            cv2.imshow("Original Image",img)
            pixelVal_vec = np.vectorize(LinearTransformation.pixelVal)
            contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)
            cv2.imshow("Piecewise-Linear",contrast_stretched)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            # do stuff
        except IOError:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
