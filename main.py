import pandas as pd
import numpy as np
import preprocess as pp

data:pd.DataFrame = pd.read_csv("./dataset/chessData.csv")

# normalize eval
normalized_data = pp.normalize_eval(data)

final_data = np.array(normalized_data['FEN'].apply(pp.FEN_to_arry))

print(normalized_data.shape)
print(final_data.shape)
