# machine-learning-group-roject

## Install Dependencies

```pip install -r requirements.txt```

## Run Data Scripts  

### Scrape the data from the web
```python data/WebScraper.py```

### Process the scraped data
```python data/DataProcessor.py```

## Cross-validation

### K-Nearest Neighbours Regression
To perform cross-validation of the KNN models run the following command.
```
python cross_validation/knn_cv.py $dataset
```
Arguments:
```
Required:
dataset:  1 = training data from dataset 1
          2 = training data from dataset 2
```
### Run the Linear Regression model
```python models/linearRegression.py```

### Run the KNN model
```python models/knn.py```
