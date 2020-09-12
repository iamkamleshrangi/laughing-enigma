import cv2
import numpy as np

import cv2
import numpy as np

# load color image
im = cv2.imread('1.jpg')

# smooth the image with alternative closing and opening
# with an enlarging kernel
morph = im.copy()

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)
morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

# take morphological gradient
gradient_image = cv2.morphologyEx(morph, cv2.MORPH_GRADIENT, kernel)

# split the gradient image into channels
image_channels = np.split(np.asarray(gradient_image), 3, axis=2)

channel_height, channel_width, _ = image_channels[0].shape

# apply Otsu threshold to each channel
for i in range(0, 3):
    _, image_channels[i] = cv2.threshold(~image_channels[i], 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    image_channels[i] = np.reshape(image_channels[i], newshape=(channel_height, channel_width, 1))

# merge the channels
image_channels = np.concatenate((image_channels[0], image_channels[1], image_channels[2]), axis=2)

# save the denoised image
cv2.imwrite('output.jpg', image_channels)
'''
img_file = '1.jpg'
img = cv2.imread(img_file, cv2.IMREAD_COLOR)
img = cv2.blur(img, (7, 7))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

thresh0 = cv2.adaptiveThreshold(s, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 2)
thresh1 = cv2.adaptiveThreshold(v, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 2)
thresh2 = cv2.adaptiveThreshold(v, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 2)
thresh = cv2.bitwise_or(thresh0, thresh1)

cv2.imshow('Image-thresh0', thresh0)
cv2.waitKey(0)
cv2.imshow('Image-thresh1', thresh1)
cv2.waitKey(0)
cv2.imshow('Image-thresh2', thresh2)
cv2.waitKey(0)
'''
'''
image = cv2.imread("1.jpg",0)
thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)

cv2.imshow('thresh', thresh)
cv2.waitKey(0)
shareedit
'''
'''
img = cv2.imread("1.jpg")
# smoothing the image
img = cv2.medianBlur(img, 5)

#edge detection    
edges = cv2.Canny(img, 100, 200)
cv2.imwrite('output.png', edges)
'''
'''
import cv2
import numpy as np

img = cv2.imread("1.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#mask = cv2.inRange(hsv, (36, 0, 0), (70, 255,255)) #green
mask = cv2.inRange(hsv, (0, 0, 0), (10, 255, 255))
#mask = cv2.inRange(hsv, (125, 0, 0), (135, 255,255))

img = cv2.bitwise_and(img, img, mask=mask)
img[np.where((img == [0,0,0]).all(axis = 2))] = [255,255,255]

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)

cv2.imwrite("out.png", img)
'''
