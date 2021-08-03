from __future__ import print_function
from __future__ import division
import cv2 as cv
import sys

colorSliderMax = 20
haloEffectMax = 100
title_window = 'Lomographic filter'

def on_trackbar1(val):

    cv.imshow(title_window)

def on_trackbar2(val):
    alpha = val / haloEffectMax
    beta = ( 1.0 - alpha )
    dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
    cv.imshow(title_window, dst)

if(len(sys.argv) > 2):
    print('To many arguments used')
    exit()

if(sys.argv[1] == '-h'):
    print("Usage is lomo.py [PICTURE_PATH]")
    exit()

src = cv.imread(cv.samples.findFile(sys.argv[1]))

if src is None:
    print('Could not open or find the image: ', sys.argv[1])
    exit(0)

cv.namedWindow(title_window)
cv.imshow('Original Image', src)

trackbar_name1 = 'Alpha x %d' % colorSliderMax
trackbar_name2 = 'Alpha1 x %d' % haloEffectMax
cv.createTrackbar(trackbar_name1, title_window , 0, colorSliderMax, on_trackbar1)
cv.createTrackbar(trackbar_name2, title_window , 1, haloEffectMax, on_trackbar2)

# Show some stuff
on_trackbar1(1)
on_trackbar2(100)
# Wait until user press some key
cv.waitKey()
