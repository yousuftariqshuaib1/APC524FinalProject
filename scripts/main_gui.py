
import PySimpleGUI as sg
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
import avionics
import control
import dynamics
import plotter3D
import plotter2D
import parameterCalc
import math
import controlV2
from pydub import AudioSegment


def main_GUI():
    # Horizon Instrument
    horiz_base = cv2.imread("images/horizon_base.png")
    horiz_outer = cv2.imread("images/horizon_outer.png", cv2.IMREAD_UNCHANGED)
    horiz_roll = cv2.imread("images/horizon_roll.png", cv2.IMREAD_UNCHANGED)
    horiz_pitch = cv2.imread("images/horizon_pitch.png", cv2.IMREAD_UNCHANGED)

    horiz_pitch = cv2.resize(horiz_pitch, None, fx = 0.5, fy = 0.5, interpolation= cv2.INTER_CUBIC)
    horiz_roll = cv2.resize(horiz_roll, None, fx = 0.5, fy = 0.5, interpolation= cv2.INTER_CUBIC)
    horiz_base = cv2.resize(horiz_base, None, fx = 0.5, fy = 0.5, interpolation= cv2.INTER_CUBIC)
    horiz_outer = cv2.resize(horiz_outer, None, fx = 0.5, fy = 0.5, interpolation= cv2.INTER_CUBIC)

    # Altimeter Instrument
    alt_base = cv2.imread("images/altimeter_base.png")
    point_1km = cv2.imread("images/1km_pointer.PNG", cv2.IMREAD_UNCHANGED)
    point_10km = cv2.imread("images/10km_pointer.PNG", cv2.IMREAD_UNCHANGED) 
    point_100m = cv2.imread("images/100m_pointer.PNG", cv2.IMREAD_UNCHANGED)

    alt_base = cv2.resize(alt_base, None, fx = 0.5, fy = 0.5, interpolation= cv2.INTER_CUBIC)
    point_10km = cv2.resize(point_10km, None, fx = 0.5, fy = 0.5, interpolation= cv2.INTER_CUBIC)
    point_1km = cv2.resize(point_1km, None, fx = 0.5, fy = 0.5, interpolation= cv2.INTER_CUBIC)
    point_100m = cv2.resize(point_100m, None, fx = 0.5, fy = 0.5, interpolation= cv2.INTER_CUBIC)

    # Airspeed instrument
    airspeed_base = cv2.imread("images/airspeed_base.png")
    airspeed_pointer = cv2.imread("images./airspeed_pointer.png",cv2.IMREAD_UNCHANGED)

    altitude = 15555
    speed = 140

    # Creates overlay for GUI
    first_column = [
        [sg.Image(filename="", key='-3DPLOT-')],
        [sg.HorizontalSeparator()],
        [sg.Image(filename="", key='-2DPLOT-')]
    ]

    second_column = [
        [sg.Image(filename="", key='-HORIZON-')],
        [sg.HorizontalSeparator()],
        [sg.Image(filename="", key='-ALTIMETER-')]
    ]

    third_column = [
        [sg.Image(filename="", key ='-AIRSPEED-')],
        [sg.HorizontalSeparator()],
        [sg.Text(font=('Helvetica', 12), justification='center', key='-FLIGHTDATA-')]
    ]

    layout = [
        [
            sg.Column(first_column),
            sg.VSeparator(),
            sg.Column(second_column),
            sg.VSeparator(),
            sg.Column(third_column)
        ]
    ]

    # Creates GUI window
    window = sg.Window("Flight Simulator 2022", layout, resizable=True)
    event, values = window.read(timeout=200)

    # Loading load screen and plane image for GPS
    load_image = cv2.imread('images/dumbshit.jpg')
    plane_image = Image.open('images/plane.png').convert("RGBA")
    background_image = Image.open('images/plot2dbackground.jpg').convert("RGBA")
    newsize = (500, 500)
    background_image = background_image.resize(newsize)
    plane_image = plane_image.resize((int(plane_image.size[0]*0.1), int(plane_image.size[1]*0.1)))

    # Converts image to bytes and update GUI window
    imgbytes = cv2.imencode(".png", load_image)[1].tobytes()
    window["-3DPLOT-"].update(data=imgbytes)
    window["-2DPLOT-"].update(data=imgbytes)
    window["-HORIZON-"].update(data=imgbytes)
    window["-ALTIMETER-"].update(data=imgbytes)
    window["-AIRSPEED-"].update(data=imgbytes)
    window["-FLIGHTDATA-"].update('LOADING\nLOADING')

    # Creates original state and control vector
    state = np.array([200, 0, 0, 200, 1000, 5000, 0, 0, 0, 0, -0.1, 0])
    control_vec = np.array([0.0,0.0,0.0,1.0])
    delta_t = 0.02

    # Creates figure for quiver plot
    fig3D = plt.figure()



    while True:
        # Reads in and updates data every 20ms
        event, values = window.read(timeout = 20)

        # In the following cases, the simulation breaks
        if event == sg.WIN_CLOSED:
            break
        if (abs(state[3]) > 5000 or abs(state[4]) > 5000):
            break
        if (state[5] > 15000 or state[5] < 1):
            break

        # Updates dynamics and control 
        state = dynamics.step(state, control_vec, delta_t)
        control_vec = control.update(control_vec)

        # Creating quiver plot
        plotter3D.vector_3D_plotter(state, fig3D)

        # Creating GPS image
        gps_image = plotter2D.GPS_plotter(state, plane_image, background_image)

        # Parameters from state
        altitude = state[5]
        pitch = state[10] * (180/math.pi)
        roll = state[9] * (180/math.pi)
        total_speed = math.sqrt(state[0] ** 2 + state[1] ** 2 + state[2] ** 2)

        # Drawing instruments
        horiz = avionics.draw_horizon(roll,-pitch, 1, horiz_base, horiz_outer, horiz_roll, horiz_pitch)
        altimeter = avionics.draw_altimeter(altitude, 1, alt_base, point_10km, point_1km, point_100m)
        speedo = avionics.draw_airspeed(total_speed, 1, airspeed_base, airspeed_pointer)

        # Converts all the OpenCV files to GUI images
        img_horizon = cv2.imencode(".png", horiz)[1].tobytes()
        img_alt = cv2.imencode(".png", altimeter)[1].tobytes()
        img_speed = cv2.imencode(".png", speedo)[1].tobytes()

        plot_3D = cv2.imread('images/vector3DPlot.jpg')
        img_3D_plotter = cv2.imencode(".png", plot_3D)[1].tobytes()
        img_2D_plotter = ImageTk.PhotoImage(image=gps_image)

        # Updates plots
        window["-HORIZON-"].update(data=img_horizon)
        window["-3DPLOT-"].update(data=img_3D_plotter)
        window["-2DPLOT-"].update(data=img_2D_plotter)
        window["-ALTIMETER-"].update(data=img_alt)
        window["-AIRSPEED-"].update(data=img_speed)

        temperature = parameterCalc.get_temperature(altitude)
        geo_potential_altitude = parameterCalc.get_geopotential_altitude(altitude)
        ambient_pressure = parameterCalc.get_pressure(altitude)
        density = parameterCalc.get_density(altitude)
        dynamic_pressure = parameterCalc.get_dynamic_pressure(altitude, total_speed)
        dynamic_viscosity = parameterCalc.get_dynamic_viscosity(altitude)
        mach_number = parameterCalc.get_mach_number(altitude, total_speed)

        window["-FLIGHTDATA-"].update("""Temperature: {:.0f}\nAirspeed: {:.0f}\nDensity: {:.1f}\n Geopotential Altitude: {:.1f}\nAmbient Pressure: {:.0f}
         Dynamic Pressure: {:.1f}\n Dynamic Viscosity: {:.1f}\n Mach Number: {:.1f}\n X: {:.1f}\nY: {:.1f}\nZ: {:.1f}\nU: {:.1f}\nV: {:.1f}
         W: {:.1f}\nRoll: {:.1f}\nPitch: {:.1f}\nYaw: {:.1f}\nRollDot: {:.1f}\nPitchDot: {:.1f}\nYawDot: {:.1f}\nElevator: {:.1f}
         Aileron: {:.1f}\n Rudder: {:.1f}\n Thrust: {:.1f}""".format(temperature, total_speed,geo_potential_altitude, ambient_pressure, density, 
                                                                     dynamic_pressure, dynamic_viscosity, mach_number, state[3], state[4], state[5], 
                                                                     state[0], state[1], state[2], state[9], state[10], state[11], state[6], state[7], 
                                                                     state[8], control_vec[0], control_vec[1], control_vec[2], control_vec[3]))




    window.close()
