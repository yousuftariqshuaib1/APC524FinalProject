
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk


_VARS = {'window': False,
         'fig_agg3D': False,
         'fig_agg2D': False,
         'pltFig3D': False,
         'pltFig2D': False}


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

first_column = [
    [sg.Canvas(key='3DPlot')],
    [sg.HorizontalSeparator()],
    [sg.Image(key='-IMAGE3-')]
]

second_column = [
    [sg.Image(key='-IMAGE2-')],
    [sg.HorizontalSeparator()],
    [sg.Image(key='-IMAGE4-')]
]

layout = [
    [
        sg.Column(first_column),
        sg.VSeparator(),
        sg.Column(second_column),
    ]
]

_VARS['window'] = sg.Window('Such Window',
                            layout,
                            finalize=True,
                            resizable=True,
                            location=(100, 100),
                            element_justification="right")

def drawChart():
    _VARS['pltFig'] = plt.figure()
    plt.scatter(np.random.rand(1,10),np.random.rand(1,10))
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['3DPlot'].TKCanvas, _VARS['pltFig'])

def updateChart():
    _VARS['fig_agg'].get_tk_widget().forget()
    # plt.cla()
    plt.clf()
    plt.scatter(np.random.rand(1,10),np.random.rand(1,10))
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['3DPlot'].TKCanvas, _VARS['pltFig'])
    _VARS['pltFig'].canvas.flush_events()

drawChart()

im = Image.open('dumbshit.jpg')
image = ImageTk.PhotoImage(image=im)


_VARS['window']['-IMAGE2-'].update(data=image)
_VARS['window']['-IMAGE3-'].update(data=image)
_VARS['window']['-IMAGE4-'].update(data=image)


# MAIN LOOP
while True:
    event, values = _VARS['window'].read(timeout=200)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    updateChart()

plt.close()
_VARS['window'].close()
