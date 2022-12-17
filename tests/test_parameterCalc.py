
from parameterCalc import *
import math
import pytest

# Pytest function
def test_temperature():
    # Make sure that temperture is being read from table properly
    assert get_temperature(1000) == pytest.approx(TEMPERATURE_TABLE[1000])
    assert get_temperature(1500) >= TEMPERATURE_TABLE[2000] and get_temperature(1500) <= TEMPERATURE_TABLE[1000]

def test_speed_of_sound():
    # Make sure speed of sound is being calculating properly
    assert get_speed_of_sound(2000) == pytest.approx(math.sqrt(get_temperature(2000) * GAS_CONSTANT * SPECIFIC_HEAT_RATIO))
    assert get_speed_of_sound(2532) == pytest.approx(math.sqrt(get_temperature(2532) * GAS_CONSTANT * SPECIFIC_HEAT_RATIO))

def test_mach_number():
    # Make sure that mach number is being calculated properly
    assert get_mach_number(3000, 100) == pytest.approx(100 / get_speed_of_sound(3000))
    assert get_mach_number(2523, 56) == pytest.approx(56 / get_speed_of_sound(2523))

def test_geopotential():
    # Make sure that geopotential altitude is being calculated properly
    assert get_geopotential_altitude(4342) == pytest.approx((RADIUS_EARTH * 4342) / (RADIUS_EARTH + 4342))
    
def test_pressure():
    # Make sure that atmospheric pressure is being calculated properly
    assert get_pressure(0) == pytest.approx(101325)
    assert 89800 <= get_pressure(1000) <= 89950
    assert 49400 <= get_pressure(5652) <= 49550
    assert get_pressure(11000) == pytest.approx(22632.10)
    assert 16500 <= get_pressure(13000) <= 16650
    assert 13550 <= get_pressure(14236) <= 13750
    
def test_density():
    # Make sure that density is being calculated properly
    assert get_density(8000) == pytest.approx(get_pressure(8000) * MOLAR_MASS / UNI_GAS_CONSTANT / get_temperature(8000))
    assert 1.0 <= get_density(1000) <= 1.225
    assert 1.2<= get_density(0) <= 1.3

def test_dynamic_viscosity():
    # Make sure that dynamic viscosity is being calculated properly
    assert get_dynamic_viscosity(2321) == pytest.approx(KINEMATIC_VISCOSITY / get_density(2321))

def test_dynamic_pressure():
    # Make sure that dynamic pressure is being calculated properly
    assert get_dynamic_pressure(3421, 123) == pytest.approx(0.5 * get_density(3421) * 123 ** 2)
