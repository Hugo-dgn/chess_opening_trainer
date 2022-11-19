def get_case_pos(n_case, case_size):
        """
        input:
            -n_case : int
        output:
            -x : int
            -y : int
        Transform the number into its position on the board
        """
        x = (n_case%8 + 0.5)*case_size
        y = (7 - n_case//8 + 0.5)*case_size
        return x, y

def get_case_number(x, y, case_size):
    """
    input:
        -x : int
        -y : int
        -case_size : int
    output:
        -n : int
    Convert a click position into the case's number the click hit
    """
    n = x//case_size + (7-y//case_size)*8
    return n