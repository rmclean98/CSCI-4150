import cv2
import numpy as np
from PIL import Image
from MessageBox import MessageBox
from matplotlib import pyplot as plt
from Hist import *

class ProcessHistogramSpecification:



    def ProcessTransformation(inputFile1, inputFile2):


        try:
            #If not a inputfiles are not valid image file, the control will navigate to exception clause 
            im=Image.open(inputFile1)
            im=Image.open(inputFile2)
            # Load the images in greyscale
            original = cv2.imread(inputFile1,0)
            specified = cv2.imread(inputFile2,0)

            # perform Histogram Matching
            a = ProcessHistogramSpecification.hist_match(original, specified)

            # Display the image

            cv2.imshow('Original',original)
            hist,bins = np.histogram(original.flatten(),256,[0,256])
            plt.hist(original.flatten(),256,[0,256], color = 'r')
            plt.xlim([0,256])
            plt.savefig('HistMatch_originalplot.png')
            org_plot = cv2.imread('HistMatch_originalplot.png')
            cv2.imshow('Original Image Histogram Plot', org_plot)
            cv2.imshow('Specified',specified)
            hist,bins = np.histogram(specified.flatten(),256,[0,256])
            plt.hist(specified.flatten(),256,[0,256], color = 'r')
            plt.xlim([0,256])
            plt.savefig('HistMatch_Specifiedplot.png')
            spec_plot = cv2.imread('HistMatch_Specifiedplot.png')
            cv2.imshow('Specified Image Histogram Plot', spec_plot)
            result= np.array(a,dtype='uint8')
            cv2.imshow('Result',result)
            hist,bins = np.histogram(result.flatten(),256,[0,256])
            plt.hist(result.flatten(),256,[0,256], color = 'r')
            plt.xlim([0,256])
            plt.savefig('HistMatch_Resultplot.png')
            result_plot = cv2.imread('HistMatch_Resultplot.png')
            cv2.imshow('Result Image Histogram Plot', result_plot)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # do stuff
        except IOError:

            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')



    def hist_match(original, specified):

        oldshape = original.shape
        original = original.ravel()
        specified = specified.ravel()

        # get the set of unique pixel values and their corresponding indices and counts
        s_values, bin_idx, s_counts = np.unique(original, return_inverse=True,return_counts=True)
        t_values, t_counts = np.unique(specified, return_counts=True)

        # Calculate s_k for original image
        s_quantiles = Hist.sum(s_counts).astype(np.float64)
        s_quantiles /= s_quantiles[-1]

        # Calculate s_k for specified image
        t_quantiles = Hist.sum(t_counts).astype(np.float64)
        t_quantiles /= t_quantiles[-1]

        # Round the values
        sour = np.around(s_quantiles*255)
        temp = np.around(t_quantiles*255)

        # Uses the lookup function to get the intensity cahnges 
        b=[]
        for data in sour[:]:
            b.append(ProcessHistogramSpecification.Lookup(temp,data))
        b= np.array(b,dtype='uint8')

        return b[bin_idx].reshape(oldshape)

    #Function to lookup values for intensity change and returns the intensity change
    def Lookup(my_array, target):
        tempIndex = len(my_array)-1
        tempValue = len(my_array)-1
        i = len(my_array)-1
        while (i >= 0):
            if (my_array[i] <= target):
                if(target < tempValue):
                    tempValue = target
                    tempIndex = i
            i -= 1

        return tempIndex
