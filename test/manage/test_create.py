import tkinter as tk
import os

from manage.create import update_ligne_handler
import opening
import board.control as control
import board


def test_update_ligne_handler():
    chess_board = board.Board(tk.Tk(), 10)
    op = opening.Opening("test", True)

    control._current_piece_case = 9


    update_ligne_handler(17, chess_board, op)

    os.remove("data/test.op")

    assert len(op.tree.childrens) == 1