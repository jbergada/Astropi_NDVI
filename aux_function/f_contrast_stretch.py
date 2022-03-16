import numpy as np

def f_contrast_stretch(im, percentage):
    in_min = np.percentile(im, percentage)
    in_max = np.percentile(im, 100 - percentage)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out