import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer
import tensorflow as tf
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

# Préparation des dataset
train_data = pd.read_csv("sample_train.csv")
test_data = pd.read_csv("sample_test.csv")

# Tokenization
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
text_column_name = "message"

train_tokenized = train_data[text_column_name].apply(lambda x: tokenizer.decode(tokenizer.encode(x, add_special_tokens=True)))
test_tokenized = test_data[text_column_name].apply(lambda x: tokenizer.decode(tokenizer.encode(x, add_special_tokens=True)))

# Modèle
class CustomDataset(Dataset):
    def __init__(self, csv_file, text_column, label_column):
        # Charger le fichier CSV
        self.df = pd.read_csv(csv_file)
        self.text_column = text_column
        self.label_column = label_column

        # Ajouter le prétraitement/tokenisation ici si nécessaire

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        text = self.df.loc[idx, self.text_column]
        label = self.df.loc[idx, self.label_column]

        # Ajouter la tokenisation ici si nécessaire

        return text, label

train_dataset = CustomDataset("sample_train.csv", text_column="message", label_column="label")
test_dataset = CustomDataset("sample_test.csv", text_column="message", label_column="label")

print(train_dataset.__getitem__(2))
