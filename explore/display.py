import board

def draw_arrow(chess_board, explorer):
    board.delete_arrows(chess_board)
    for node in explorer.current.childrens:
        board.draw_arrow(node.move.from_square, node.move.to_square, chess_board)