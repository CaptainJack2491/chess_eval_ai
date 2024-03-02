# import numpy as np
# import pandas as pd
# from pandas import DataFrame

# data:DataFrame = pd.read_csv("./dataset/random_evals.csv")


def fen_to_array(fen: str) -> str:
    """
    Converts FEN into a string of 64 characters

    """
    count:int = 0
    
    final:str = ''
    # create a list of 64 0s
    for letter in fen:
        # rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
        if letter == '/':
            pass
        elif letter.isdigit():
            for _ in range(int(letter)):
                count += 1
                final += '0'
        else:
                final += letter
                count += 1


    return final


def split_fen(fen:str) -> list[list]:
    """
    splits FEN into two lists of strings 
    """
    fen_black:list = []
    fen_white:list = []

    for i in fen:
        if i.islower():
            fen_black.append(i)
            fen_white.append(0)
        elif i.isupper():
            fen_white.append(i)
            fen_black.append(0)
        elif i.isdigit():
            i_int = int(i)
            fen_white.append(i_int)
            fen_black.append(i_int)
        else:
            fen_white.append(i)
            fen_black.append(i)

    return [fen_black, fen_white]



test = fen_to_array("r1bqk2r/pp1n2pp/2n1pp2/3pP3/1b1P1P2/3B1N2/PP1B2PP/R2QK1NR")
test_split = split_fen(test)
print(test)



print("-------------------------")

for i in test_split:
    print(i)
    print(len(i))
    print("******************")




# print(data.FEN[0])
