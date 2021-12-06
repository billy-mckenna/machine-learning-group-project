#Lasso Regression Training
import sys
from sklearn.linear_model import Lasso
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

#Select the polynomial order of the features
Poly = PolynomialFeatures(order)
X_poly = Poly.fit_transform(X)

#Define Model
model = Lasso(1/(2*C))

#Train Model
model.fit(X_poly, y)

#Useful print statements for investigating features, parameters and biases
"""
print(Poly.get_feature_names())
print("Coefs: ", model.coef_)
print("Bias: ", model.intercept_)
"""

#Save Model
dump(model, 'models/lasso_model' + data + '.joblib')