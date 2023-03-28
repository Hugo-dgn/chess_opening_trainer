import tkinter as tk

import chess

from . import image as _image
from . import location as _loc
from . import control as _control

from .control import get_color_to_move
from .control import change_color_to_move
from .control import get_hold_piece_case
from .draw import draw_arrow, delete_arrows

set_input_handler = _control.set_input_handler
set_mode = _control.set_mode

class Board:

    def __init__(self, root, case_size):
        """
        input:
            -root : tk widget
            -case_size : int
        """
        self.case_size = case_size

        self.board = chess.Board()
        self.canvas = _image.draw_board(root, case_size)
        self.is_fliped = False

        self._current_image = []

        self.canvas.bind("<Button-1>", 
            lambda event : _control.click(self.case_size, self.board,
                                            self.is_fliped, self.draw,
                                            self.canvas, event))
        self.canvas.bind("<B1-Motion>", 
            lambda event : _control.motion(self.case_size, self.canvas, event))
        
        self.canvas.bind("<ButtonRelease>", 
            lambda event : _control.release(self.case_size, self.draw,
                                            self.is_fliped, self,
                                            event))
    
    def draw(self, without=None):
        """
        input:
            -without : int list
        output:
            -None
        Draw the pieces on the board. If some pieces
        don't need to be draw, give their case_number in
        without
        """
        if without is None:
            without=[]
        self._current_image = []
        position_list = self.board.epd().split()[0].split("/")
        position_list.reverse()
        position = "".join(position_list)

        n_case = 0
        for epd_info in position:
            try:
                n = int(epd_info)
            except ValueError:
                if not (n_case in without):
                    image = _image.get_piece_image(epd_info, self.case_size)
                    self._current_image.append(image)
                    self.canvas.create_image(_loc.get_case_pos(n_case, self.case_size, self.is_fliped),
                                                image=self._current_image[-1])
                n = 1
            n_case += n
    
    def reset(self):
        self.board = chess.Board()
        self._current_image = []
        self.draw()