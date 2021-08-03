import cv2
import numpy as np
from PIL import Image
from MessageBox import MessageBox
from matplotlib import pyplot as plt

refPT = []
targetPT = []
img1 = None
img2 = None
referenceIMG=None
targetIMG=None

class ProcessManualRegistration:

    def refClickPoints(event,x,y,flags,param):
        global refPT, targetPT, img1,referenceIMG
        if event == cv2.EVENT_LBUTTONUP:
            print((x,y))
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img1, str(x) + ',' +
                        str(y), (x,y), font,
                        1, (255, 0, 0), 2)
            refPT.append((x,y))
            cv2.imshow('Reference Image', img1)


    def targetClickPoints(event,x,y,flags,param):
        global refPT, targetPT, img2,targetIMG
        if event == cv2.EVENT_LBUTTONUP:
            print("click on target")
            print((x,y))
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img2, str(x) + ',' +
                        str(y), (x,y), font,
                        1, (255, 0, 0), 2)
            targetPT.append((x,y))
            cv2.imshow('Target Image', img2)
            # # wait for a key to be pressed to exit


    def ProcessTransformation(inputFile1, inputFile2):
        global refPT, targetPT, img1, img2,referenceIMG,targetIMG
        try:
            #If not a inputfiles are not valid image file, the control will navigate to exception clause
            im=Image.open(inputFile1)
            im=Image.open(inputFile2)
            # Load the images
            referenceIMG = cv2.imread(inputFile1)
            targetIMG = cv2.imread(inputFile2)

            img1 = referenceIMG.copy()
            img2 = targetIMG.copy()

            height, width = referenceIMG.shape[:2]

            cv2.namedWindow('Reference Image')
            cv2.imshow('Reference Image', img1)

            cv2.setMouseCallback('Reference Image', ProcessManualRegistration.refClickPoints)

            # # wait for a key to be pressed to exit
            cv2.waitKey(0)

            # # close the window
            cv2.destroyAllWindows()
            cv2.imshow('Target Image', img2)

            cv2.setMouseCallback('Target Image', ProcessManualRegistration.targetClickPoints)

            # # wait for a key to be pressed to exit
            cv2.waitKey(0)

            # # close the window
            cv2.destroyAllWindows()


            print("refPT: " + str(refPT))
            print("targetPT: " + str(targetPT))

            points1 = np.array(refPT)
            points2 = np.array(targetPT)

            print("points1: " + str(points1))
            print("points2: " + str(points2))

            #Find and Apply Homography
            homography, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

            transformed_img = cv2.warpPerspective(targetIMG, homography, (width, height))

            cv2.imshow("Original Image", referenceIMG)
            cv2.imshow('Target Image', targetIMG)
            cv2.imshow("Transformed Image", transformed_img)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except IOError:

            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
