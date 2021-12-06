import numpy as np
import pandas as pd
import category_encoders as ce
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


def one_hot_encode_location(input_data):
    # Takes in data, encodes location and returns new data frame
    X1 = input_data.iloc[:, 1]  # Location
    location_data = pd.DataFrame({'Dublin_Area': X1})
    encoder = ce.OneHotEncoder(cols='Dublin_Area', handle_unknown='return_nan', return_df=True, use_cat_names=True)
    data_encoded = encoder.fit_transform(location_data)
    return data_encoded


def one_hot_encode_property_type(input_data):
    # Takes in data, encodes property type and returns new data frame
    X5 = input_data.iloc[:, 5]  # property type
    property_type_data = pd.DataFrame({'Property_Type': X5})
    encoder = ce.OneHotEncoder(cols='Property_Type', handle_unknown='return_nan', return_df=True, use_cat_names=True)
    data_encoded = encoder.fit_transform(property_type_data)
    return data_encoded


def replace_data(input_data, replacement_data, index):
    left = input_data.iloc[:, :index]
    right = input_data.iloc[:, index + 1:]
    df = left.join(replacement_data)
    df = df.join(right)
    return df


def min_max_scaler(input_data, lower_bound, upper_bound):
    features = input_data[input_data.columns]
    scaler = MinMaxScaler(feature_range=(lower_bound, upper_bound))
    input_data[input_data.columns] = scaler.fit_transform(features.values)
    return input_data


def map_location_to_mean_price(input_data):
    # Takes in data, encodes location and returns new data frame
    df = input_data.copy()
    X1 = df.iloc[:, 1]  # Location
    mean_prices_locations = pd.read_csv('./data/misc_data_files/mean_price_for_location.csv')
    for i in range(0, len(X1), 1):
        mean_price_location = mean_prices_locations.query(f'Zone=={X1[i]}')
        X1[i] = mean_price_location.iloc[:, 1]
    return X1


def split_data(original_data):
    y = original_data.iloc[:, 0]
    X = original_data.iloc[:, 1:]
    xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)
    train = pd.DataFrame({'Price': ytrain}, xtrain)
    test = pd.DataFrame({'Price': ytest}, xtest)
    return train, test


def encode_approach1(input_data):
    # location and property type one hot encoded, different types of scaling used
    original_data = input_data
    encoded_location_data = one_hot_encode_location(original_data)
    location_cols = encoded_location_data.columns.tolist()
    location_cols.sort()
    encoded_property_type_data = one_hot_encode_property_type(original_data)
    property_type_cols = encoded_property_type_data.columns.tolist()
    property_type_cols.sort()
    data = replace_data(original_data, encoded_property_type_data, 6)
    data = replace_data(data, encoded_location_data, 1)
    cols = default_cols[0:1]
    cols = np.append(cols, location_cols)
    cols = np.append(cols, default_cols[2:5])
    cols = np.append(cols, property_type_cols)
    data = data[cols]
    return data


def encode_approach2(input_data):
    # location mapped to mean price value and property type one hot encoded, different types of scaling used
    original_data = input_data
    encoded_location_data = map_location_to_mean_price(original_data)
    encoded_property_type_data = one_hot_encode_property_type(original_data)
    property_type_cols = encoded_property_type_data.columns.tolist()
    property_type_cols.sort()
    data = replace_data(original_data, encoded_property_type_data, 6)
    data = replace_data(data, encoded_location_data, 1)
    cols = default_cols[0:5]
    cols = np.append(cols, property_type_cols)
    data = data[cols]
    return data


# Set Column names of data
default_cols = ['Price', 'Location', 'Beds', 'Baths', 'Square Area', 'Type']

# Read in cleaned data and split into train and test
clean_data = pd.read_csv('./data/raw_data/daft_data_clean.csv')
training_data, test_data = train_test_split(clean_data)

# location and property type one hot encoded, scaled(0, 1)
encoded_data = encode_approach1(clean_data)
encoded_data = min_max_scaler(encoded_data, 0, 1)
training_encoded_data = encoded_data.iloc[training_data.index, :]
test_encoded_data = encoded_data.iloc[test_data.index, :]
training_encoded_data.to_csv('./data/processed_data/processed_data1_train.csv', index=False)
test_encoded_data.to_csv('./data/processed_data/processed_data1_test.csv', index=False)

# location mapped to mean price value and property type one hot encoded, scaled(0, 1)
encoded_data = encode_approach2(clean_data)
encoded_data = min_max_scaler(encoded_data, 0, 1)
training_encoded_data = encoded_data.iloc[training_data.index, :]
test_encoded_data = encoded_data.iloc[test_data.index, :]
training_encoded_data.to_csv('./data/processed_data/processed_data2_train.csv', index=False)
test_encoded_data.to_csv('./data/processed_data/processed_data2_test.csv', index=False)
