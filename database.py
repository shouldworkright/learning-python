# A showcase of Python's database functionality.
# Author: Dan Mello
# Date: 2020-06-02

# Importing packages
import pandas as pd

# Read data from a .csv file
df = pd.read_csv('mtg_decks.csv')
print(df.head())