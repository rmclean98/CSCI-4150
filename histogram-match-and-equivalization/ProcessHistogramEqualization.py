import cv2
import numpy as np
from Hist import *
from PIL import Image
from MessageBox import MessageBox
from matplotlib import pyplot as plt

class ProcessHistogramEqualization:



    def ProcessTransformation(inputFile):

        try:
            #If not a inputfile is not valid image file, the control will navigate to exception clause 
            im=Image.open(inputFile)
            #imports the image in grayscale and transforms it into an np array
            img = cv2.imread(inputFile, 0)
            imgArray = np.asarray(img)

            #Displays the histogram before the Equivalizion has been applied
            hist,bins = np.histogram(img.flatten(),256,[0,256])
            plt.hist(img.flatten(),256,[0,256], color = 'r')
            plt.xlim([0,256])
            plt.savefig('originalplot.png')
            org_plot = cv2.imread('originalplot.png')

            #applys the Equivalizion
            flat = imgArray.flatten()
            histIMG = Hist.get_histogram(flat, 256)
            cs = Hist.sum(histIMG)

            newIMG = cs[flat]

            #Displays the histogram after the Equivalizaion has been applied
            plt.hist(newIMG,256,[0,256], color = 'r')
            plt.xlim([0,256])
            plt.savefig('equivalizedplot.png')
            equ_plot = cv2.imread('equivalizedplot.png')

            #Reshapes the flatten np array of Equivalized img into the same size of the input image then displayed
            newIMG = np.reshape(newIMG, img.shape)

            cv2.imshow('Original Image Histogram Plot', org_plot)
            cv2.imshow('Equivalized Image Histogram Plot', equ_plot)
            cv2.imshow('Original Image',img)
            cv2.imshow('Equivalized Image',newIMG)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except IOError:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
