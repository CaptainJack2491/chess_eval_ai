import pandas as pd

data = pd.read_csv("./dataset/chessData.csv")

def is_mate(fen):
    if '#' in fen:
        return 1
    else:
        return 0

data['is_mate'] = data.Evaluation.apply(is_mate)

def has_hash(fen):
    if '#' in fen:
        fen.replace('#','')
    else:
        return fen

data['Evaluation'] = data.Evaluation.apply(has_hash)
data.to_csv('chessData.csv', index=False)

print(data)
