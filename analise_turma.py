
# 0. Importe as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_turma.csv', sep=';');

print(df.head())

df.describe()