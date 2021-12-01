import sys
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from joblib import load
sys.path.insert(0, './data')
import data_functions

model = sys.argv[1]
data = sys.argv[2]
try:
    order = int(sys.argv[3])
except:
    order = 1

X, y = data_functions.csv_to_Xy("data/processed_data/processed_data" + data + "_test.csv")

Poly = PolynomialFeatures(order)
X_poly = Poly.fit_transform(X)

model = load("models/" + model + "_model" + data + ".joblib")

y_pred = model.predict(X_poly)

print("MSE: ", mean_squared_error(y_pred=y_pred,y_true=y))
print("MAE: ", mean_absolute_error(y_pred=y_pred,y_true=y))
print("R2 Score", r2_score(y_pred=y_pred,y_true=y))