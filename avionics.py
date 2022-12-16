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

def draw_airspeed(airspeed: float, scale: float, base: np.array, dial: np.array) -> np.array:
    h, w = base.shape[:2]
    dims = [w, h]
    middle = [h/2, w/2]
    angle = airspeed * -0.77
    rot = cv2.getRotationMatrix2D(middle, angle, 1)
    dial = cv2.warpAffine(dial, rot, dims)
    result = overlay(base, dial)
    return result

def draw_altimeter(altitude: float, scale: float, base: np.array, dial_10km: np.array, dial_1km: np.array, dial_100m: np.array) -> np.array:
    h, w = base.shape[:2]
    dims = [w, h]
    middle = [h/2, w/2]

    tens = altitude // 10000
    kms = (altitude % 10000) // 1000
    ms = altitude % 1000

    tens_angle = -36 * tens
    kms_angle = -36 * kms
    ms_angle = -0.36 * ms

    rot_tens = cv2.getRotationMatrix2D(middle, tens_angle, 1)
    rot_kms = cv2.getRotationMatrix2D(middle, kms_angle, 1)
    rot_ms = cv2.getRotationMatrix2D(middle, ms_angle, 1)

    dial_10km = cv2.warpAffine(dial_10km, rot_tens, dims)
    dial_1km = cv2.warpAffine(dial_1km, rot_kms, dims)
    dial_100m = cv2.warpAffine(dial_100m, rot_ms, dims)

    
    inter = overlay(base, dial_10km)
    inter = overlay(inter, dial_1km)
    result = overlay(inter, dial_100m)
    return result



def draw_horizon(roll: float, pitch: float, scale: float, base: np.array, outer: np.array, roll_ind: np.array, pit_ind: np.array) -> np.array :
    n = len(base)
    dims = np.array([n, n])
    middle = dims / 2

    rot = cv2.getRotationMatrix2D(middle, -roll, 1)
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


