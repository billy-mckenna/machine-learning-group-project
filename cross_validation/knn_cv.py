#KNN Regression Cross-Validation
import numpy as np
import pandas as pd
from cv_functions import knn_cross_validation, save_plot

#Taking in Data
df  = pd.read_csv("test_data.csv", parse_dates=True, sep=',')
X1  = df.iloc[:,0]
X2  = df.iloc[:,1]
X   = np.column_stack((X1,X2))
y   = df.iloc[:,2]

#Choose the range of neighbours you want to use
neighbors_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21, 23, 24, 25, 26, 27, 29, 31]

#Perform KNN Cross-Validation using uniform and distance weights 
mean_mse_uniform, std_mse_uniform, mean_mae_uniform, std_mae_uniform     = knn_cross_validation(X, y, neighbors_range, 'uniform')
mean_mse_distance, std_mse_distance, mean_mae_distance, std_mae_distance = knn_cross_validation(X, y, neighbors_range, 'distance')

#Save plots of Cross-Validation Results
x_label        = "K"
title_uniform  = "5-fold Cross Validation, K-Nearest-Neighbours, Uniform Weights"
title_distance = "5-fold Cross Validation, K-Nearest-Neighbours, Distance Weights"

save_plot("plots/knn_cv_uniform.jpg", neighbors_range, title_uniform, x_label, mean_mse_uniform, std_mse_uniform, mean_mae_uniform, std_mae_uniform)
save_plot("plots/knn_cv_distance.jpg", neighbors_range, title_distance, x_label, mean_mse_distance, std_mse_distance, mean_mae_distance, std_mae_distance)
