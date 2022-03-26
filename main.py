import PySimpleGUI as sg
import os.path
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import digital_calculator 
import eigenstuff
from zmath import *

"""Selection Section"""
selection_section = [
    [
        sg.Text("Select type of calculation"),
    ],
    [
        sg.Combo([
            "Digital Calculator",
            "Matrix",
            "Eigenstuff",
            "Combinatorics",
            "Summation",
            "Graph"
            ],
            key="-TYPE-"),
    ],
    [
        sg.Button("-GO-", key="-GO-")
    ]
]

""" Main Layout """
main_layout = [
    [sg.Column(selection_section)],
    [sg.Button('Exit', size=(10, 1), pad=((280, 0), 3), font='Helvetica 14')]
]

window = sg.Window("Zainic Math", main_layout)
while True:
    event, values = window.read()
    if event in ('Exit', None, sg.WIN_CLOSED):
        exit(69)
    if event == "-GO-":
        selector = values["-TYPE-"]
        break

window.close()

if selector == "Digital Calculator":
    digital_calculator.run()
elif selector == "Eigenstuff":
    eigenstuff.run()

window.close()