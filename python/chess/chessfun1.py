# Set up board

xlabels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def colour_check(box):
    x = box[0]
    y = int(box[1])

    if xlabels.index(x) % 2 == 0:
        if y % 2 == 0:
            return 'Light'

        else:
            return 'Dark'

    else:
        if y % 2 == 0:
            return 'Dark'

        else:
            return 'Light'

def chess_board_cell_color(cell1, cell2):

    return colour_check(cell1) == colour_check(cell2)

