import introScreen
import main_gui
import gameover
import PySimpleGUI
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import cv2
import numpy
import keyboard
from typing import Protocol
from PIL import Image, ImageTk
from pydub import AudioSegment
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm 
from mpl_toolkits.mplot3d import axes3d
from matplotlib.colors import Normalize

value = introScreen.intro_screen()
if (value is not None):
    main_gui.main_GUI(value)
    gameover.game_over_screen()