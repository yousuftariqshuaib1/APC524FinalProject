
import keyboard
import numpy as np
import time

#maximum control surface deflections - test and correct later
#aileron and rudder assumed to be symmetric in travel
# Units are in degrees
MAX_ELEV = 30.0
MIN_ELEV = 20.0
MAX_AIL = 20.0
MAX_RUD = 35.0

# Maximum and minimum thrust of plane
# Units in newtons
MAX_THRUST = 20000.0
MIN_THRUST = 0.0

#proportional gain for control input tracking
K_P_ELEV = 1
K_P_ELEV_NEG =  2
K_P_AIL = 1
K_P_AIL_NEG = 2
K_P_RUD = 1
K_P_RUD_NEG = 2
K_P_THRUST = 200.0

def update(control: np.array) -> np.array :
    # Elevator Control
    if keyboard.is_pressed("w"):
        if (control[0] <= MAX_ELEV - K_P_ELEV):
            control[0] += K_P_ELEV
    elif keyboard.is_pressed("s"):
        if (control[0] >= -MIN_ELEV + K_P_ELEV):
            control[0] -= K_P_ELEV
    else:
        if (abs(control[0]) <= K_P_ELEV_NEG):
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
        if (abs(control[1]) <= K_P_AIL_NEG):
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
        if (abs(control[2]) <= K_P_RUD_NEG):
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

controller = np.array([0.0,0.0,0.0,0.0])
while True:
    time.sleep(0.1)
    print(update(controller))
