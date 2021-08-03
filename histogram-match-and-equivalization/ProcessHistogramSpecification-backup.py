import cv2
import numpy as np
from PIL import Image
from MessageBox import MessageBox
from matplotlib import pyplot as plt

class ProcessHistogramSpecification:



    def ProcessTransformation(inputFile1, inputFile2):


        try:
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
            k = cv2.waitKey(0)
            if k == 27:         # wait for ESC key to exit
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
        s_quantiles = np.cumsum(s_counts).astype(np.float64)
        s_quantiles /= s_quantiles[-1]

        # Calculate s_k for specified image
        t_quantiles = np.cumsum(t_counts).astype(np.float64)
        t_quantiles /= t_quantiles[-1]

        # Round the values
        sour = np.around(s_quantiles*255)
        temp = np.around(t_quantiles*255)

        # Map the rounded values
        b=[]
        for data in sour[:]:
            b.append(ProcessHistogramSpecification.find_nearest_above(temp,data))
        b= np.array(b,dtype='uint8')

        return b[bin_idx].reshape(oldshape)


    def find_nearest_above(my_array, target):
        diff = my_array - target
        mask = np.ma.less_equal(diff, -1)
        # We need to mask the negative differences
        # since we are looking for values above
        if np.all(mask):
            c = np.abs(diff).argmin()
            return c # returns min index of the nearest if target is greater than any value
        masked_diff = np.ma.masked_array(diff, mask)
        return masked_diff.argmin()
