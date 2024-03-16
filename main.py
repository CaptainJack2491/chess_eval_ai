# import numpy as np
# import pandas as pd
# from pandas import DataFrame

# data:DataFrame = pd.read_csv("./dataset/random_evals.csv")


def fen_to_array(fen: str) -> str:
    """
    Converts FEN into a string of 64 characters by replacing the numbers by 0s
    """

    final:str = ''
    for letter in fen:
        # r1bqk2r/pp1n2pp/2n1pp2/3pP3/1b1P1P2/3B1N2/PP1B2PP/R2QK1NR
        if letter == '/':
            pass
        elif letter.isdigit():
            for _ in range(int(letter)):
                final += '0'
        else:
            final += letter

    # r0bqk00rpp0n00pp00n0pp00000pP0000b0P0P00000B0N00PP0B00PPR00QK0NR
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
            fen_white.append(i.lower())
            fen_black.append(0)
        elif i.isdigit():
            i_int = int(i)
            fen_white.append(i_int)
            fen_black.append(i_int)
        else:
            fen_white.append(i)
            fen_black.append(i)
        
    print(fen_black)
    print(fen_white)
    return [fen_black, fen_white]


dict = {'p':1,'n':3,'b':3,'r':5,'q':9,'k':20,0:0}


test = fen_to_array("r1bqk2r/pp1n2pp/2n1pp2/3pP3/1b1P1P2/3B1N2/PP1B2PP/R2QK1NR")
test_split = split_fen(test)
print(test)

for i in test_split:
    print(i)
    print(len(i))
    print("******************")



print(list(map(dict.get,test_split[0])))
print(list(map(dict.get,test_split[1])))

# print(data.FEN[0])
