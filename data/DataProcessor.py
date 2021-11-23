import pandas as pd
import numpy as np

# Read in CSV with location values
df = pd.read_csv('location_values.csv')
X1 = df.iloc[:, 2]  # MinMax
X2 = df.iloc[:, 3]  # std
X3 = df.iloc[:, 3]  # robust
X = np.column_stack((X1, X2, X3))
zones = df.iloc[:, 0]
