import chess

import board
import opening

from explore.explorer import Explorer
import explore.action as action
import explore.display as display

def event_manager(event, _chess_board, explorer):
    if event.keycode == 37:
        action.back(event, _chess_board, explorer)
    elif event.keycode == 46:
        action.delete(event, _chess_board, explorer)
    elif event.keycode == 83:
        opening.save(explorer.op)

def edit_handler(target_square, chess_board, op, explorer):
    def _get_promotion_type():
        return chess.QUEEN
    move = chess.Move(board.get_hold_piece_case(), target_square)
    promotion_move = chess.Move(board.get_hold_piece_case(), target_square, promotion=chess.QUEEN)

    flag = True
    for next_node in explorer.current.childrens:
        if move == next_node.move:
            explorer.select(next_node)
            chess_board.board.push(move)
            board.change_color_to_move()
            flag = False
        elif promotion_move == next_node.move:
            explorer.select(next_node)
            promotion_piece_type = _get_promotion_type()
            promotion_move = chess.Move(board.get_hold_piece_case(), target_square, promotion=promotion_piece_type)
            chess_board.board.push(promotion_move)
            board.change_color_to_move()
            flag = False
    if flag:
        ligne = chess_board.board.move_stack
        if chess_board.board.is_legal(move):
            chess_board.board.push(move)
            board.change_color_to_move()
            op.add(ligne)
            for next_node in explorer.current.childrens:
                if next_node.move == ligne[-1]:
                    explorer.select(next_node)
        if chess_board.board.is_legal(promotion_move):
            promotion_piece_type = _get_promotion_type()
            promotion_move = chess.Move(board.get_hold_piece_case(), target_square, promotion=promotion_piece_type)
            chess_board.board.push(promotion_move)
            board.change_color_to_move()
            ligne = chess_board.board.move_stack
            op.add(ligne)
            for next_node in explorer.current.childrens:
                if next_node.move == ligne[-1]:
                    explorer.select(next_node)
    display.draw_arrow(chess_board, explorer)

def edit_mode(op, _chess_board, root):
    explorer = Explorer(op)
    root.bind("<Key>", lambda event : event_manager(event, _chess_board, explorer))
    board.set_mode(True)
    display.draw_arrow(_chess_board, explorer)
    board.set_input_handler(
        lambda target_square, chess_board : edit_handler(target_square, chess_board, op, explorer)
        )