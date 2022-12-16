
from typing import Protocol
import math
import pytest

# Global Variables
SPECIFIC_HEAT_RATIO = 1.4 
RADIUS_EARTH = 6367474 # m
TEMPERATURE_TABLE = {-2000: 301.15,
                     -1000: 294.65,
                         0: 288.15,
                      1000: 281.65,
                      2000: 275.15,
                      3000: 268.65,
                      4000: 262.15,
                      5000: 255.65,
                      6000: 249.15,
                      7000: 242.65,
                      8000: 236.15,
                      9000: 229.65,
                     10000: 223.15,
                     11000: 219.90,
                     12000: 216.65,
                     13000: 216.65,
                     14000: 216.65,
                     15000: 216.65}
GRAVITY = 9.80665 # m/s^2
MOLAR_MASS = 0.0289644 # kg/mol
UNI_GAS_CONSTANT = 8.31444598 # J/molK
GAS_CONSTANT = UNI_GAS_CONSTANT / MOLAR_MASS # J/kgK
KINEMATIC_VISCOSITY = 1.48 * 10 ** -4 # m^2/s

# Uses temperature table to linearlly interpolate the temperature at altitude
def get_temperature(altitude: float) -> float: # Kelvin
    low_alt = int(math.floor(altitude / 1000) * 1000)
    high_alt = int(math.ceil(altitude / 1000) * 1000)
    low_temp = TEMPERATURE_TABLE[low_alt]
    high_temp = TEMPERATURE_TABLE[high_alt]
    
    if (high_alt - low_alt != 0):
        temperature = low_temp + (altitude - low_alt) * (high_temp - low_temp) / (high_alt - low_alt)
    else:
        temperature = low_temp
    return temperature

# Get's speed of sound at altitude
def get_speed_of_sound(altitude: float) -> float: # m / s
    temperature = get_temperature(altitude)
    speedOfSound = math.sqrt(temperature * GAS_CONSTANT * SPECIFIC_HEAT_RATIO) 
    return speedOfSound

# Calculates the geopotential altitude
def get_geopotential_altitude(altitude: float) -> float: # m
    geoPotential = (RADIUS_EARTH * altitude) / (RADIUS_EARTH + altitude)
    return geoPotential

# Calculates ambient pressure at altitude
def get_pressure(altitude: float) -> float: # Pa
    
    if (altitude < 11000):
        refPressure = 101325
        refAltitude = 0
        tempLapseRate = -0.0065
    else:
        refPressure = 22632.10
        refAltitude = 11000
        tempLapseRate = 0
    
    refTemp = get_temperature(refAltitude)
    
    if (tempLapseRate == 0):
        pressure = refPressure * math.exp(-GRAVITY * MOLAR_MASS * (altitude - refAltitude) / UNI_GAS_CONSTANT / refTemp)
    else:
        pressure = refPressure * ((refTemp + (altitude - refAltitude) \
                                   * tempLapseRate) / refTemp) ** (-GRAVITY * MOLAR_MASS / UNI_GAS_CONSTANT / tempLapseRate)
    
    return pressure

# Calculates air density at altitude
def get_density(altitude: float) -> float: # kg/m^3
    density = get_pressure(altitude) * MOLAR_MASS / UNI_GAS_CONSTANT / get_temperature(altitude)
    
    return density

# Calculates the dynamic pressure at altitude given a velocity
def get_dynamic_pressure(altitude: float, velocity: float) -> float:
    dynamic_pressure = 0.5 * get_density(altitude) * velocity ** 2
    return dynamic_pressure

# Get's dynamic viscosity at altitude
def get_dynamic_viscosity(altitude: float) -> float:
    dynamic_viscosity = KINEMATIC_VISCOSITY / get_density(altitude)
    return dynamic_viscosity

# Get's Mach number at altitude
def get_mach_number(altitude: float, velocity: float) -> float:
    mach_number = velocity / get_speed_of_sound(altitude)
    return mach_number

    
