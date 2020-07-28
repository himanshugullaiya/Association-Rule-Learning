# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = dataset.values
transactions = np.array(transactions, dtype = np.unicode_)
transactions = transactions.tolist()

from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
res = list(rules)

def nan_remove(s):
      while 'nan' in s:
            s.remove('nan')
      return s
            

results = []
for x in range(len(res)):
      temp = list(res[x][0])
      temp = nan_remove(temp)
      results.append(temp)


all_items = set()
for x in range(20):
    [all_items.add(y) for y in list(dataset[x])]
    