#KNN Regression Training
import sys
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures
from joblib import dump
sys.path.insert(0, './data')
from data_functions import csv_to_Xy

#Arguments passed from user
data = sys.argv[1]
neighbours = int(sys.argv[2])
weights = sys.argv[3]
try:
    order = int(sys.argv[4])
except:
    order = 1

#Taking in Data
X, y = csv_to_Xy("data/processed_data/processed_data" + data + "_train.csv")

#Increase order of the model
Poly = PolynomialFeatures(order)
X_poly = Poly.fit_transform(X)

#Define Model
model = KNeighborsRegressor(n_neighbors=neighbours,weights=weights)

#Train Model
model.fit(X_poly,y)

#Save Model
dump(model, 'models/knn_model' + data + '.joblib')