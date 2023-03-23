import os

import tkinter as tk
import argparse

import manage
import board
import opening

root = tk.Tk()

chess_board = board.Board(root, 80)
chess_board.canvas.pack()
chess_board.draw()

def create_opening(vars):
    name = vars[1]
    color = vars[0].lower() == "w"
    op = opening.Opening(name, color)
    opening.save(op)

def add_ligne(name):
    op = opening.load(name)
    manage.insert_mode(op)
    root.mainloop()

def print_tree(name):
    op = opening.load(name)
    print(op.tree)

def main():
    parser = argparse.ArgumentParser(
                    prog = 'chess opening trainer',
                    description = 'the program helps you learn openings')
    parser.add_argument('action', type=str,
                        choices=["create",
                                    "delete",
                                    "add",
                                    "tree",
                                    "list"])
    
    parser.add_argument('vars', nargs='*')
    args = parser.parse_args()

    if args.action == "create":
        create_opening(args.vars)

    if args.action == "delete":
        manage.delete_op(args.vars[0])
    
    elif args.action == "add":
        add_ligne(args.vars[0])
    
    elif args.action == "tree":
        print_tree(args.vars[0])
    
    elif args.action == "list":
        print(os.listdir("data"))
        
if __name__ == "__main__":
    main()