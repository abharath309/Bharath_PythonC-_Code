from skimage import io
import numpy as np
import collections
images = io.imread_collection('/Users/bharath/Downloads/Week13_14/training_files/train3_1.png')


for (image, fn) in zip(images, images.files):
    #print (image)
    #print (fn)
    print (image)
    print (image.shape)
    io.imshow(image)
    
    
    
    
    
    
    
    