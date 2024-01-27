import numpy as np
import pandas as pd


def fen_to_array(fen: str) -> list[list]:
    board: list[list] = [
        [fen],
    ]

    return board


ans = fen_to_array("test")

for answer in ans:
    print(answer)
