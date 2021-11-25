import csv
import pandas as pd


data = pd.read_csv('daft_data_clean.csv')
location_counts = data['Address'].value_counts()
property_type_counts = data['Type'].value_counts()
print("Location Counts")
print(location_counts)
print("Property Type Counts")
print(property_type_counts)
