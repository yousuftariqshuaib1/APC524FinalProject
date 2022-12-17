
from dynamics import *
import numpy as np

def test_f():
    # Setting up a variety of test states
    teststate1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    teststate2 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    teststate3 = np.random.rand(12)
    
    # Setting up a variety of test controls
    testcontrol1 = np.array([0, 0, 0, 0])
    testcontrol2 = np.array([2, 2, 2, 2])
    testcontrol3 = np.random.rand(4)
    
    # Setting up a variety of delta t's
    delta_t1 = 0
    delta_t2 = 1
    delta_t3 = 1.5
    
    # Ensuring that state doesn't update from delta_t = 0
    assert np.array_equal(step(teststate1, testcontrol1, delta_t1), np.zeros(12))
    assert np.array_equal(step(teststate2, testcontrol1, delta_t1), teststate2)
    assert np.array_equal(step(teststate1, testcontrol2, delta_t1), np.zeros(12))
    
    # Ensuring that with a zero intial state, state is entirely dependent on control input
    assert np.allclose(step(teststate1, testcontrol2, delta_t2), np.matmul(B_MAT, testcontrol2))
    assert np.allclose(step(teststate1, testcontrol2, delta_t3), delta_t3 * np.matmul(B_MAT, testcontrol2))
    
    # Ensuring that with zero control input, the state is entirely dependent on the intial state
    assert np.allclose(step(teststate2, testcontrol1, delta_t2), teststate2 + np.matmul(A_MAT, teststate2))
    assert np.allclose(step(teststate2, testcontrol1, delta_t3), teststate2 + delta_t3 * np.matmul(A_MAT, teststate2))
    
    # Ensuring that the control and state work well togther
    assert np.allclose(step(teststate2, testcontrol2, delta_t2), teststate2 + np.matmul(A_MAT, teststate2) + np.matmul(B_MAT, testcontrol2))
    assert np.allclose(step(teststate2, testcontrol2, delta_t3), teststate2 + delta_t3 \
                      * (np.matmul(A_MAT, teststate2) + np.matmul(B_MAT, testcontrol2)))
    assert np.allclose(step(teststate3, testcontrol3, delta_t2), teststate3 + np.matmul(A_MAT, teststate3) + np.matmul(B_MAT, testcontrol3))
    assert np.allclose(step(teststate3, testcontrol3, delta_t3), teststate3 + delta_t3 \
                      * (np.matmul(A_MAT, teststate3) + np.matmul(B_MAT, testcontrol3)))
    
