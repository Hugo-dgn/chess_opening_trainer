from board.location import get_case_pos, get_case_number

arrows = []

def draw_arrow(from_square, to_square, chess_board):
    pos_start = get_case_pos(from_square, chess_board.case_size, chess_board.is_fliped)
    pos_end = get_case_pos(to_square, chess_board.case_size, chess_board.is_fliped)
    arrow = chess_board.canvas.create_line(pos_start[0], pos_start[1], pos_end[0], pos_end[1])
    arrows.append(arrow)
    chess_board.draw()

def delete_arrows(chess_board):
    global arrows
    for arrow in arrows:
        chess_board.canvas.delete(arrow)
    arrows = []