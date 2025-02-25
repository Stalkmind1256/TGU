import pandas as pd
import numpy as np
import json



df = pd.read_csv("fish.csv")
pd.set_option('display.max_rows', None)  # Показывать все строки
pd.set_option('display.max_columns', None)  # Показывать все столбцы
pd.set_option('display.width', None)  # Полная ширина вывода
pd.set_option('display.max_colwidth', None)

df_copy = df.copy()

print(df_copy.head())

mean_length1_pike = df_copy[df_copy["Species"] == "Pike"]["Length1"].mean()
mean_length1_pike_rounded = round(mean_length1_pike, 1)
print(mean_length1_pike_rounded)

bream_with_width_7 = df_copy[(df_copy["Species"] == "Bream") & (df_copy["Width"] == 7)]
mean_weight_bream = bream_with_width_7["Weight"].mean()
print(mean_weight_bream)