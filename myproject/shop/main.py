# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import shutil
import os
import numpy as np
import pandas as pd
from apyori import apriori
import pickle

store_data = pd.read_csv('C:/Users/AsusG531/PycharmProjects/pythonProject1/myproject/shop/store_data.csv', header=None)
store_data.head()

df_shape = store_data.shape
n_of_transactions = df_shape[0]
n_of_products = df_shape[1]

# Converting our dataframe into a list of lists for Apriori algorithm
records = []
for i in range(0, n_of_transactions):
    records.append([])
    for j in range(0, n_of_products):
        if (str(store_data.values[i,j]) != 'nan'):
            records[i].append(str(store_data.values[i,j]))
        else:
            continue
# Run the apriori algorithm
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=2, max_length=5)
association_results = list(association_rules)

# Get all the products listed in dataset
# First merge all the columns of the data frame to a data series object
merged = store_data[0]
for i in range(1,n_of_products):
    merged = merged.append(store_data[i])

# Then rank all the unique products
ranking = merged.value_counts(ascending=False)
# Extract the products in order without their respective count
ranked_products = list(ranking.index)

lookup_table = {}
for item in association_results:

    # First index of the inner list contains base item and add item
    pair = item[0]
    items = [x for x in pair]

    # If we do not have 3 recommendations for our base product we will
    # suggest top ranked products in addition
    if len(items) < 4:
        items_to_append = items
        i = 0
        while len(items) < 4:
            if ranked_products[i] not in items:
                items_to_append.append(ranked_products[i])
            i += 1

    # Add the items to db, with base product separately from the products
    # that are to be recommended
    lookup_table[items_to_append[0]] = items_to_append[1:]
    print(lookup_table)