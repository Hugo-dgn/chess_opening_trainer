import os

import tkinter as tk
import argparse

import manage
import board
import opening
import explore

root = tk.Tk()

chess_board = board.Board(root, 60)

def start():
    chess_board.canvas.pack()
    chess_board.draw()
    root.mainloop()

def check_flip(op):
    if not op.color:
        chess_board.is_fliped = True
        chess_board.draw()
    else:
        chess_board.is_fliped = False
        chess_board.draw()

def create_opening(vars):
    name = vars[1]
    color = vars[0].lower() == "w"
    op = opening.Opening(name, color)
    opening.save(op)

def train_opening(name):
    op = opening.load(name)
    check_flip(op)
    explore.train_mode(op, chess_board)
    start()

def explore_opening(name):
    op = opening.load(name)
    check_flip(op)
    explore.explore_mode(op, chess_board, root)
    start()

def edit_opening(name):
    op = opening.load(name)
    check_flip(op)
    explore.edit_mode(op, chess_board, root)
    start()
    opening.save(op)

def add_ligne(name):
    op = opening.load(name)
    check_flip(op)
    manage.insert_mode(op)
    start()
    opening.save(op)

def print_tree(name):
    op = opening.load(name)
    print(op.tree)

def print_names(args):
    if len(args) > 0:
        color = args[0]
        ops = explore.get_op(color=="w" or color=="white")
        for op in ops:
            print(op.name)
    else:
        ops = explore.get_all_op()
        for op in ops:
            print(op.name)

def main():
    parser = argparse.ArgumentParser(
                    prog = 'chess opening trainer',
                    description = 'the program helps you learn openings')
    parser.add_argument('action', type=str,
                        choices=["create",
                                    "delete",
                                    "add",
                                    "tree",
                                    "list",
                                    "train",
                                    "explore",
                                    "edit"])
    
    parser.add_argument('vars', nargs='*')
    args = parser.parse_args()

    if args.action == "create":
        create_opening(args.vars)

    elif args.action == "delete":
        manage.delete_op(args.vars[0])
    
    elif args.action == "add":
        add_ligne(args.vars[0])
    
    elif args.action == "tree":
        print_tree(args.vars[0])
    
    elif args.action == "list":
        print_names(args.vars)
    
    elif args.action == "train":
        train_opening(args.vars[0])
    
    elif args.action == "explore":
        explore_opening(args.vars[0])
    elif args.action == "edit":
        edit_opening(args.vars[0])
        
if __name__ == "__main__":
    main()