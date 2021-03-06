#Lasso Regression Cross-Validation
import sys
from cv_functions import order_cross_validation, penalty_cross_validation, save_plot
sys.path.insert(0, './data')
from data_functions import csv_to_Xy

#Receive desired dataset and optional settings from user
data = sys.argv[1]
try:
    order = int(sys.argv[2])
except:
    order = 1
try:
    c = int(sys.argv[3])
except:
    c = 1

#Taking in Data
X, y = csv_to_Xy("data/processed_data/processed_data" + data + "_train.csv")

#Cross Validation for model order selection
order_range = [1, 2, 3, 4, 5]#, 6, 7, 8, 9, 10]
mean_mse_order, std_mse_order, mean_mae_order, std_mae_order, mean_r2_order, std_r2_order = order_cross_validation(X, y, order_range, c, "lasso")

#Plot Cross-Validation Results
x_label_order = "q"
title_order   = "5-fold Cross Validation, Lasso Regression, Alpha=1/(2C), C=" + str(c)
save_plot("cross_validation/plots/lasso_cv_order_dataset_" + data + ".jpg", order_range, title_order, x_label_order, mean_mse_order, std_mse_order, 
mean_mae_order, std_mae_order, mean_r2_order, std_r2_order)

#Cross Validation for C value selection
C_range = [1, 5, 10, 50, 100, 200, 500, 1000, 1500, 2000, 5000]
mean_mse_C, std_mse_C, mean_mae_C, std_mae_C, mean_r2_C, std_r2_C = penalty_cross_validation(X, y, order, C_range, "lasso")

#Plot Cross-Validation Results
x_label_C = "C"
title_C   = "5-fold Cross Validation, Lasso Regression, Alpha=1/(2C), Order=" +str(order)
save_plot("cross_validation/plots/lasso_cv_penalty_dataset_" + data + ".jpg", C_range, title_C, x_label_C, mean_mse_C, std_mse_C, 
mean_mae_C, std_mae_C, mean_r2_C, std_r2_C)
print("Plots saved!")
