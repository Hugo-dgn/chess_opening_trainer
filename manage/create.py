import chess

import board
import opening

def update_ligne_handler(target_square, chess_board, op):
    def _get_promotion_type():
        return chess.QUEEN
    move = chess.Move(board.get_hold_piece_case(), target_square)
    promotion_move = chess.Move(board.get_hold_piece_case(), target_square, promotion=chess.QUEEN)
    if chess_board.board.is_legal(move):
        chess_board.board.push(move)
        board.change_color_to_move()
    if chess_board.board.is_legal(promotion_move):
        promotion_piece_type = _get_promotion_type()
        promotion_move = chess.Move(board.get_hold_piece_case(), target_square, promotion=promotion_piece_type)
        chess_board.board.push(promotion_move)
        board.change_color_to_move()
    
    ligne = chess_board.board.move_stack
    op.add(ligne)

def insert_mode(op):
    board.set_mode(True)
    board.set_input_handler(
        lambda target_square, chess_board : update_ligne_handler(target_square, chess_board, op)
        )