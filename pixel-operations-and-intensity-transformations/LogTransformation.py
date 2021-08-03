import cv2
import numpy as np
from PIL import Image
from MessageBox import MessageBox

class LogTransformation: 
        
    
    def ProcessTransformation(inputFile):
        try:
            im=Image.open(inputFile)              
            # Open the image. 
            img = cv2.imread(inputFile) 
              
            # Apply log transform. 
            c = 255/(np.log(1 + np.max(img))) 
            log_transformed = c * np.log(1 + img) 
              
            # Specify the data type. 
            log_transformed = np.array(log_transformed, dtype = np.uint8)
            cv2.imshow("Original Image",img)
            cv2.imshow("log_transformed",log_transformed)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except IOError:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')