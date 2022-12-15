import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import cv2

def overlay(back: np.array, fore: np.array) -> np.array :
    alpha_channel = fore[:, :, 3] / 255 
    overlay_colors = fore[:, :, :3]
    alpha_mask = np.dstack((alpha_channel, alpha_channel, alpha_channel))
    result = back * (1 - alpha_mask) + overlay_colors * alpha_mask
    return result


def get(roll: float, pitch: float, scale: float, base: np.array, outer: np.array, roll_ind: np.array, pit_ind: np.array) -> np.array :
    n = len(base)
    dims = np.array([n, n])
    middle = dims / 2

    rot = cv2.getRotationMatrix2D(middle, roll, 1)
    pitch_trans = np.array([
        [1, 0, 0],
        [0, 1, pitch*3.5]
    ])
    
    #translate pitch indicator image by pitch angle * 3.5 (degrees to pixels)
    pit_ind = cv2.warpAffine(pit_ind, pitch_trans, dims)
    #overlay pitch indicator on base
    inter1 = overlay(base, pit_ind)
    #rotate base+pitch by roll angle
    inter1 = cv2.warpAffine(inter1, rot, dims)
    #rotate roll indicator to roll angle
    roll_ind = cv2.warpAffine(roll_ind, rot, dims)
    #overlay roll indicator on
    inter2 = overlay(inter1, roll_ind)
    final = overlay(inter2, outer)
    final = cv2.resize(final, None, fx = scale, fy = scale, interpolation= cv2.INTER_CUBIC)
    return final


