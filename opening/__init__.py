import chess
from .tree import get_root as _get_root
from .tree import Node as _Node

class Opening:
    """
    attribut:
        -name : str
        -color : chess.color
        -tree : Node class
    methode:
        -add
    
    The root of an opening tree is always None
    Only one responce is allowed for the color which is
    training
    """

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.tree = _Node(None, None, [])
    
    def add(self, ligne):
        """
        input:
            -self : Opening class
            -ligne : chess.Move list
        output:
            -None
        add a ligne to the opening. 
        """
        current_node = self.tree