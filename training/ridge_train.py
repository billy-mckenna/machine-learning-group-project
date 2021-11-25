#Ridge Regression Training
import sys
from sklearn.linear_model import Ridge
from joblib import dump
from data_functions import csv_to_Xy

#Arguments passed from user
data = sys.argv[1]
C = int(sys.argv[2])

#Taking in Data
X, y = csv_to_Xy("processed_data/processed_data" + data + "train.csv")

#Define Model
model = Ridge(1/(2*C))

#Train Model
model.fit(X,y)

#Save Model
dump(model, 'models/ridge_model.joblib')