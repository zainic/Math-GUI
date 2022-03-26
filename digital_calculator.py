import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from zmath import *

""" Digital Calculator Layout """
digital_calculator = [
    [sg.Text("Type the calculation below")],
    [sg.InputText(size=(40,1), key="-CALCULATOR-")],
    [sg.Text(size=(20,1), key="-RESULT-")],
]

digital_calculator_layout = [
    [sg.Column(digital_calculator)],
    [sg.Button('Exit', size=(10, 1), pad=((280, 0), 3), font='Helvetica 14')]
]

""" Run digital calculator window """
def run():
    window = sg.Window("Zainic Math", digital_calculator_layout)
    while True:
        event, values = window.read(timeout=2)
        if event in ('Exit', None, sg.WIN_CLOSED):
            exit(69)
        if values["-CALCULATOR-"] != "":
            try:
                window["-RESULT-"].update(str(eval(values["-CALCULATOR-"])))
            except:
                window["-RESULT-"].update("Invalid Calculation")
                