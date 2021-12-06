import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge, Lasso

def order_cross_validation(X, y, order_range, C, model_type):
    #Cross-validation for determining the optimal polynomial order of the features.
    #Ridge and Lasso only
    mean_mse=[]; std_mse=[]
    mean_mae=[]; std_mae=[]
    mean_r2 =[]; std_r2 =[]
    
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
        r2_temp  = [] 

        for train, test in kf.split(X_poly):
            model.fit(X_poly[train], y[train])
            ypred = model.predict(X_poly[test])
            mse_temp.append(mean_squared_error(y[test],ypred))
            mae_temp.append(mean_absolute_error(y[test],ypred))
            r2_temp.append(r2_score(y[test],ypred))
        
        mean_mse.append(np.array(mse_temp).mean())
        std_mse.append(np.array(mse_temp).std())
        mean_mae.append(np.array(mae_temp).mean())
        std_mae.append(np.array(mae_temp).std())
        mean_r2.append(np.array(r2_temp).mean())
        std_r2.append(np.array(r2_temp).std())
    
    return mean_mse, std_mse, mean_mae, std_mae, mean_r2, std_r2

def penalty_cross_validation(X, y, order, C_range, model_type):
    #Cross-validation for determining the optimal penalty parameter value (C).
    #Ridge and Lasso only
    mean_mse=[]; std_mse=[]
    mean_mae=[]; std_mae=[]
    mean_r2 =[]; std_r2 =[]
    
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
        r2_temp  = []    

        for train, test in kf.split(X_poly):
            model.fit(X_poly[train], y[train])
            ypred = model.predict(X_poly[test])
            mse_temp.append(mean_squared_error(y[test],ypred))
            mae_temp.append(mean_absolute_error(y[test],ypred))
            r2_temp.append(r2_score(y[test],ypred))
        
        mean_mse.append(np.array(mse_temp).mean())
        std_mse.append(np.array(mse_temp).std())
        mean_mae.append(np.array(mae_temp).mean())
        std_mae.append(np.array(mae_temp).std())
        mean_r2.append(np.array(r2_temp).mean())
        std_r2.append(np.array(r2_temp).std())
    
    return mean_mse, std_mse, mean_mae, std_mae,  mean_r2, std_r2

def knn_cross_validation(X, y, neighbors_range, weights):
    #Cross-validation for determining the optimal number of neighbours for KNN.
    #Can support all of sklearns weighting options.
    mean_mse=[]; std_mse=[]
    mean_mae=[]; std_mae=[]
    mean_r2 =[]; std_r2 =[]
    
    for neighbor in neighbors_range:
        model = KNeighborsRegressor(n_neighbors=neighbor,weights=weights)
        kf    = KFold(n_splits=5)

        mse_temp = []
        mae_temp = []
        r2_temp  = []    

        for train, test in kf.split(X):
            model.fit(X[train], y[train])
            ypred = model.predict(X[test])
            mse_temp.append(mean_squared_error(y[test],ypred))
            mae_temp.append(mean_absolute_error(y[test],ypred))
            r2_temp.append(r2_score(y[test],ypred))
        
        mean_mse.append(np.array(mse_temp).mean())
        std_mse.append(np.array(mse_temp).std())
        mean_mae.append(np.array(mae_temp).mean())
        std_mae.append(np.array(mae_temp).std())
        mean_r2.append(np.array(r2_temp).mean())
        std_r2.append(np.array(r2_temp).std())
    
    return mean_mse, std_mse, mean_mae, std_mae,  mean_r2, std_r2

def save_plot(filepath, range, title, x_label, mean_mse, std_mse, mean_mae, std_mae, mean_r2, std_r2):
    #Plot Cross-Validation Results
    #MAE and R^2 subplots were removed as we focused on MSE performance.
    fig = plt.figure(figsize=(24,16))
    plt.rcParams.update({'font.size': 32})
    plt.rcParams.update({'axes.labelsize': 64})

    #sp1.set_title(title) #Uncomment to add subplot titles feature

    sp1 = fig.add_subplot(111) #Change to fig.add_subplot(311) to include the other 2 subplots 
    sp1.errorbar(range, mean_mse, yerr=std_mse)
    sp1.set_xlabel(x_label)
    sp1.set_ylabel('Mean Squared Error')

    #Uncomment the below code to view MAE and R^2 performance during CV.
    # sp2 = fig.add_subplot(312)
    # sp2.errorbar(range, mean_mae, yerr=std_mae)
    # sp2.set_xlabel(x_label)
    # sp2.set_ylabel('Mean Absolute Error')

    # sp2 = fig.add_subplot(313)
    # sp2.errorbar(range, mean_r2, yerr=std_r2)
    # sp2.set_xlabel(x_label)
    # sp2.set_ylabel('R2')

    fig.savefig(filepath)
