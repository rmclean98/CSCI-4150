import cv2
from PIL import Image
from MessageBox import MessageBox

class ImageNegativeTransformation:  
    
        
    
    def ProcessTransformation(inputFile):
        
        try:
            im=Image.open(inputFile)
            img = cv2.imread(inputFile)
            cv2.imshow("Original Image",img)             
            img_not = cv2.bitwise_not(img)
            cv2.imshow("ImageNegative",img_not)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            # do stuff
        except IOError:
            MessageBox.showMessageBox('info','Please provide a valid Image File Path to Transform')
        