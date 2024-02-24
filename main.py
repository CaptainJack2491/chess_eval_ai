import numpy as np
import pandas as pd
from pandas import DataFrame

data:DataFrame = pd.read_csv("./dataset/random_evals.csv")


board: list[str] = [
    "_","_","_","_","_","_","_","_",
    "_","_","_","_","_","_","_","_",
    "_","_","_","_","_","_","_","_",
    "_","_","_","_","_","_","_","_",
    "_","_","_","_","_","_","_","_",
    "_","_","_","_","_","_","_","_",
    "_","_","_","_","_","_","_","_",
    "_","_","_","_","_","_","_","_",
]

def fen_to_array(fen: str) -> list[str]:
    """
    replaces blank value ("_") in {board} with values in FEN

    """
    for letter in fen:
        # rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
        count = 0
        if type(letter) == int:
            count += 1
        elif expression:
            pass


    return board


print(data.FEN[0])
