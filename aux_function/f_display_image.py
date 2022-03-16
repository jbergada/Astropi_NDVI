import numpy as np
import cv2 as cv

def f_display_image(image, image_name):
    image = np.array(image, dtype=float)/float(255)
    shape = image.shape
    height = int(shape[0] / 2)
    width = int(shape[1] / 2)
    image = cv.resize(image, (width, height))
    cv.namedWindow(image_name)
    cv.imshow(image_name, image)
    cv.waitKey(0)
    cv.destroyAllWindows()