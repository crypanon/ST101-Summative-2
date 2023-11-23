'''
This module loads, manipulate, and displays images
Includes repetition function for tesselating images

'''

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load(path):
    '''
    Get an image in the form of 3d numpy array from the given path
    path: string
        file directory location of the image

    return: 3d numpy ndarray with dtype np.uint8
        image
    '''
    img = Image.open(path, 'r')
    img = np.asarray(img)[:,:,:3].copy()
    return img

def show(img):
    '''
    Show the given image
    img: non-empty 3d numpy ndarray with dtype np.uint8
        image to show
    return: None
    '''
    if type(img) is not np.ndarray:
       raise TypeError("Input must be a numpy ndarray")

    if not img.ndim == 3 or not img.dtype == np.uint8:
       raise TypeError("Input must be a 3d numpy ndarray with dtype np.uint8")

    if img.size == 0:
       raise ValueError("Input array must be non zero")
       
    dpi = 120
    height, width, _ = img.shape
    figsize = (width/dpi, height/dpi)
    fig = plt.figure(figsize = figsize)
    plt.axis('off')
    plt.imshow(img)     
    
def repetition(img, rows, cols):
    '''
    Create an image where the image is repeated (rows x cols) times
    Args:
    img: non-empty 3d numpy ndarray with dtype np.uint8, image to repeat
    rows: number of rows 
    cols: number of columns 
    Returns: 3d numpy ndarray with dtype np.uint8, given image repeated rows x cols times
    '''
    if not isinstance(img, np.ndarray):
        raise TypeError("Input image must be a numpy array")
    if img.ndim != 3 or img.dtype != np.uint8:
        raise ValueError("Input image must be a non-empty 3d numpy ndarray with dtype np.uint8")
    if img.size == 0:
        raise ValueError("Input image must be non-empty")
    if not all(isinstance(i, int) and i > 0 for i in [rows, cols]):
        raise ValueError("m and n must be positive integers")


    h, w, _ = img.shape
    # Create a blank image of the correct scaled dimensions
    repeated_image = np.zeros((h*rows,w*cols,3))

    # Cycling through larger image by smaller image dimensions
    for i in range(rows):
        for j in range(cols):
            # Loop over all copies of image by height and width
            repeated_image[i*h:(i+1)*h,j*w:(j+1)*w,:] = img 
            
    return repeated_image.astype(dtype=np.uint8)