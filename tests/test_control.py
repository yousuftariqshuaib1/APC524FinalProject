
from control import *
import pytest
from pynput.keyboard import Key, Controller

test_keyboard = Controller()
def test_noinput():
    #test case for no user input
    test_control_vec1 = [0.0, 0.0, 0.0, 0.0]
    test_control_vec2 = [.7, .5, .5, .5]
    assert np.allclose(update(test_control_vec1), np.array([0., 0.0, 0.0, 0.0]))
    assert np.allclose(update(test_control_vec2), np.array([.5, .3, .3, .5]))

def test_w_pressed():
    test_control_vec1 = [0.0, 0.0, 0.0, 0.0]
    test_control_vec2 = [.7, .5, .5, .5]
    
    # Test that elevator moves when w is pressed
    with test_keyboard.pressed('w'):
        assert np.allclose(update(test_control_vec1), np.array([-0.1, 0., 0., 0.]))
        assert np.allclose(update(test_control_vec2), np.array([0.6, 0.3, 0.3, 0.5]))
        time.sleep(1) 
    
    # Test that it returns back to normal
    assert np.allclose(update(test_control_vec1), np.array([0., 0., 0., 0.]))
    assert np.allclose(update(test_control_vec2), np.array([0.4, 0.1, 0.1, 0.5]))
    
def test_s_pressed():
    test_control_vec1 = [0.0, 0.0, 0.0, 0.0]
    test_control_vec2 = [.7, .5, .5, .5]
    
    # Test that elevator moves when s is pressed
    with test_keyboard.pressed('s'):
        assert np.allclose(update(test_control_vec1), np.array([0.1, 0., 0., 0.]))
        assert np.allclose(update(test_control_vec2), np.array([0.8, 0.3, 0.3, 0.5]))
        time.sleep(1) 
    
    # Test that it returns back to normal
    assert np.allclose(update(test_control_vec1), np.array([0.0, 0., 0., 0.]))
    assert np.allclose(update(test_control_vec2), np.array([0.6, 0.1, 0.1, 0.5]))
    
def test_q_pressed():
    test_control_vec1 = [0.0, 0.0, 0.0, 0.0]
    test_control_vec2 = [.7, .5, .5, .5]
    
    # Test that aileron moves when s is pressed
    with test_keyboard.pressed('q'):
        assert np.allclose(update(test_control_vec1), np.array([0.0, 0., 0.1, 0.]))
        assert np.allclose(update(test_control_vec2), np.array([0.5, 0.3, 0.6, 0.5]))
        time.sleep(1) 
    
    # Test that it returns back to normal
    assert np.allclose(update(test_control_vec1), np.array([0.0, 0., 0., 0.]))
    assert np.allclose(update(test_control_vec2), np.array([0.3, 0.1, 0.4, 0.5]))
    
def test_e_pressed():
    test_control_vec1 = [0.0, 0.0, 0.0, 0.0]
    test_control_vec2 = [.7, .5, .5, .5]
    
    # Test that elevator moves when s is pressed
    with test_keyboard.pressed('e'):
        assert np.allclose(update(test_control_vec1), np.array([0.0, 0., -0.1, 0.]))
        assert np.allclose(update(test_control_vec2), np.array([0.5, 0.3, 0.4, 0.5]))
        time.sleep(1) 
    
    # Test that it returns back to normal
    assert np.allclose(update(test_control_vec1), np.array([0., 0., 0., 0.]))
    assert np.allclose(update(test_control_vec2), np.array([0.3, 0.1, 0.2, 0.5]))
    
def test_d_pressed():
    test_control_vec1 = [0.0, 0.0, 0.0, 0.0]
    test_control_vec2 = [.7, .5, .5, .5]
    
    # Test that elevator moves when s is pressed
    with test_keyboard.pressed('d'):
        assert np.allclose(update(test_control_vec1), np.array([0.0, -0.1, 0., 0.]))
        assert np.allclose(update(test_control_vec2), np.array([0.5, 0.4, 0.3, 0.5]))
        time.sleep(1) 
    
    # Test that it returns back to normal
    assert np.allclose(update(test_control_vec1), np.array([0.0, 0., 0., 0.]))
    assert np.allclose(update(test_control_vec2), np.array([0.3, 0.2, 0.1, 0.5]))
    
def test_a_pressed():
    test_control_vec1 = [0.0, 0.0, 0.0, 0.0]
    test_control_vec2 = [.7, .5, .5, .5]
    
    # Test that elevator moves when s is pressed
    with test_keyboard.pressed('a'):
        assert np.allclose(update(test_control_vec1), np.array([0.0, 0.1, 0., 0.]))
        assert np.allclose(update(test_control_vec2), np.array([0.5, 0.6, 0.3, 0.5]))
        time.sleep(1) 
    
    # Test that it returns back to normal
    assert np.allclose(update(test_control_vec1), np.array([0.0, 0., 0., 0.]))
    assert np.allclose(update(test_control_vec2), np.array([0.3, 0.4, 0.1, 0.5]))

def test_up_pressed():
    test_control_vec1 = [0.0, 0.0, 0.0, 0.0]
    test_control_vec2 = [.7, .5, .5, .5]
    
    # Test that elevator moves when s is pressed
    with test_keyboard.pressed(Key.up):
        assert np.allclose(update(test_control_vec1), np.array([0.0, 0., 0., 1.]))
        assert np.allclose(update(test_control_vec2), np.array([0.5, 0.3, 0.3, 1.5]))
        time.sleep(1) 
    
    # Test that it returns back to normal
    assert np.allclose(update(test_control_vec1), np.array([0.0, 0., 0., 1.]))
    assert np.allclose(update(test_control_vec2), np.array([0.3, 0.1, 0.1, 1.5]))
    
def test_down_pressed():
    test_control_vec1 = [0.0, 0.0, 0.0, 0.0]
    test_control_vec2 = [.7, .5, .5, 5]
    
    # Test that elevator moves when s is pressed
    with test_keyboard.pressed(Key.down):
        assert np.allclose(update(test_control_vec1), np.array([0.0, 0., 0., 0.]))
        assert np.allclose(update(test_control_vec2), np.array([0.5, 0.3, 0.3, 4.]))
        time.sleep(1) 
    
    # Test that it returns back to normal
    assert np.allclose(update(test_control_vec1), np.array([0.0, 0., 0., 0.]))
    assert np.allclose(update(test_control_vec2), np.array([0.3, 0.1, 0.1, 4.]))
