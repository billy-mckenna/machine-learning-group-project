#Lasso Regression Cross-Validation
import sys
from cv_functions import order_cross_validation, penalty_cross_validation, save_plot
from data_functions import csv_to_Xy

#Receive desired dataset from user
data = sys.argv[1]

#Taking in Data
X, y = csv_to_Xy("processed_data/processed_data" + data + "train.csv")

#Cross Validation for model order selection
order_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 100
mean_mse_order, std_mse_order, mean_mae_order, std_mae_order = order_cross_validation(X, y, order_range, c, "lasso")

#Plot Cross-Validation Results
x_label_order = "Model Order"
title_order   = "5-fold Cross Validation, Lasso Regression, Alpha=1/(2C), C=" + str(c)
save_plot("plots/lasso_cv_order.jpg", order_range, title_order, x_label_order, mean_mse_order, std_mse_order, mean_mae_order, std_mae_order)

#Cross Validation for C value selection
C_range = [0.1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
order = 1
mean_mse_C, std_mse_C, mean_mae_C, std_mae_C = penalty_cross_validation(X, y, order, C_range, "lasso")

#Plot Cross-Validation Results
x_label_C = "C"
title_C   = "5-fold Cross Validation, Lasso Regression, Alpha=1/(2C), Order=" +str(order)
save_plot("plots/lasso_cv_penalty.jpg", C_range, title_C, x_label_C, mean_mse_C, std_mse_C, mean_mae_C, std_mae_C)
