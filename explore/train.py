import os

import chess

import opening
import board
from explore.explorer import Explorer

def draw_arrow(chess_board, explorer):
    pass

def train_handler(target_square, chess_board, op, explorer):
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
            flag =True
        elif promotion_move == next_node.move:
            explorer.select(next_node)
            promotion_piece_type = _get_promotion_type()
            promotion_move = chess.Move(board.get_hold_piece_case(), target_square, promotion=promotion_piece_type)
            chess_board.board.push(promotion_move)
            board.change_color_to_move()
            flag = True
        if flag:
            move = explorer.next()
            chess_board.board.push(move)
            board.change_color_to_move()

def train_mode(op, _chess_board):
    explorer = Explorer(op)
    board.set_mode(op.color)
    if not op.color:
        move = explorer.next()
        _chess_board.board.push(move)
        board.change_color_to_move()
    draw_arrow(_chess_board, explorer)
    board.set_input_handler(
        lambda target_square, chess_board : train_handler(target_square, chess_board, op, explorer)
        )