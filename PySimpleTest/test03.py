# This is my modification of a pySimpleGUI example
# MDT
# 2021.07.10

import PySimpleGUI as sg

# Clever tricks to make a grid of buttons for the layout:
layout = [[sg.Button(f'{row}, {col}') for col in range(4)] for row in range(4)]

# In the original, this is a one-shot, but here I have added an
# event loop:

window = sg.Window('Grid of Buttons', layout, alpha_channel = 0.9)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:    # If user closes window, exit loop
        break
    print('You entered ', event)  # Event contains the name of the buttons (not sure why)

window.close()
