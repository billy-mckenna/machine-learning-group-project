#Ridge Regression Cross-Validation
import numpy as np
import pandas as pd
from cv_functions import order_cross_validation, penalty_cross_validation, save_plot

#Taking in Data
df  = pd.read_csv("test_data.csv", parse_dates=True, sep=',')
X1  = df.iloc[:,0]
X2  = df.iloc[:,1]
X   = np.column_stack((X1,X2))
y   = df.iloc[:,2]

#Cross Validation for model order selection
order_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 5
mean_mse_order, std_mse_order, mean_mae_order, std_mae_order = order_cross_validation(X, y, order_range, c, "ridge")

#Plot Cross-Validation Results
x_label_order = "Model Order"
title_order   = "5-fold Cross Validation, Ridge Regression, Alpha=1/(2C), C=" + str(c)
save_plot("plots/ridge_cv_order.jpg", order_range, title_order, x_label_order, mean_mse_order, std_mse_order, mean_mae_order, std_mae_order)

#Cross Validation for C value selection
C_range = [0.1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
order = 1
mean_mse_C, std_mse_C, mean_mae_C, std_mae_C = penalty_cross_validation(X, y, order, C_range, "ridge")

#Plot Cross-Validation Results
x_label_C = "C"
title_C   = "5-fold Cross Validation, Ridge Regression, Alpha=1/(2C), Order=" + str(order)
save_plot("plots/ridge_cv_penalty.jpg", C_range, title_C, x_label_C, mean_mse_C, std_mse_C, mean_mae_C, std_mae_C)
