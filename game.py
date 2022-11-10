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

    window.close()

# this function will review players moves to see if they won
def win(moves = []):
    wins = {0 : [(0, 0), (0, 1), (0, 2)], # horizontal top row
            1 : [(1, 0), (1, 1), (1, 2)], # horizontal middle row
            2 : [(1, 0), (1, 1), (1, 2)], # horizontal middle row
            3 : [(2, 0), (2, 1), (2, 2)], # horizontal bottom row
            4 : [(0, 0), (1, 0), (2, 0)], # vertical first column
            5 : [(0, 1), (1, 1), (2, 1)], # vertical second column
            6 : [(0, 2), (1, 2), (2, 2)], # vertical third column
            7 : [(0, 0), (1, 1), (2, 2)], # diagonal top left to bottom right
            8 : [(0, 2), (1, 1), (2, 0)]  # diagonal top right to bottom left
            }                             # end dictionary

    # this section iterates through dictionary of winning moves
    # and compares them with the players moves to detect a win
    for dict in range(9):   # increment through each dictionary list
        counter = 0
        for i in range(len(moves)): # increment through players moves
            for dict_moves in range(3): # increment through winning moves
                # if player moves are in winning moves, increment counter
                if moves[i] == wins[dict][dict_moves]:
                    counter += 1
        # if the counter is 3 then player won
        if counter == 3:
            return True
    else:
        return False

while True:
    reset = TikTacToe()
    if reset == '-RESET-':
        continue
    else:
        break