import os as _os

import pickle as _pickle

import opening.manage_ligne as _manage_ligne
import opening.tree as _tree

def save(op):
    """
    input:
        -op : str
    output:
        -None
    Save an opening
    """
    with open(f"data/{op.name}.op", "wb") as file:
        _pickle.dump(op, file)

def load(op_name):
    """
    input:
        -op_name : str
    output:
        op : Opening
    """
    with open(f"data/{op_name}.op", "rb") as file:
        op = _pickle.load(file)
    return op

def oplist():
    """
    input:
        -None
    output:
        -op_files : str list
    Gives the list of the openings names
    """
    files =  _os.listdir("data/")
    def is_op(file):
        if len(file) < 3:
            return False
        else:
            return file[-3:len(file)] == ".op"
    op_files = [file for file in files if is_op(file)]
    return op_files

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
        if node is not None:
            _manage_ligne.clean_ligne(node)
    
    def delete(self, ligne):
        """
        input:
            -self : Opening class
            -ligne : chess.Move list
        output:
            -None
        deleat ligne from opening tree
        """
        _manage_ligne.deleat_ligne(self.tree, ligne)
    
    def delete_last_move(self, ligne):
        """
        input:
            -self : Opening class
            -ligne : chess.Move list
        output:
            -None
        deleat last move from opening tree
        """
        _manage_ligne.delete_last_move(self.tree, ligne)