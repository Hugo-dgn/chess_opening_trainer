import random

import chess
import board
from explore.explorer import Explorer

def manage_end(chess_board, explorer):
    if len(explorer.current.childrens) == 0:
        set_up(explorer, chess_board)

def train_handler(target_square, chess_board, op, explorer):
    def _get_promotion_type():
        return chess.QUEEN
    move = chess.Move(board.get_hold_piece_case(), target_square)
    promotion_move = chess.Move(board.get_hold_piece_case(), target_square, promotion=chess.QUEEN)

    flag = False
    for next_node in explorer.current.childrens:
        if move == next_node.move:
            board.set_mode(False)
            explorer.select(next_node)
            chess_board.board.push(move)
            board.change_color_to_move()
            flag =True
        elif promotion_move == next_node.move:
            board.set_mode(False)
            explorer.select(next_node)
            promotion_piece_type = _get_promotion_type()
            promotion_move = chess.Move(board.get_hold_piece_case(), target_square, promotion=promotion_piece_type)
            chess_board.board.push(promotion_move)
            board.change_color_to_move()
            flag = True
        if flag:
            move = explorer.next()
            if move is not None:
                chess_board.board.push(move)
                board.change_color_to_move()
                board.set_mode(True)
    manage_end(chess_board, explorer)

def chose_next_move(node_list):
    i = random.randint(0, len(node_list)-1)
    return node_list[i]

def set_up(explorer, chess_board):
    explorer.reset()
    chess_board.reset()
    board.set_mode(explorer.color)
    if not explorer.color:
        move = explorer.next()
        chess_board.board.push(move)
        chess_board.draw()
        board.change_color_to_move()
        board.set_mode(True)
    chess_board.draw()

def train_mode(op, _chess_board):
    explorer = Explorer(op)
    explorer.set_choice_function(chose_next_move)
    set_up(explorer, _chess_board)
    board.set_input_handler(
        lambda target_square, chess_board : train_handler(target_square, chess_board, op, explorer)
        )