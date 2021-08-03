import cv2
import numpy as np
from PIL import Image
from MessageBox import MessageBox
from matplotlib import pyplot as plt

class ProcessHarrisCorner:



    def ProcessTransformation(inputFile,bsizevalue,ksizevalue,harrisvalue):

        try:
            # read images
            img1 = cv2.imread(inputFile)  
            
            # Change to Grayscale
            img1_Gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            
            # Find points using Harris Corner Detection
            dst=cv2.cornerHarris(img1_Gray,int(bsizevalue),int(ksizevalue),float(harrisvalue))
            dst = cv2.dilate(dst, None)
            
            #Change the intensity of the points detected to make it visible
            img1[dst>0.05*dst.max()] =[0,0,255]
            
            
            cv2.imshow("Image",img1)
            cv2.waitKey(0)

        except IOError:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
