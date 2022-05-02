#FIXME: not modified yet
import skimage
from skimage.segmentation import watershed
import cv2
from matplotlib import pyplot as plt
import numpy as np
import copy

def SeededWatershed (seed, flat):
    """
    input: 
           
    output: segmentation mask. Each cell is marked with a different number; background is 0
    
    The seed used for seeded watershed is the center of each nucleus, labeled with a unique nonzero number
    """
    
    # Seed obtained. Now doing seeded watershed
    
    ## convert to grey-scale image by summing intensities across all channels
    # flat = comp.sum(axis = 2) # default dtype: uint64
    
    ## inverting to make boundaries between between the cells. Watershed circles out area along the highest altitude, so inverting can help circle out each cell instead of internal structure or background
    # flat = flat.astype('uint16') # see how skimage.util.invert inverts. uint8 causes overflow because max of sum can be > 255
    flat_inv = skimage.util.invert(flat)
    
    ## Take a look
    # print('comp')
    # plt.imshow(comp)
    plt.show()
    print('flat')
    plt.imshow(flat)
    plt.show()
    print('flat_inv')
    plt.imshow(flat_inv)
    plt.show()

    ## Segmentation
    seg = watershed(flat_inv,markers = seed)
    
    ## Take a look
    print('seg')
    plt.imshow(seg)
    plt.show()
    
    # subtract background from seeded watershed mask
    ret, thresh = cv2.threshold(flat,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    ## noise removal 
    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

    ## sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations = 2)
    print('background')
    plt.imshow(sure_bg)
    plt.show()
    
    
    ## set background to 0
    seg[sure_bg == 255] = 0
    
    ## Take a look
    print('seg without background')
    plt.imshow(seg)
    plt.show()
    
    return seg

    