import numpy as np
from PIL import Image
from ImportFile import *
from MainWindow import MainWindow
from UserEventResponse import UserEventResponse
import math
import argparse
import textwrap
import sys

lut=np.empty(256)
show=0

#lomoTrackerCallback Function splits the picture provided into 3 channels.
#Modifys the red channel based on the slider poition.
#Merges the 3 channels back into a picture.
def lomoTrackerCallback(x):
    pos = cv2.getTrackbarPos('Lomo','Image')
    lomo_param=pos/100
    if lomo_param< 0.08:
        lomo_param=0.08
    lut = np.array([round( 256 * (1/(1 + math.exp(-(((i/256.0)-0.5)/lomo_param)) )) )
    		for i in np.arange(0, 256)]).astype("uint8")
    b,g,r = cv2.split(img)
    cv2.LUT(r, lut, r)
    equ = cv2.merge((b,g,r))
    show=1
    if(x == "pass"):
        return equ
    displayChangedImage(equ,'Image')
    

#haloTrackerCallback Function copys the image and creates a new float32 numpy array and filled all values to .75
#Then creates a circle based off the Halo Silder and fills the circle with white.
#Then it blurs the circle numpy array, converts the copy of the image to a float32 the multiplies them together
#Then converts the result of multipling they two images together into uint8 numpy array
def haloTrackerCallback(x):
    radius = None
    imgCopy = None
    pos = cv2.getTrackbarPos('Halo','Image')
    if(cv2.getTrackbarPos('Lomo','Image') == 0):
        imgCopy = img.copy()
    else:
        lomo = lomoTrackerCallback("pass")
        imgCopy = lomo.copy()
    height, width = imgCopy.shape[:2]
    haloArray = np.full([height, width, 3], 0.75, dtype=np.float32)
    minHeight = int((height * (pos/100))/2)
    minWidth = int((width * (pos/100))/2)
    if(minHeight < minWidth):
        radius = minHeight
    else:
        radius = minWidth
    cx, cy = int(width/2), int(height/2)
    cv2.circle(haloArray,(cx,cy), radius, (1,1,1), -1)
    blurHalo = cv2.blur(haloArray, (radius, radius))
    imgCopy = imgCopy.astype(np.float32)
    imgCopy /= 255
    finalimg = None
    finalimg = cv2.multiply(imgCopy, blurHalo, finalimg)
    finalimg *= 255
    finalimg = finalimg.astype(np.uint8)
    show=1
    displayChangedImage(finalimg, 'Image')
    

#displayImage displays the image and has the options to save the image aswell and close the windows
def displayImage(image,windowTitle):
    cv2.imshow(windowTitle,image)
    #'show' variable is used to avoid recursive calling of the same code segment when user moves trackbar.
    if show ==0:
        while(1):
            keyInput=cv2.waitKey(0)
            # Exit Functionality on pressing the key 'q'
            if keyInput == ord('q'):
                    print('exitting loop')
                    cv2.destroyAllWindows()
                    sys.exit()
            
            # Save Functionality on pressing the key 's'
            if keyInput == ord('s'):
                app = QApplication([])
                mainWindow = MainWindow()
                mainWindow.setWindowTitle('File Save Dialog')
                mainWindow.show()
                app.exec_()
    
                try:
                    if os.path.exists('fileNameTracker.txt'):
                        fileName = open("fileNameTracker.txt", "r")
                        userText=str(fileName.read())
                        if userText!='cancel':
                            cv2.imwrite(userText + '.png', image)
                            fileName.close()
                            os.remove('fileNameTracker.txt')
    
                except IOError:
                    print('Error:Unable to Proceed Further. Restart the Program')

#The changed Image as per the halo and lomo trackbar values is displayed here.
def displayChangedImage(image,windowTitle):
    cv2.imshow(windowTitle,image)
  


if __name__ == '__main__':
    parser = argparse.ArgumentParser(epilog=textwrap.dedent('Please read the user instructions document \"ReadMe.pdf\" for more details'),formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('filename', metavar='', type=str, nargs='?',help='Input file path')
    args = parser.parse_args()
    try:
        if(len(sys.argv) > 1):
            inputFile=sys.argv[1]
        else:
            print('Not enough arguments passed, use -h to see help')
            sys.exit()
        im=Image.open(inputFile)
        img = cv2.imread(inputFile)
        cv2.namedWindow('Image',cv2.WINDOW_GUI_NORMAL)
        cv2.createTrackbar('Lomo','Image',0,20,lomoTrackerCallback)
        cv2.createTrackbar('Halo','Image',0,100,haloTrackerCallback)
        show=0
        displayImage(img,'Image')
        cv2.waitKey(0)


    except IOError:
        print('Please provide a valid Image File Path')
