import numpy as np
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import skimage
from scipy.ndimage import filters
import cv2 as cv
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean


file = r'C:\Users\sarat\OneDrive\Documents\data\marketing_project\Saint John\SaintJohn_7cm_aerialImage.tif'

image = Image.open(file)

image.load()

img_array = np.asarray(image, dtype='int32')


#print(img_array.min(), img_array.max())
#print(img_array[:,:,2])

downsample_value = 15

ds_array = img_array/255

#print(ds_array[:,100,:])

red_array = skimage.measure.block_reduce(ds_array[:,:,0], (downsample_value, downsample_value), np.mean)

green_array = skimage.measure.block_reduce(ds_array[:,:,1], (downsample_value, downsample_value), np.mean)

blue_array = skimage.measure.block_reduce(ds_array[:,:,2], (downsample_value, downsample_value), np.mean)

final_img = np.stack((red_array, green_array, blue_array), axis=-1)

#print(final_img)

stack_img = Image.fromarray((final_img*255).astype(np.uint8))

smooth_img = stack_img.filter(ImageFilter.MedianFilter(size=3))

smooth_img.save(r'C:\Users\sarat\OneDrive\Documents\data\marketing_project\Saint John\smooth_imagery\SaintJohn_15_median_aerialImage_MORE.tif')

#plt.imshow(final_img)
#print()
'''
basewidth = 300
img = Image.open(file)
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('C:/Users/sarat/OneDrive/Documents/data/marketing project/resized_image.jpg')'''