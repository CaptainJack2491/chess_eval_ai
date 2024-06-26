# import numpy as np
# import pandas as pd
# from pandas import DataFrame
# import tensorflow as tf

# data:DataFrame = pd.read_csv("./dataset/random_evals.csv")

# Hyprparameters

values:dict = {'p':0.05,'n':0.15,'b':0.15,'r':0.25,'q':0.45,'k':1,0:0}


def split_fen(fen:str) -> list[str]:
    # rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1
    split_fen = fen.split(" ")
    return split_fen



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


def split_array(fen:str) -> list[list]:
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
        
    # print(fen_black)
    # print(fen_white)

    transformed_black = list(map(values.get,fen_black))
    transformed_white = list(map(values.get,fen_white))
    return [transformed_black, transformed_white]



test_fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"
fen = split_fen(test_fen)
position = split_array(fen_to_array(fen[0]))
print(position)

turn:int = 0
if fen[1] == 'b':
    turn = 1

print(fen[5])
# TODO normalize move number



# TODO normalize evaluations
    # TODO splt # into a binary column



