import os

import opening

def get_op(color):
    selected_op = [opening.load(name[:-3]) for name in os.listdir("data") if opening.load(name[:-3]).color == color]
    return selected_op

def get_all_op():
    selected_op = [opening.load(name[:-3]) for name in os.listdir("data")]
    return selected_op

class Explorer(opening.Opening):

    def __init__(self, op):
        opening.Opening.__init__(self, op.name, op.color)
        self.tree = op.tree
        self.current = op.tree
        self.choice_function = lambda l : l[0]
    
    def next(self):
        next_node = self.choice_function(self.current.childrens)
        self.current = next_node
        return next_node.move
    
    def select(self, next_node):
        self.current = next_node
    
    def set_choice_function(self, func):
        self.choice_function = func