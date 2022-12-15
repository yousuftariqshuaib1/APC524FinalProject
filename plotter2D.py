
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data
import cv2

def GPS_Plotter(state: np.array, image):
    fig, ax = plt.subplots()
    height, width = image.shape[:2]
    center = (width/2, height/2)
    
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=-state[11], scale=1)
    rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))
    
    im = OffsetImage(rotated_image, zoom=0.05)
    
    ab = AnnotationBbox(im, (state[3], state[4]), xycoords='data', frameon=False)
    ax.add_artist(ab)
    ax.set_xlim(-5000.0, 5000.0)
    ax.set_ylim(-5000.0, 5000.0)
    title = "Altitude: "
    title = title + str(state[5])
    plt.title(title)
    
    plt.savefig('images/GPSPlot.jpg')
    plt.close(fig)
    
    
