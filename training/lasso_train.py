#Lasso Regression Training
import numpy as np
import pandas as pd
import sys
from sklearn.linear_model import Lasso
from joblib import dump

#Arguments passed from user
C = int(sys.argv[1])

#Taking in Data
df  = pd.read_csv("cross_validation/test_data.csv", parse_dates=True, sep=',')
X1  = df.iloc[:,0]
X2  = df.iloc[:,1]
X   = np.column_stack((X1,X2))
y   = df.iloc[:,2]

#Define Model
model = Lasso(1/(2*C))

#Train Model
model.fit(X,y)

#Save Model
dump(model, 'models/lasso_model.joblib')