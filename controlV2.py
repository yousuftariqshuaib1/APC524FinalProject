import keyboard
import numpy as np

#maximum control surface deflections - test and correct later
#aileron and rudder assumed to be symmetric in travel
MAX_ELEV = 0.5
MIN_ELEV = 0.5
MAX_AIL = 0.5
MAX_RUD = 0.5
MAX_THROT = 100.0
MIN_THROT = 0
#proportional gain for control input tracking
K_P = 0.2
#throttle update speed
THROT_SENS = 5

def update(control: np.array) -> np.array :
    ref_stick = np.array([0.2, 0, 0, 0])
    if keyboard.is_pressed("s"):
        ref_stick[0]= MAX_ELEV
    if keyboard.is_pressed("w"):
        ref_stick[0]= -MIN_ELEV
        
    if keyboard.is_pressed("a"):
        ref_stick[1]= MAX_AIL
        
    if keyboard.is_pressed("d"):
        ref_stick[1]= -MAX_AIL
        
    if keyboard.is_pressed("q"):
        ref_stick[2]= MAX_RUD
        
    if keyboard.is_pressed("e"):
        ref_stick[2]= -MAX_RUD

    if keyboard.is_pressed("up arrow"):
        if control[3] < (MAX_THROT - THROT_SENS):
            control[3] += THROT_SENS

    if keyboard.is_pressed("down arrow"):
        if control[3] > (MIN_THROT + THROT_SENS):
            control[3] -= THROT_SENS
    
    err = control - ref_stick
    control = control - err * K_P
    return control