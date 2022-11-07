import PySimpleGUI as sg

layout = [[sg.Text('This is a thing')]]

window = sg.Window('Thingy', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()