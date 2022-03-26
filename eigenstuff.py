import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from zmath import *

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

"""Run digital calculator window"""
def run():
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