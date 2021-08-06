import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2



############### put the name of image here #####################
image_name='4.png'
################################################################


im_data = cv2.imread(image_name)
im_data = cv2.cvtColor(im_data,cv2.COLOR_BGR2RGB)
imgb = cv2.cvtColor(im_data, cv2.COLOR_BGR2GRAY)
# print(im_data)
# print(np.shape(im_data))

# Data in MxN (rarely), MxNx3 (standard RGB), MxNx4 (RGBA)
red_data = im_data[:,:,0]
green_data = im_data[:,:,1]
blue_data = im_data[:,:,2]

# new image - swap RGB order
# image1 = np.array([blue_data, green_data, red_data])
# image1 = np.swapaxes(image1, 0, 1)
# image1 = np.swapaxes(image1, 1, 2)
image1 = cv2.cvtColor(im_data, cv2.COLOR_RGB2BGR)
# print(np.shape(image1))

# # new image - colour tweaked
# image2 = np.array([1.0*green_data, 0.5*red_data, 0.5*blue_data]) # If RGB values are float
# # image2 = np.array([(1.5*green_data)%256, (1.0*red_data)%256, (1.0*blue_data)%256]).astype(np.uint8) # if RGB values are int
# image2 = np.swapaxes(image2, 0, 1)
# image2 = np.swapaxes(image2, 1, 2)
# print(np.shape(image2))

#
# cmap = 'hot'
# cmap = 'gray'
cmap = 'jet'
#
plt.figure(figsize=(10,5))
#
plt.subplot(231)
plt.imshow(im_data, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Original Image in RGB')

plt.subplot(232)
plt.imshow(image1, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Image in BGR')

plt.subplot(233)
plt.imshow(imgb, cmap= 'gray', interpolation='nearest')
plt.axis('off')
plt.title('Image tweaked')

plt.subplot(234)
plt.imshow(red_data, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Red Channel')
plt.colorbar()

plt.subplot(235)
plt.imshow(green_data, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Green Channel')
plt.colorbar()

plt.subplot(236)
plt.imshow(blue_data, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Blue Channel')
plt.colorbar()
#
plt.figure(figsize=(10,5))
plt.subplot(131)
plt.hist(red_data.ravel(), bins=50, fc='red', ec='k')
plt.subplot(132)
plt.hist(green_data.ravel(), bins=50, fc='green', ec='k')
plt.subplot(133)
plt.hist(blue_data.ravel(), bins=50, fc='blue', ec='k')


plt.figure(figsize=(5,5))
# find frequency of pixels in range 0-255
histr = cv2.calcHist([imgb],[0],None,[256],[0,256])

# show the plotting graph of an image
plt.plot(histr)

plt.show()