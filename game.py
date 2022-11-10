import PySimpleGUI as sg

def TikTacToe():
    sg.theme('Dark')
    MAX_ROWS = MAX_COL = 3
    player1 = []

    layout = [[sg.Text('TIK TAC TOE')],
              [sg.Text('Player 1 is "O"; Player 2 is "X"')]
    ]

    # Build the 'board', a grid of buttons
    board = []
    for row in range(MAX_ROWS):
        layout_row = []
        for col in range(MAX_COL):
            layout_row.append(sg.Button(str(''), size=(4, 2), pad=(0, 0), border_width=1, key=(row,col)))
        board.append(layout_row)

    # Add the board to the layout
    layout += board

    # Add the rest button as the last row
    layout += [[sg.Text(key='-MESSAGE-')],
               [sg.Text(key='-WIN-')],
               [sg.Button('Reset Game', button_color=('white', 'red'), key='-RESET-'),
                sg.Button('Exit', button_color=('white', 'red'))]
    ]

    window = sg.Window('TIC TAC TOE', layout)

    # The event loop
    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == '-RESET-':
            window.close()
            return event
        else:
            window[event].update('O', button_color=('white', 'blue'))
            window[event].update(disabled=True)
            player1.append(event)
            window['-MESSAGE-'].update(player1)
            winwin = win(player1)
            if winwin == True:
                window['-WIN-'].update('Player wins!')
                for y in range(MAX_ROWS):
                    for z in range(MAX_COL):
                        window[(y,z)].update(disabled=True)
            # elif x + 1 == 2:
            #    window[event].update('X', button_color=('white', 'purple'))
            #    window[event].update(disabled=True)

    window.close()

def win(moves = []):
    if moves == [(0, 0), (0, 1), (0, 2)]:
        return True
    elif moves == [(0, 0), (1, 0), (2, 0)]:
        return True
    elif moves == [(1, 1), (1, 2), (1, 3)]:
        return True
    else:
        return False

while True:
    reset = TikTacToe()
    if reset == '-RESET-':
        continue
    else:
        break