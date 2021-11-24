#KNN Regression Training
import numpy as np
import pandas as pd
import sys
from sklearn.neighbors import KNeighborsRegressor
from joblib import dump

#Arguments passed from user
neighbours = int(sys.argv[1])
weights = sys.argv[2]

#Taking in Data
df  = pd.read_csv("cross_validation/test_data.csv", parse_dates=True, sep=',')
X1  = df.iloc[:,0]
X2  = df.iloc[:,1]
X   = np.column_stack((X1,X2))
y   = df.iloc[:,2]

#Define Model
model = KNeighborsRegressor(n_neighbors=neighbours,weights=weights)

#Train Model
model.fit(X,y)

#Save Model
dump(model, 'models/knn_model.joblib')