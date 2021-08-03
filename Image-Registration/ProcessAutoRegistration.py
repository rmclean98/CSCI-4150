import cv2
import numpy as np
from PIL import Image
from MessageBox import MessageBox
from matplotlib import pyplot as plt

class ProcessAutoRegistration:



    def ProcessTransformation(inputFile1, inputFile2):

        try:
            #If not a inputfile is not valid image file, the control will navigate to exception clause
            im=Image.open(inputFile1)
            im=Image.open(inputFile2)
            # Load the images in greyscale
            referenceIMG = cv2.imread(inputFile1)
            targetIMG = cv2.imread(inputFile2)

            referenceBW = cv2.cvtColor(referenceIMG, cv2.COLOR_BGR2GRAY)
            targetBW = cv2.cvtColor(targetIMG, cv2.COLOR_BGR2GRAY)

            height, width = referenceBW.shape

            orb = cv2.ORB_create(5000)

            kp1, d1 = orb.detectAndCompute(targetBW, None)
            kp2, d2 = orb.detectAndCompute(referenceBW, None)

            matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

            matches = matcher.match(d1, d2)

            matches.sort(key = lambda x: x.distance)

            matches = matches[:int(len(matches)*90)]
            no_of_matches = len(matches)

            # Define empty matrices of shape no_of_matches * 2.
            p1 = np.zeros((no_of_matches, 2))
            p2 = np.zeros((no_of_matches, 2))

            for i in range(len(matches)):
                p1[i, :] = kp1[matches[i].queryIdx].pt
                p2[i, :] = kp2[matches[i].trainIdx].pt

            # Find the homography matrix.
            homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)

            #Apply Homography
            
            transformed_img = cv2.warpPerspective(targetIMG, homography, (width, height))

            cv2.imshow("Reference Image", referenceIMG)
            cv2.imshow("Target Image", targetIMG)
            cv2.imshow("Matched Image", transformed_img)

            
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except IOError:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
