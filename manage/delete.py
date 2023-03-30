import opening
import os

def delete_op(name : str):
    os.remove(f"data/{name}.op")