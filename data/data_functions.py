import pandas as pd
import numpy as np

def csv_to_Xy(file):
    df  = pd.read_csv(file, parse_dates=True, sep=',')
    y   = df.iloc[:,0]
    X = df.iloc[:,1]

    for i in range(len(df.columns) - 2):
        temp = df.iloc[:, i+2]
        X = np.column_stack((X, temp))

    return X, y