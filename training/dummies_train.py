#Lasso Regression Training
import sys
from sklearn.dummy import DummyRegressor
from sklearn.preprocessing import PolynomialFeatures
from joblib import dump
sys.path.insert(0, './data')
from data_functions import csv_to_Xy

#Arguments passed from user
data = sys.argv[1]

#Taking in Data
X, y = csv_to_Xy("data/processed_data/processed_data" + data + "_train.csv")

#Increase order of the model
Poly = PolynomialFeatures(1)
X_poly = Poly.fit_transform(X)

#Define Model
mean_model = DummyRegressor(strategy="mean")
median_model = DummyRegressor(strategy="median")

#Train Model
mean_model.fit(X_poly, y)
median_model.fit(X_poly, y)

#Save Model
dump(mean_model, 'models/mean_dummy_model' + data + '.joblib')
dump(median_model, 'models/median_dummy_model' + data + '.joblib')