#Ridge Regression Cross-Validation
import sys
from cv_functions import order_cross_validation, penalty_cross_validation, save_plot
sys.path.insert(0, './data')
from data_functions import csv_to_Xy

#Receive desired dataset from user
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
#order_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #Dataset 5
order_range = [1, 2, 3, 4, 5] #, 6, 7, 8, 9, 10] #Dataset 2
mean_mse_order, std_mse_order, mean_mae_order, std_mae_order, mean_r2_order, std_r2_order = order_cross_validation(X, y, order_range, c, "ridge")

#Plot Cross-Validation Results
x_label_order = "Model Order"
title_order   = "5-fold Cross Validation, Ridge Regression, Alpha=1/(2C), C=" + str(c)
save_plot("cross_validation/plots/ridge_cv_order" + data + "_2.jpg", order_range, title_order, x_label_order, mean_mse_order, std_mse_order, 
mean_mae_order, std_mae_order, mean_r2_order, std_r2_order)

#Cross Validation for C value selection
#C_range = [ 1, 5, 10, 15, 20, 25, 30, 40, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 60, 70, 80, 90, 100] # Dataset 5
#C_range = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20] # Dataset 2
C_range = [0.1, 0.5, 1, 5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100] # Dataset 5 Round 2
#C_range = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20] # Dataset 2 Round 2
mean_mse_C, std_mse_C, mean_mae_C, std_mae_C, mean_r2_C, std_r2_C = penalty_cross_validation(X, y, order, C_range, "ridge")

#Plot Cross-Validation Results
x_label_C = "C"
title_C   = "5-fold Cross Validation, Ridge Regression, Alpha=1/(2C), Order=" + str(order)
save_plot("cross_validation/plots/ridge_cv_penalty" + data + "_2.jpg", C_range, title_C, x_label_C, mean_mse_C, std_mse_C, 
mean_mae_C, std_mae_C, mean_r2_C, std_r2_C)
print("Plots saved!")
