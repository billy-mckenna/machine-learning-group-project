import sys
from sklearn.metrics import mean_squared_error, mean_absolute_error
from joblib import load
import data_functions

model = sys.argv[1]
data = sys.argv[2]

X, y = data_functions.csv_to_Xy("processed_data/processed_data" + data + "test.csv")

model = load("models/" + model + "_model.joblib")

y_pred = model.predict(X)

print("MSE: ", mean_squared_error(y_pred=y_pred,y_true=y))
print("MAE: ", mean_absolute_error(y_pred=y_pred,y_true=y))