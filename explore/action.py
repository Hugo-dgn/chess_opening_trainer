import board
from explore import display
import manage


def back(event, chess_board, explorer):
    if explorer.pop() is not None:
        chess_board.board.pop()
        chess_board.draw()
        display.draw_arrow(chess_board, explorer)
        board.change_color_to_move()

def delete(event, chess_board, explorer):
    if event.keycode == 46:
        if explorer.pop() is not None:
            explorer.op.delete_last_move(chess_board.board.move_stack)
            chess_board.board.pop()
            chess_board.draw()
            display.draw_arrow(chess_board, explorer)
            board.change_color_to_move()