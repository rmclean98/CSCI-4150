import cv2
import numpy as np
from PIL import Image
from MessageBox import MessageBox
from matplotlib import pyplot as plt
#from matplotlib.backends.backend_agg import FigureCanvasAgg as canvas
#from matplotlib.figure import Figure

class ProcessHistogramEquivalization:



    def ProcessTransformation(inputFile):

        try:
            img = cv2.imread(inputFile, 0)
            hist,bins = np.histogram(img.flatten(),256,[0,256])
            plt.hist(img.flatten(),256,[0,256], color = 'r')
            plt.xlim([0,256])
            #plt.show()
            plt.savefig('originalplot.png')
            org_plot = cv2.imread('originalplot.png')
            #b,g,r = cv2.split(img)
            #equ_b = cv2.equalizeHist(b)
            #equ_g = cv2.equalizeHist(g)
            #equ_r = cv2.equalizeHist(r)
            #equ = cv2.merge((equ_b, equ_g, equ_r))
            equ = cv2.equalizeHist(img)
            hist,bins = np.histogram(equ.flatten(),256,[0,256])
            plt.hist(equ.flatten(),256,[0,256], color = 'r')
            plt.xlim([0,256])
            plt.savefig('equivalizedplot.png')
            img_plot = cv2.imread('originalplot.png')
            equ_plot = cv2.imread('equivalizedplot.png')
            #plt.savefig('Equivalizedplot.png')
            cv2.imshow('Original', img)
            cv2.imshow('Original Image Histogram Plot', org_plot)
            cv2.imshow('Equivalized Image Histogram Plot', equ_plot)
            cv2.imshow('Equivalized', equ)
            k = cv2.waitKey(0)
            if k == 27:         # wait for ESC key to exit
                cv2.destroyAllWindows()

        except IOError:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
