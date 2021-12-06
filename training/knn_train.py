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

#Taking in Data
X, y = csv_to_Xy("data/processed_data/processed_data" + data + "_train.csv")

#KNN doesn't require feature order augmentation.
#This was added in so that the same code could be used to evaluate all 3 models.
#The extra constant feature shouldn't affect performance since all points will have the same same value in this dimension (1).
Poly = PolynomialFeatures(1)
X_poly = Poly.fit_transform(X)

#Define Model
model = KNeighborsRegressor(n_neighbors=neighbours,weights=weights,algorithm='brute')

#Train Model
model.fit(X_poly,y)

#Save Model
dump(model, 'models/knn_model' + data + '.joblib')