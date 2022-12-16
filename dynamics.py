import numpy as np 
from typing import Protocol
#Matrices are taken from Flight Dynamics, by Robert Stengel
#Chapter 4, p. 296
#Linear time-invariant flight model for a business jet

#Dynamics matrix A - influence of state on state
A_MAT =  np.array([
    [ -0.12,      0,  0.096, 0, 0,      0,      0,  -6.45,      0,     0, -9.79,   0], # u
    [     0,  -0.16,      0, 0, 0,      0,   6.45,      0, -101.8,  9.79,     0,   0], # v
    [ -0.12,      0,  -1.28, 0, 0, -0.001,      0,  100.8,      0,     0, -0.62,   0], # w
    [   1.0,      0,   0.06, 0, 0,      0,      0,      0,      0,     0,     0,   0], # x
    [     0,    1.0,      0, 0, 0,      0,      0,      0,      0, -6.45,     0, 102], # y
    [ 0.063,      0,    1.0, 0, 0,      0,      0,      0,      0,     0,  -102,   0], # z
    [     0, -0.025,      0, 0, 0,      0,  -1.18,      0,   0.18,     0,     0,   0], # p
    [ 0.005,      0, -0.078, 0, 0,      0,      0, -1.279,      0,     0,     0,   0], # q
    [     0,  0.017,      0, 0, 0,      0, -0.011,      0, -0.093,     0,     0,   0], # r
    [     0,      0,      0, 0, 0,      0,      1,      0,      0,     0,     0,   0], # roll
    [     0,      0,      0, 0, 0,      0,      0,      1,      0,     0,     0,   0], # pitch
    [     0,      0,      0, 0, 0,      0,      0,      0,  1.002,     0,     0,   0], # yaw
])
#Control matrix B - influence of control inputs on state

# Elevator, Aileron, Rudder, Thrust
B_MAT = np.array([
    [0.0065,     0,     0, 4.67],
    [     0, -0.16,  3.51,    0],
    [-13.17,     0,     0,    0],
    [     0,     0,     0,    0],
    [     0,     0,     0,    0],
    [     0,     0,     0,    0],
    [     0,  2.31,  0.25,    0],
    [ -9.07,     0,     0,    0],
    [     0,  0.12, -1.11,    0],
    [     0,     0,     0,    0],
    [     0,     0,     0,    0],
    [     0,     0,     0,    0]
])
#iterate next state step from x_dot = Ax + Bu
def step(state: np.ndarray, control: np.ndarray, dt: float) -> np.ndarray :
    state_new = state + (dt * (np.matmul(A_MAT, state) + np.matmul(B_MAT, control)))
    return state_new

