'''
This module loads, manipulate, and displays images

please add your functions in this .py file (and update this docstring)
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
    
def repetition(img, m, n):
    '''
    Create an image where the image is repeated (m x n)times
    img: non-empty 3d numpy ndarray with dtype np.uint8
        image to repeat
    m: number of rows 
    n: number of columns 
    return: 3d numpy ndarray with dtype np.uint8
        given image repeated m x n times
    '''
    if not isinstance(img, np.ndarray):
        raise TypeError("Input image must be a numpy array")
    if img.ndim != 3 or img.dtype != np.uint8:
        raise ValueError("Input image must be a non-empty 3d numpy ndarray with dtype np.uint8")
    if img.size == 0:
        raise ValueError("Input image must be non-empty")
    if not all(isinstance(i, int) and i > 0 for i in [m, n]):
        raise ValueError("m and n must be positive integers")

    h, w, _ = img.shape
    repeated_img = np.tile(img, (m, n, 1))
    return repeated_img 