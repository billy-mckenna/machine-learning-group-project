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
neighbors_range = [1, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100]

#Perform KNN Cross-Validation using uniform and distance weights 
mean_mse_uniform, std_mse_uniform, mean_mae_uniform, std_mae_uniform, mean_r2_uniform, std_r2_uniform       = knn_cross_validation(X, y, neighbors_range, 'uniform')
mean_mse_distance, std_mse_distance, mean_mae_distance, std_mae_distance, mean_r2_distance, std_r2_distance = knn_cross_validation(X, y, neighbors_range, 'distance')

#Save plots of Cross-Validation Results
x_label        = "k"
title_uniform  = "5-fold Cross Validation, K-Nearest-Neighbours, Uniform Weights"
title_distance = "5-fold Cross Validation, K-Nearest-Neighbours, Distance Weights"

save_plot("cross_validation/plots/knn_cv_uniform_dataset_" + data + ".jpg", neighbors_range, title_uniform, x_label, mean_mse_uniform, std_mse_uniform, 
mean_mae_uniform, std_mae_uniform, mean_r2_uniform, std_r2_uniform)
save_plot("cross_validation/plots/knn_cv_distance_dataset_" + data + ".jpg", neighbors_range, title_distance, x_label, mean_mse_distance, std_mse_distance, 
mean_mae_distance, std_mae_distance, mean_r2_distance, std_r2_distance)
print("Plots saved!")