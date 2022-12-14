import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import numpy as np

# Creates an intro screen using saved image
def intro_screen():
    first_column = [
        [sg.Image(filename="", key='-INTRO-')]
    ]
    second_column = [
        [sg.Text(font=('Helvetica', 12), justification='center', key='-CONTROL-')],
        [sg.Button("Closed-Loop Control Scheme")],
        [sg.Button("Decaying Open-Loop Control Scheme")]
    ]
    layout = [
        [
            sg.Column(first_column),
            sg.VSeperator(),
            sg.Column(second_column)
        ]
    ]

    im = Image.open('../images/intro_screen.png')
    window = sg.Window('Intro Screen', layout, finalize=True, resizable=True, element_justification='c')
    image = ImageTk.PhotoImage(image=im)
    window['-INTRO-'].update(data=image)
    window['-CONTROL-'].update("""Use a proper proprtional closed-loop 
    control scheme that doesn't have a sticky thrust
    or use an open-loop decaying control scheme
    that does have a sticky thrust""")
    
    value = None
    while True:
        event, values = window.read()
        if event == "Closed-Loop Control Scheme":
            value = 0
            break
        if event == sg.WIN_CLOSED:
            break
        if event == "Decaying Open-Loop Control Scheme":
            value = 1
            break
    
    window.close()
    
    return value