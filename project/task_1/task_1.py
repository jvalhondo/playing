# Playing with Spanish population dataset
import os

import pandas as pd

print()

df = pd.read_csv(os.path.join(os.path.dirname(__file__)) + '/data_population.csv')

print(df.head())
