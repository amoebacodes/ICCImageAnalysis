import cv2
from matplotlib import pyplot as plt
import numpy as np

def getSeeds(nuc_img):
    ## threshold to exclude background
    otsu_value, nuc_img_th = cv2.threshold(nuc_img, 0, 255, cv2.THRESH_OTSU) 
    ### editing mask
    kernel = np.ones((3,3), np.uint8)
    nuc_img_open = cv2.morphologyEx(nuc_img_th,cv2.MORPH_OPEN, kernel, iterations = 3)
    nuc_img_closed = cv2.morphologyEx(nuc_img_open,cv2.MORPH_CLOSE,kernel, iterations = 4)
      
    ## Take a look
    print('nuc_img')
    plt.imshow(nuc_img)
    plt.show()
    print('nuc_img_th')
    plt.imshow(nuc_img_th)
    plt.show()
    print('nuc_img_open')
    plt.imshow(nuc_img_open)
    plt.show()
    print('nuc_img_closed')
    plt.imshow(nuc_img_closed)
    plt.show()
    
    ## assign numbers to each connected components; 0 == background
    retval,nuc_img_connected = cv2.connectedComponents(nuc_img_closed)
        
    ## Take a look
    print('nuc_img_connected')
    plt.imshow(nuc_img_connected)
    plt.show()
    
    ## compress nuc_img_connected to seed
    marked_nuc = np.empty((nuc_img.shape[0],nuc_img.shape[1],3)).astype('uint8') # for visualization
    for i in range(len(nuc_img)):
        for j in range(len(nuc_img[0])):
            marked_nuc[i,j]= [round(nuc_img[i,j]) for k in range(3)]

    seed = np.zeros(nuc_img_connected.shape) # sparse matrix with values marking centers of nuclei; dtype = float64
    for i in range(1,np.max(nuc_img_connected) + 1): # not marking background so starting from 1
        location = np.where(nuc_img_connected == i)
        mid_y = int((np.max(location[0]) + np.min(location[0])) / 2)
        mid_x = int((np.max(location[1]) + np.min(location[1])) / 2)
        seed[mid_y,mid_x] = i
        marked_nuc[mid_y:(mid_y + 30), mid_x:(mid_x + 30)] = [0,255,0] # for visualization
    
    ## Take a look
    print('marked_nuc')
    plt.imshow(marked_nuc)
    plt.show()
    return seed
