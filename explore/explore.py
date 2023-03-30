import chess
import board
from explore.explorer import Explorer
import explore.action as action
import explore.display as display

def event_manager(event, _chess_board, explorer):
    if event.keycode == 37:
        action.back(event, _chess_board, explorer)

def explore_handler(target_square, chess_board, op, explorer):
    def _get_promotion_type():
        return chess.QUEEN
    move = chess.Move(board.get_hold_piece_case(), target_square)
    promotion_move = chess.Move(board.get_hold_piece_case(), target_square, promotion=chess.QUEEN)

    flag = False
    for next_node in explorer.current.childrens:
        if move == next_node.move:
            explorer.select(next_node)
            chess_board.board.push(move)
            board.change_color_to_move()
            display.draw_arrow(chess_board, explorer)
        elif promotion_move == next_node.move:
            explorer.select(next_node)
            promotion_piece_type = _get_promotion_type()
            promotion_move = chess.Move(board.get_hold_piece_case(), target_square, promotion=promotion_piece_type)
            chess_board.board.push(promotion_move)
            board.change_color_to_move()
            display.draw_arrow(chess_board, explorer)

def explore_mode(op, _chess_board, root):
    explorer = Explorer(op)
    root.bind("<Key>", lambda event : event_manager(event, _chess_board, explorer))
    board.set_mode(True)
    display.draw_arrow(_chess_board, explorer)
    board.set_input_handler(
        lambda target_square, chess_board : explore_handler(target_square, chess_board, op, explorer)
        )