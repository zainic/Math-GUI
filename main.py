import PySimpleGUI as sg
import os.path
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import matplotlib.pyplot as plt
from zmath import *

"""Graph Stuff"""
matplotlib.use("TkAgg")
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

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

""" Eigenstuff Layout """
matrix_input = [
    [sg.Text("Write your matrix below")],
    [sg.InputText(size=(40,1), key="-MATRIX-")],
    [sg.Text(size=(40,1), key="-ERROREIGEN-")],
]

eigenstuff = [
    [sg.Text(size=(50,1), key="-EIGENVALS-")],
    [sg.Text(size=(50,20), key="-EIGENVECS-")]
]

eigenstuff_layout = [
    [sg.Column(matrix_input), sg.VSeperator(), sg.Column(eigenstuff)],
    [sg.Button('Exit', size=(10, 1), pad=((280, 0), 3), font='Helvetica 14'),]
]

window.close()

if selector == "Digital Calculator":
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
                break
            
elif selector == "Eigenstuff":
    window = sg.Window("Zainic Math", eigenstuff_layout)
    while True:
        event, values = window.read(timeout=10)
        if event in ('Exit', None, sg.WIN_CLOSED):
            exit(69)
        if values["-MATRIX-"] != "":
            try:
                eigenvals, eigenvecs = np.linalg.eig(eval(values["-MATRIX-"]))
                str_eigenvals = "[" + " ".join([str(np.round(l,3)) for l in eigenvals]) + "]"
                str_eigenvecs = "\n".join([str(np.round(l,3)) for l in eigenvecs])
                window["-EIGENVALS-"].update("Eigenvalues : " + str_eigenvals)
                window["-EIGENVECS-"].update("Eigenvectors : \n" + str_eigenvecs)
                window["-ERROREIGEN-"].update("Success")
            except:
                window["-EIGENVALS-"].update("")
                window["-EIGENVECS-"].update("")
                window["-ERROREIGEN-"].update("Invalid Matrix Input")

window.close()