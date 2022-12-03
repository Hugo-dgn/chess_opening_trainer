import chess

import opening.manage_ligne as _manage_ligne
import opening.tree as _tree

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
        self.tree = _tree.Node(None, None, [])
    
    def add(self, ligne):
        """
        input:
            -self : Opening class
            -ligne : chess.Move list
        output:
            -None
        add a ligne to the opening. Must be called each time
        a new move is make by the user
        """
        node = _manage_ligne.add_ligne(self.tree, ligne)
        _manage_ligne.clean_ligne(node)