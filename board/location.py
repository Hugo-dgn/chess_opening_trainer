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