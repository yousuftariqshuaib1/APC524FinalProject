import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import numpy as np

def game_over_screen():
    first_column = [
        [sg.Image(filename="", key='-GAMEOVER-')],
        [sg.Button('Exit')]
    ]
    layout = [
        [
            sg.Column(first_column),
        ]
    ]

    im = Image.open('../images/gameover.jpg')
    window = sg.Window('Intro Screen', layout, finalize=True, resizable=True, element_justification='c')
    image = ImageTk.PhotoImage(image=im)
    window['-GAMEOVER-'].update(data=image)
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    
    window.close()

    