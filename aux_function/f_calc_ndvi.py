import cv2 as cv

def f_calc_ndvi(image):
    b, g, r = cv.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.001

    ndvi = (b.astype(float) - r.astype(float)) / bottom
    ndvi[ndvi<=0] = 0;
    
    return ndvi