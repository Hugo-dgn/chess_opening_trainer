import chess
from .tree import get_root as _get_root

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
        self.tree = Node(None, None, [])
    
    def add(self, ligne):
        """
        input:
            -self : Opening class
            -ligne : chess.Move list
        output:
            -None
        add a ligne to the opening"""
        pass
        

class Node:

    def __init__(self, move, parents, childrens):
        self.move = move
        self.parents = parents
        self.childrens = childrens
    
    def add(self, move):
        """
        input:
            -self : opening.Node
            -move : chess.Move
        output:
            -None
        Add a children to the node and check if the position
        is already reach in another branch, if it is it links
        the children of the nodes together
        """
        next_node = Node(move, [self], [])
        self.childrens.append(next_node)
    
    def __repr__(self):
        if self.move is None:
            uci = None
        else:
            uci = self.move.uci()
        return f"{uci} : {self.childrens}"
