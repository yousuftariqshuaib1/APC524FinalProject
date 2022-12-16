import math
import numpy as np
from PIL import Image

def GPS_plotter(state: np.array, plane, background):
    background_temp = background.copy()
    width_b, height_b = background_temp.size
    width_p, height_p = plane.size
    
    x_pos = int(width_b / 2 + state[3] / 20 - width_p/2)
    y_pos = int(height_b / 2 - state[4] / 20 - width_p/2)
    
    plane_rotated = plane.rotate(state[11]-90 expand = 1)
    background_temp.paste(plane_rotated, (x_pos,y_pos), plane_rotated)
    
    return background_temp
