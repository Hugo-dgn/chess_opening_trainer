import os

import chess

import opening
import board

def get_op(color):
    selected_op = [opening.load(name[:-3]) for name in os.listdir("data") if opening.load(name[:-3]).color == color]
    return selected_op

def get_all_op():
    selected_op = [opening.load(name[:-3]) for name in os.listdir("data")]
    return selected_op

class Explorer(opening.Opening):

    def __init__(self, op):
        opening.Opening.__init__(self, op.name, op.color)
        self.tree = op.tree
        self.current = op.tree
        self.choice_function = lambda l : l[0]
    
    def next(self):
        next_node = self.choice_function(self.current.childrens)
        self.current = next_node
        return next_node.move
    
    def select(self, next_node):
        self.current = next_node
    
    def set_choice_function(self, func):
        self.choice_function = func

def draw_arrow(chess_board, explorer):
    pass

def explore_ligne_handler(target_square, chess_board, op, explorer):
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

def explore_mode(op, _chess_board):
    explorer = Explorer(op)
    board.set_mode(op.color)
    if not op.color:
        move = explorer.next()
        _chess_board.board.push(move)
        board.change_color_to_move()
    draw_arrow()
    board.set_input_handler(
        lambda target_square, chess_board : explore_ligne_handler(target_square, chess_board, op, explorer)
        )