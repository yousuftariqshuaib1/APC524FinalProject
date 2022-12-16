
import keyboard
import numpy as np

#maximum control surface deflections - test and correct later
#aileron and rudder assumed to be symmetric in travel
# Units are in degrees
MAX_ELEV = 0.5
MIN_ELEV = 0.5
MAX_AIL = 0.5
MAX_RUD = 0.5

# Maximum and minimum thrust of plane
# Units in newtons
MAX_THRUST = 10.0
MIN_THRUST = 0.0

#proportional gain for control input tracking
K_P_ELEV = 0.2
K_P_ELEV_NEG =  0.1
K_P_AIL = 0.2
K_P_AIL_NEG = 0.1
K_P_RUD = 0.2
K_P_RUD_NEG = 0.2
K_P_THRUST = 1.0

def update(control: np.array) -> np.array :
    # Elevator Control
    if keyboard.is_pressed("s"):
        if (control[0] <= MAX_ELEV - K_P_ELEV):
            control[0] += K_P_ELEV
    elif keyboard.is_pressed("w"):
        if (control[0] >= -MIN_ELEV + K_P_ELEV):
            control[0] -= K_P_ELEV
    else:
        if (control[0] <= K_P_ELEV_NEG or control[0] <= -K_P_ELEV_NEG):
            control[0] = 0
        else:
            if (control[0] > 0):
                control[0] -= K_P_ELEV_NEG
            elif (control[0] < 0):
                control[0] += K_P_ELEV_NEG
    
    # Aileron control
    if keyboard.is_pressed("a"):
        if (control[1] <= MAX_AIL - K_P_AIL):
            control[1] += K_P_AIL
    elif keyboard.is_pressed("d"):
        if (control[1] >= -MAX_AIL + K_P_AIL):
            control[1] -= K_P_AIL
    else:
        if (control[1] <= K_P_AIL_NEG or control[1] <= -K_P_AIL_NEG):
            control[1] = 0
        else:
            if (control[1] > 0):
                control[1] -= K_P_AIL_NEG
            elif (control[1] < 0):
                control[1] += K_P_AIL_NEG
    
    # Rudder control
    if keyboard.is_pressed("q"):
        if (control[2] <= MAX_RUD - K_P_RUD):
            control[2] += K_P_RUD
    elif keyboard.is_pressed("e"):
        if (control[2] >= -MAX_RUD + K_P_RUD):
            control[2] -= K_P_RUD
    else:
        if (control[2] <= K_P_RUD_NEG or control[2] <= -K_P_RUD_NEG):
            control[2] = 0
        else: 
            if (control[2] > 0):
                control[2] -= K_P_RUD_NEG
            elif (control[2] < 0):
                control[2] += K_P_RUD_NEG
            
    # Thrust control
    if keyboard.is_pressed("UP"):
        if (control[3] <= MAX_THRUST - K_P_THRUST):
            control[3] += K_P_THRUST
    elif keyboard.is_pressed("DOWN"):
        if (control[3] >= MIN_THRUST + K_P_THRUST):
            control[3] -= K_P_THRUST
            
    return control
