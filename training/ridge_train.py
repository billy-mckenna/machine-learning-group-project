#Ridge Regression Training
import sys
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from joblib import dump
sys.path.insert(0, './data')
from data_functions import csv_to_Xy

#Arguments passed from user
data = sys.argv[1]
order = int(sys.argv[2])
C = int(sys.argv[3])

#Taking in Data
X, y = csv_to_Xy("data/processed_data/processed_data" + data + "_train.csv")

#Increase order of the model
Poly = PolynomialFeatures(order)
X_poly = Poly.fit_transform(X)

#Define Model
model = Ridge(1/(2*C))

#Train Model
model.fit(X_poly, y)

#Save Model
dump(model, 'models/ridge_model' + data + '.joblib')