def chess_board_cell_color(cell1, cell2):
    return sum((ord(cell1[0]), int(cell1[1]), ord(cell2[0]), int(cell2[1]))) % 2 == 0


print("Same colour")
print(chess_board_cell_color("A1", "C3"))
print(chess_board_cell_color("D3", "E6"))
print(chess_board_cell_color("B6", "F2"))
print(chess_board_cell_color("H2", "C1"))

print("Different colour")
print(chess_board_cell_color("A1", "H3"))
print(chess_board_cell_color("B3", "H6"))
print(chess_board_cell_color("C8", "B2"))
print(chess_board_cell_color("A1", "B1"))
