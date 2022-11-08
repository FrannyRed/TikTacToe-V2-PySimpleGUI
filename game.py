import PySimpleGUI as sg

def TikTacToe():
    sg.theme('Dark')
    MAX_ROWS = MAX_COL = 3
    player = 0

    layout = [[sg.Text('TIK TAC TOE')],
              [sg.Text('Player 1 is "O"; Player 2 is "X"')]
    ]

    # Build the 'board', a grid of buttons
    board = []
    for row in range(MAX_ROWS):
        layout_row = []
        for col in range(MAX_COL):
            layout_row.append(sg.Button(str(''), size=(4, 2), pad=(0, 0), border_width=1, key=(player)))
        board.append(layout_row)

    # Add the board to the layout
    layout += board

    # Add the rest button as the last row
    layout += [[sg.Text('Press if you would like to reset the game:')],
               [sg.Button('Reset Game', button_color=('white', 'red'), key='-RESET-')],
               [sg.Button('Exit', button_color=('white', 'red'))]
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
        if '-PLAYER-' in event:
            window[event].update('O', button_color=('white', 'blue'))

    window.close()

while True:
    reset = TikTacToe()
    if reset == '-RESET-':
        continue
    else:
        break