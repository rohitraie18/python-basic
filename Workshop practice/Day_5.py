"""
#Task 1: Load the dataset that contains data on investments (marketing, R&D, and administration) and profits.
import pandas as pd

# Load the dataset
file_path = '"C:\Users\Ace\Downloads\HousePrices.csv"'  # Replace with the actual path to your dataset
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
housing_data = pd.read_csv('C:\Users\Ace\Downloads\HousePrices.csv')

# Display the first few rows to understand the data
print(housing_data.head())