import tkinter as tk

import chess

from . import image as _image
from . import location as _loc

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

        self._current_image = []
    
    def draw(self):
        self._current_image = []
        n_case = 63 #begin with black rock
        position = "".join(self.board.epd().split()[0].split("/"))
        print(position)
        for epd_info in position:
            try:
                n = int(epd_info)
                n_case -= n
            except ValueError:
                image = _image.get_piece_image(epd_info, self.case_size)
                self._current_image.append(image)
                self.canvas.create_image(_loc.get_case_pos(n_case, self.case_size),
                                            image=self._current_image[-1])
                n_case -= 1
