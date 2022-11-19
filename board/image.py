import tkinter as tk
import yaml
from PIL import Image, ImageTk

def draw_board(root, case_size):
    """
    input:
        -root : tk widget
        -case_size : int
    output:
        -tk.Canvas
    Draw board's squares on a canvas
    """
    canvas = tk.Canvas(root, width=case_size*8,
                        height=case_size*8)
    for i in range(8):
        for j in range(8):
            if (i+j) % 2:
                color = "#A04000"
            else:
                color = "#B3B6B7"
            canvas.create_rectangle(i*case_size, j*case_size,
                                (i+1)*case_size, (j+1)*case_size,
                                fill=color, outline="")
    return canvas

### load assets ###

def get_rect_pieces(path):
    """
    input:
        -path : str
    output:
        -yaml : dic
    load pieces positions on the image
    """
    with open(path, 'r') as file:
        return yaml.load(file, Loader=yaml.FullLoader)

def get_image_pieces(path):
    """
    input:
        -path : str
    output:
        -image : PIL.Image
    load pieces image
    """
    return Image.open(path).convert("RGBA")

_path = "assets/"

_pieces_rect = get_rect_pieces(_path+"pieces_rec.yaml")
_pieces_image = get_image_pieces(_path+"Chess_Pieces.png")

### load assets ###

def get_piece_image(piece, case_size):
    """
    input:
        -piece : str
        -case_size : int
    output:
        -piece_tk_image : PIL.ImageTk
    Gets the image of a pieces in ImageTk format given its
    symbol (piece = "Q" -> white queen)
    """
    piece_image =  _pieces_image.crop(_pieces_rect[piece])
    piece_image = piece_image.resize((case_size, case_size))
    piece_tk_image = ImageTk.PhotoImage(piece_image)
    return piece_tk_image
