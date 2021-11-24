import pandas as pd
import category_encoders as ce
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
    input_data[data.columns] = scaler.fit_transform(features.values)
    return input_data


def map_location_to_mean_price(input_data):
    # Takes in data, encodes location and returns new data frame
    X1 = input_data.iloc[:, 1]  # Location
    mean_prices_locations = pd.read_csv('mean_price_for_location.csv')
    for i in range(0, len(X1), 1):
        mean_price_location = mean_prices_locations.query(f'Zone=={X1[i]}')
        X1[i] = mean_price_location.iloc[:, 1]
    return X1


# Read in data
original_data = pd.read_csv('daft_data_clean.csv')

# processed_data1.csv - location and property type one hot encoded, no scaling
original_data = pd.read_csv('daft_data_clean.csv')
encoded_location_data = one_hot_encode_location(original_data)
encoded_property_type_data = one_hot_encode_property_type(original_data)
data = replace_data(original_data, encoded_property_type_data, 5)
data = replace_data(data, encoded_location_data, 1)
data.to_csv('processed_data1.csv')

# processed_data2.csv - location and property type one hot encoded, scaled(0, 1)
original_data = pd.read_csv('daft_data_clean.csv')
encoded_location_data = one_hot_encode_location(original_data)
encoded_property_type_data = one_hot_encode_property_type(original_data)
data = replace_data(original_data, encoded_property_type_data, 5)
data = replace_data(data, encoded_location_data, 1)
data = min_max_scaler(data, 0, 1)
data.to_csv('processed_data2.csv')

# processed_data3.csv - location and property type one hot encoded, scaled(-1, 1)
original_data = pd.read_csv('daft_data_clean.csv')
encoded_location_data = one_hot_encode_location(original_data)
encoded_property_type_data = one_hot_encode_property_type(original_data)
data = replace_data(original_data, encoded_property_type_data, 5)
data = replace_data(data, encoded_location_data, 1)
data = min_max_scaler(data, -1, 1)
data.to_csv('processed_data3.csv')

# processed_data4.csv - location mapped to mean price value and property type one hot encoded, no scaling
original_data = pd.read_csv('daft_data_clean.csv')
encoded_location_data = map_location_to_mean_price(original_data)
encoded_property_type_data = one_hot_encode_property_type(original_data)
data = replace_data(original_data, encoded_property_type_data, 5)
data = replace_data(data, encoded_location_data, 1)
data.to_csv('processed_data4.csv')

# processed_data5.csv - location mapped to mean price value and property type one hot encoded, scaled(0, 1)
original_data = pd.read_csv('daft_data_clean.csv')
encoded_location_data = map_location_to_mean_price(original_data)
encoded_property_type_data = one_hot_encode_property_type(original_data)
data = replace_data(original_data, encoded_property_type_data, 5)
data = replace_data(data, encoded_location_data, 1)
data = min_max_scaler(data, 0, 1)
data.to_csv('processed_data5.csv')

# processed_data6.csv - location and mean price value and property type one hot encoded, scaled(-1, 1)
original_data = pd.read_csv('daft_data_clean.csv')
encoded_location_data = map_location_to_mean_price(original_data)
encoded_property_type_data = one_hot_encode_property_type(original_data)
data = replace_data(original_data, encoded_property_type_data, 5)
data = replace_data(data, encoded_location_data, 1)
data = min_max_scaler(data, -1, 1)
data.to_csv('processed_data6.csv')
