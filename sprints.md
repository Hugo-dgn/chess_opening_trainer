<sprint 1 = Package : board>

Generate a chess board. The player and the program can move
the pieces.

>>>files:

control file:
    -function tied to the board canvas
    -uses board's canvas to get user inputs
    -gives user input into a given function
    -when the user moves a piece, the piece must follow
        the user's mouse

utils file:
    -creates board canvas
    -convert square name into square number (a1 -> 0)
    -load pieces images and get the rect of each pieces on
        the image
    -gives pieces image with correct size

>>>class

Board class :
    -contains the state of the boardin real time
    -contains canvas of the chess board
    -keeps moves history
    -can be reset

>>>function

set_mode function:
    -change the controls according to the game mode

### final implementation of sprint 1 ###

<class board.Board:
    attribute:
        -board : chess.Board
        -canvas : tk.Canvas
        -case_size : int
        -is_fliped : bool
    method:
        -draw(without=[]) : None
            draw pieces on the board without the pieces given
            to the argument without (their square)
        -reset : None
            reset the board to starting position and draw it

<function set_input_handler(function) : None
    set the function called when when the player moves a piece.
    This function must be :
        function(target_square, board) : None
            -target_square : int
            -board : board.Board

<function set_mode(user_to_move) : None
    user_to_move = True -> white to move
    user_to_move = False -> Black to move

<function get_color_to_move : bool
    get_color_to_move() = True -> white to move
    get_color_to_move() = False -> Black to move

<function change_color_to_move : None
    does : user_to_move = not user_to_move

### final implementation of sprint 1 ###

============================================================

<sprint 2 = Pavkage : opening>

Design the data structure use to store openings and repertoire

>>> file

manager file:
    -save opening
    -load opening

>>> class

class Opening:
    -represent a opening
    -have a name
    -the opening is represented by a tree

class Node:
    -use to represent a opening's tree
    -each node is labeled by a move
    -have parent (None if root)
    -have children ([] if end node)

### final implementation of sprint 2 ###

<class Opening:
    attribute:
        -name : str
        -color : chess.Color
        -tree : Node
    method:
        -add(ligne : chess.Move list) : add a ligne
        -delete(ligne : chess.Move list) : deleat a ligne

<function save(op : Opening) : None
    Save the given opening

<function load(op_name : str) : Opening
    load the opening corresponding to the given name

<funciton oplist() : str list
    gives a list of the names of all openings saved

### final implementation of sprint 2 ###

============================================================

<sprint 3 = Package : create>

Allow player to enter new openings to the database. The first
implementation of this function will be with command lignes.

>>>files:

manager file:
    -save openings
    -load openings

>>>function:

get_new_opening(opening) : None
    -update the opening tree in real time
    -use the board to get the moves from the user

### final implementation of sprint 3 ###

<function delete_op(name : str) : None
    remove the given opening from the database

<function delete_ligne(op : opening.Opening, ligne : list)
    delete an entire ligne from the given opening

<function delete_last_move(op : opening.Opening, ligne :list) : None
    delete the last move from the given opening

### final implementation of sprint 3 ###