import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import KFold
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge, Lasso

def order_cross_validation(X, y, order_range, C, model_type):
    mean_mse=[]; std_mse=[]
    mean_mae=[]; std_mae=[]
    
    for order in order_range:
        if model_type == "ridge":
            model  = Ridge(alpha=(1/(2*C)))
        else:
            model  = Lasso(alpha=(1/(2*C)))
        
        Poly   = PolynomialFeatures(order)
        X_poly = Poly.fit_transform(X)
        kf     = KFold(n_splits=5)

        mse_temp = []
        mae_temp = []    

        for train, test in kf.split(X_poly):
            model.fit(X_poly[train], y[train])
            ypred = model.predict(X_poly[test])
            mse_temp.append(mean_squared_error(y[test],ypred))
            mae_temp.append(mean_absolute_error(y[test],ypred))
        
        mean_mse.append(np.array(mse_temp).mean())
        std_mse.append(np.array(mse_temp).std())
        mean_mae.append(np.array(mae_temp).mean())
        std_mae.append(np.array(mae_temp).std())
    
    return mean_mse, std_mse, mean_mae, std_mae

def penalty_cross_validation(X, y, order, C_range, model_type):
    mean_mse=[]; std_mse=[]
    mean_mae=[]; std_mae=[]
    
    for Ci in C_range:
        if model_type == "ridge":
            model  = Ridge(alpha=(1/(2*Ci)))
        else:
            model  = Lasso(alpha=(1/(2*Ci)))
        
        Poly   = PolynomialFeatures(order)
        X_poly = Poly.fit_transform(X)
        kf     = KFold(n_splits=5)

        mse_temp = []
        mae_temp = []    

        for train, test in kf.split(X_poly):
            model.fit(X_poly[train], y[train])
            ypred = model.predict(X_poly[test])
            mse_temp.append(mean_squared_error(y[test],ypred))
            mae_temp.append(mean_absolute_error(y[test],ypred))
        
        mean_mse.append(np.array(mse_temp).mean())
        std_mse.append(np.array(mse_temp).std())
        mean_mae.append(np.array(mae_temp).mean())
        std_mae.append(np.array(mae_temp).std())
    
    return mean_mse, std_mse, mean_mae, std_mae

def knn_cross_validation(X, y, neighbors_range, weights):
    mean_mse=[]; std_mse=[]
    mean_mae=[]; std_mae=[]
    
    for neighbor in neighbors_range:
        model = KNeighborsRegressor(n_neighbors=neighbor,weights=weights)
        kf    = KFold(n_splits=5)

        mse_temp = []
        mae_temp = []    

        for train, test in kf.split(X):
            model.fit(X[train], y[train])
            ypred = model.predict(X[test])
            mse_temp.append(mean_squared_error(y[test],ypred))
            mae_temp.append(mean_absolute_error(y[test],ypred))
        
        mean_mse.append(np.array(mse_temp).mean())
        std_mse.append(np.array(mse_temp).std())
        mean_mae.append(np.array(mae_temp).mean())
        std_mae.append(np.array(mae_temp).std())
    
    return mean_mse, std_mse, mean_mae, std_mae

def save_plot(filepath, range, title, x_label, mean_mse, std_mse, mean_mae, std_mae):
    #Plot Cross-Validation Results
    fig = plt.figure(figsize=(8,7))

    sp1 = fig.add_subplot(211)
    sp1.set_title(title)
    sp1.errorbar(range, mean_mse, yerr=std_mse)
    sp1.set_xlabel(x_label)
    sp1.set_ylabel('Mean Squared Error')

    sp2 = fig.add_subplot(212)
    sp2.errorbar(range, mean_mae, yerr=std_mae)
    sp2.set_xlabel(x_label)
    sp2.set_ylabel('Mean Absolute Error')

    fig.savefig(filepath)