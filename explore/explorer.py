import os

import opening

def get_op(color):
    selected_op = [opening.load(name[:-3]) for name in os.listdir("data") if opening.load(name[:-3]).color == color]
    return selected_op

def get_all_op():
    selected_op = [opening.load(name[:-3]) for name in os.listdir("data")]
    return selected_op

class Explorer():

    def __init__(self, op):
        self.op = op
        self.tree = op.tree
        self.current = op.tree
        self.choice_function = lambda l : l[-1]
        self.pile = [op.tree]
    
    def next(self):
        if len(self.current.childrens) > 0:
            next_node = self.choice_function(self.current.childrens)
            self.current = next_node
            self.pile.append(next_node)
            return next_node.move
    
    def select(self, next_node):
        self.pile.append(next_node)
        self.current = next_node
    
    def pop(self):
        if len(self.pile) > 1:
            undo_move = self.pile.pop()
            self.current = self.pile[-1]
            return undo_move
    
    def set_choice_function(self, func):
        self.choice_function = func
    
    def reset(self):
        self.current = self.tree
        self.pile = [self.tree]