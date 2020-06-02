#!env python

# Import libs
import pandas as pd
import numpy as np

def RNA_Regression(dataV, targetV, seed, algorithm, max_iteractions, es):
    data_train, data_test, target_train, target_test = train_test_split(dataV, targetV, random_state=seed, test_size=0.2)
    regression = MLPRegressor(random_state=seed, early_stopping=es, max_iter=max_iteractions, solver=algorithm).fit(data_train, target_train)
    score = regression.score(data_test, target_test)
    return score

# Import data
data_filename = "dados/pre_processed_data.csv"
data = pd.read_csv(data_filename)

# Separating target attribute
target = data['absences']
data = data.drop(columns=['absences'])
original = data

# Scikit Learn MLP Regression
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

# My training
seed = 1
algorithm = 'sgd'
max_iteractions = 10000
early_stopping = True

# {G1, G2, G3}
score = RNA_Regression(data, target, seed, algorithm, max_iteractions, early_stopping)
print(f"[G1, G2, G3] - Score: {score}")

# {G1, G2}
data = original.drop(columns=['G3'])
score = RNA_Regression(data, target, seed, algorithm, max_iteractions, early_stopping)
print(f"[G1, G2]     - Score: {score}")

# {G1, G3}
data = original.drop(columns=['G2'])
score = RNA_Regression(data, target, seed, algorithm, max_iteractions, early_stopping)
print(f"[G1, G3]     - Score: {score}")

# {G2, G3}
data = original.drop(columns=['G1'])
score = RNA_Regression(data, target, seed, algorithm, max_iteractions, early_stopping)
print(f"[G2, G3]     - Score: {score}")

# {G1}
data = original.drop(columns=['G2', 'G3'])
score = RNA_Regression(data, target, seed, algorithm, max_iteractions, early_stopping)
print(f"[G1]         - Score: {score}")

# {G2}
data = original.drop(columns=['G1', 'G3'])
score = RNA_Regression(data, target, seed, algorithm, max_iteractions, early_stopping)
print(f"[G2]         - Score: {score}")

# {G3}
data = original.drop(columns=['G1', 'G2'])
score = RNA_Regression(data, target, seed, algorithm, max_iteractions, early_stopping)
print(f"[G3]         - Score: {score}")

# {}
data = original.drop(columns=['G1', 'G2', 'G3'])
score = RNA_Regression(data, target, seed, algorithm, max_iteractions, early_stopping)
print(f"[]           - Score: {score}")