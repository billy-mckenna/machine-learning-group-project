# machine-learning-group-roject

## Install Dependencies

```pip install -r requirements.txt```

## Run Data Scripts  

### Scrape the data from the web
```python data/web_scraper.py```

### Process the scraped data
```python data/data_processor.py```

## Cross-validation
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
##Training

##Evaluation
