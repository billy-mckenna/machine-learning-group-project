#KNN Regression Cross-Validation
import sys
from cv_functions import knn_cross_validation, save_plot
sys.path.insert(0, './data')
from data_functions import csv_to_Xy

#Receive desired dataset from user
data = sys.argv[1]

#Taking in Data
X, y = csv_to_Xy("data/processed_data/processed_data" + data + "_train.csv")

#Choose the range of neighbours you want to use
neighbors_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21, 23, 24, 25, 26, 27, 29, 31]

#Perform KNN Cross-Validation using uniform and distance weights 
mean_mse_uniform, std_mse_uniform, mean_mae_uniform, std_mae_uniform     = knn_cross_validation(X, y, neighbors_range, 'uniform')
mean_mse_distance, std_mse_distance, mean_mae_distance, std_mae_distance = knn_cross_validation(X, y, neighbors_range, 'distance')

#Save plots of Cross-Validation Results
x_label        = "K"
title_uniform  = "5-fold Cross Validation, K-Nearest-Neighbours, Uniform Weights"
title_distance = "5-fold Cross Validation, K-Nearest-Neighbours, Distance Weights"

save_plot("cross_validation/plots/knn_cv_uniform.jpg", neighbors_range, title_uniform, x_label, mean_mse_uniform, std_mse_uniform, mean_mae_uniform, std_mae_uniform)
save_plot("cross_validation/plots/knn_cv_distance.jpg", neighbors_range, title_distance, x_label, mean_mse_distance, std_mse_distance, mean_mae_distance, std_mae_distance)
print("Plots saved!")