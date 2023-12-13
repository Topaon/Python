import pandas as pd
from sklearn.model_selection import train_test_split

import tensorflow as tf

# Charger le dataset depuis le fichier CSV
train_data = pd.read_csv("sample_train.csv")
test_data = pd.read_csv("sample_test.csv")

print(train_data)
print(test_data)

all_data = pd.concat([train_data, test_data])

print(all_data)