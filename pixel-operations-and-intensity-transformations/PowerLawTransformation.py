import cv2
import numpy as np
from PIL import Image
from MessageBox import MessageBox

class PowerLawTransformation: 
        
    
    def ProcessTransformation(inputFile, gamma):
        try:
            im=Image.open(inputFile)
            img = cv2.imread(inputFile)
            cv2.imshow("Original Image",img)
             
            # Apply gamma correction. 
            gamma_corrected = np.array(255*(img / 255) ** float(gamma), dtype = 'uint8') 
      
            # Save edited images. 
            #cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected) 
            cv2.imshow("gamma_transformed",gamma_corrected)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except IOError:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')