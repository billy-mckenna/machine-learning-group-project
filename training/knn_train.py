#KNN Regression Training
import sys
from sklearn.neighbors import KNeighborsRegressor
from joblib import dump
from data_functions import csv_to_Xy

#Arguments passed from user
data = sys.argv[1]
neighbours = int(sys.argv[2])
weights = sys.argv[3]

#Taking in Data
X, y = csv_to_Xy("processed_data/processed_data" + data + "train.csv")

#Define Model
model = KNeighborsRegressor(n_neighbors=neighbours,weights=weights)

#Train Model
model.fit(X,y)

#Save Model
dump(model, 'models/knn_model.joblib')