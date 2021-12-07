# machine-learning-group-roject

## Install Dependencies

```pip install -r requirements.txt```

## Run Data Scripts  

### Scrape the data from the web
```python data/web_scraper.py```

### Process the scraped data
```python data/data_processor.py```

## Cross-validation
The following scripts perform cross-validation and save the results in the cross-validation/plots directory.
### K-Nearest Neighbours Regression
To perform cross-validation of the KNN models run the following command.
```
python cross_validation/knn_cv.py $dataset
```
The usage of the arguments are as follows.
```
(REQUIRED)
dataset: The dataset that will be used for cross-validation.  
1 = training data from dataset 1
2 = training data from dataset 2
```
### Lasso Regression
To perform cross-validation of the Lasso models run the following command.
```
python cross_validation/lasso_cv.py $dataset $order $C
```
The usage of the arguments are as follows.
```
(REQUIRED)
$dataset: The dataset that will be used for cross-validation.
1 = training data from dataset 1
2 = training data from dataset 2

(OPTIONAL)
$order: The polynomial order of the features when cross-validating the value of C. Integer values only.
DEFAULT = 1

$C: The value of C when cross-validating the polynomial order of the features.
DEFAULT = 1
```
### Ridge Regression
To perform cross-validation of the Lasso models run the following command.
```
python cross_validation/ridge_cv.py $dataset $order $C
```
The usage of the arguments are as follows.
```
(REQUIRED)
$dataset: The dataset that will be used for cross-validation 
1 = training data from dataset 1
2 = training data from dataset 2

(OPTIONAL)
$order: The polynomial order of the features when cross-validating the value of C. Integer values only.
DEFAULT = 1

$C: The value of C when cross-validating the polynomial order of the features.
DEFAULT = 1
```
## Training
The following scripts train models on particular dataset and then saves it to the models directory.
### KNN
To train a KNN model run the following command.
```
python training/knn_train.py $dataset $k $weights
```
The usage of the arguments are as follows.
```
(REQUIRED)
$dataset: The dataset that will be used for training
1 = training data from dataset 1
2 = training data from dataset 2

(OPTIONAL)
$k: The number of nearest neighbours that the model considers when making decisions. Integers only.
DEFAULT = 1

$weights: The weighting method used by the model.
uniform = All nearest neighbours are weighted equally.
distance = Nearest neighbours are weighted by their distance from the query point.
```
### Lasso
To train a lasso regression model run the following command.
```
python training/lasso_train.py $dataset $order $C
```
The usage of the arguments are as follows.
```
(REQUIRED)
$dataset: The dataset that will be used for training 
1 = training data from dataset 1
2 = training data from dataset 2

(OPTIONAL)
$order: The polynomial order of the trained model. Integer values only.
DEFAULT = 1

$C: The value of C for the trained model.
DEFAULT = 1
```
### Ridge
To train a lasso regression model run the following command.
```
python training/ridge_train.py $dataset $order $C
```
The usage of the arguments are as follows.
```
(REQUIRED)
$dataset: The dataset that will be used for training 
1 = training data from dataset 1
2 = training data from dataset 2

(OPTIONAL)
$order: The polynomial order of the features for training. Integer values only.
DEFAULT = 1

$C: The value of C for the trained model.
DEFAULT = 1
```
## Evaluation
Command for evaluating the models performance. This will print out the models MSE, MAE, R-squared performance on the test data of the chosen dataset.
```
python evaluation/evaluate.py $model $dataset $order 
```
The usage of the arguments are as follows.
```
(REQUIRED)
$model: The dataset that will be used for evaluation.
knn = Saved knn model
ridge = Saved ridge regression model
lasso = Saved lasso regression model

$dataset: The dataset that will be used for evaluation.
1 = test data from dataset 1
2 = test data from dataset 2

(OPTIONAL)
$order: The polynomial order of the saved model. N/A for KNN.
DEFAULT = 1
```
