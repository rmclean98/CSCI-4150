import numpy as np
import cv2
from PIL import Image
from MessageBox import MessageBox

class BitPlaneTransformation:

    # Converts the input image to grayscale
    # Applys the BitPlane Transformation by splitting the image into each bit and labels the bits
    def ProcessTransformation(inputFile):

        try:
            im=Image.open(inputFile)
            img = cv2.imread(inputFile, 0)
            cv2.imshow("Original Image",img)
            bitOP = cv2.imread(inputFile, 0)
            lst = []
            for i in range(bitOP.shape[0]):
                    for j in range(bitOP.shape[1]):
                        lst.append(np.binary_repr(bitOP[i][j] ,width=8)) # width = no. of bits

            eightBit = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128).reshape(bitOP.shape[0],bitOP.shape[1])
            sevenBit = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64).reshape(bitOP.shape[0],bitOP.shape[1])
            sixBit = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32).reshape(bitOP.shape[0],bitOP.shape[1])
            fiveBit = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16).reshape(bitOP.shape[0],bitOP.shape[1])
            fourBit = (np.array([int(i[4]) for i in lst],dtype = np.uint8) * 8).reshape(bitOP.shape[0],bitOP.shape[1])
            threeBit = (np.array([int(i[5]) for i in lst],dtype = np.uint8) * 4).reshape(bitOP.shape[0],bitOP.shape[1])
            twoBit = (np.array([int(i[6]) for i in lst],dtype = np.uint8) * 2).reshape(bitOP.shape[0],bitOP.shape[1])
            oneBit = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1).reshape(bitOP.shape[0],bitOP.shape[1])
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(eightBit, "8-bit", (20,15), font, 1, (255,255,255), 2)
            cv2.putText(sevenBit, "7-bit", (20,15), font, 1, (255,255,255), 2)
            cv2.putText(sixBit, "6-bit", (20,15), font, 1, (255,255,255), 2)
            cv2.putText(fiveBit, "5-bit", (20,15), font, 1, (255,255,255), 2)
            cv2.putText(fourBit, "4-bit", (20,15), font, 1, (255,255,255), 2)
            cv2.putText(threeBit, "3-bit", (20,15), font, 1, (255,255,255), 2)
            cv2.putText(twoBit, "2-bit", (20,15), font, 1, (255,255,255), 2)
            cv2.putText(oneBit, "1-bit", (20,15), font, 1, (255,255,255), 2)

            finalrows = cv2.hconcat([eightBit,sevenBit,sixBit,fiveBit])
            finalcols =cv2.hconcat([fourBit,threeBit,twoBit,oneBit])

            final = cv2.vconcat([finalrows,finalcols])

            cv2.imshow("Bit-Plane",final)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            # do stuff
        except IOError:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
