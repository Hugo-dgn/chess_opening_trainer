import chess

from .location import get_case_number
from .image import get_piece_image

_user_to_move = False

_color_to_move = chess.WHITE

def set_mode(user_to_move):
    global _user_to_move
    _user_to_move = user_to_move

_current_piece = None
_current_piece_case = None
_current_image = None
_current_image_id = None

def reset():
    global _user_to_move, _color_to_move, _current_piece
    global _current_piece_case, _current_image, _current_image_id
    _user_to_move = False
    _color_to_move = chess.WHITE
    _current_piece = None
    _current_piece_case = None
    _current_image = None
    _current_image_id = None


def click(case_size, board, isfliped, draw_function, canvas, event):
    """
    input:
        -case_size : int
        -board : chess.Board
        -darw_function : board.Board method
        -canvas : tk.Canvas
        -event : tk.event
    output:
        None
    Called function when the user click on the board. This
    function check if a piece is clicked on, if one is
    it sets up the variable for the animation (piece follow
    the mouse)
    """
    if _user_to_move:
        global _current_piece
        global _current_piece_case
        global _current_image
        global _current_image_id
        _current_piece_case = get_case_number(event.x, event.y, case_size, isfliped)
        _current_piece = board.piece_at(_current_piece_case)
        if not (_current_piece is None):
            if _current_piece.color is _color_to_move:
                _current_piece = _current_piece.symbol()
                draw_function(without=[_current_piece_case])
                _current_image = get_piece_image(_current_piece, case_size)
                _current_image_id = canvas.create_image((event.x, event.y),
                                    image = _current_image)
            else:
                _current_piece = None
                _current_piece_case = None
                _current_image = None
                _current_image_id = None

def release(case_size, draw_function, isfliped, board, event):
    """
    input:
        -case_size : int
        -darw_function : board.Board method
        -event : tk.event
    output:
        None
    When the user release the piece, call the given function
    to inform the program of the target square and then draw
    the board with the new info
    """
    global _current_piece
    if _user_to_move and not (_current_piece is None):
        global _current_piece_case
        global _current_image
        global _current_image_id

        target_square = get_case_number(event.x, event.y, case_size, isfliped)
        _input_handler(target_square, board)

        _current_piece = None
        _current_piece_case = None
        _current_image = None
        _current_image_id = None
        draw_function()

def motion(case_size, canvas, event):
    if _user_to_move and not (_current_piece is None):
        global _current_image
        if not (_current_piece is None):
            canvas.moveto(_current_image_id, event.x-case_size//2, event.y-case_size//2)

def _default_input_handler(target_square, board):
    """
    input:
        -target_square : int
        -board : Board.board
    output:
        -None
    Default game mode : user play both black and white with
    queen autopromote on
    """
    def _get_promotion_type():
        return chess.QUEEN
    move = chess.Move(get_hold_piece_case(), target_square)
    promotion_move = chess.Move(get_hold_piece_case(), target_square, promotion=chess.QUEEN)
    if board.board.is_legal(move):
        board.board.push(move)
        change_color_to_move()
    if board.board.is_legal(promotion_move):
        promotion_piece_type = _get_promotion_type()
        promotion_move = chess.Move(get_hold_piece_case(), target_square, promotion=promotion_piece_type)
        board.board.push(promotion_move)
        change_color_to_move()

def set_input_handler(function):
    """
    input:
        -function : function 
    output:
        -None
    set the input_handler function which define how the pieces
    are moved given the input
    """
    global _input_handler
    _input_handler = function


set_input_handler(_default_input_handler)

def get_color_to_move():
    return _color_to_move

def get_hold_piece_case():
    return _current_piece_case

def change_color_to_move():
    global _color_to_move
    _color_to_move = not _color_to_move