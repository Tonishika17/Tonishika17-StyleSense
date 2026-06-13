import pandas as pd

print("Starting...")

df = pd.read_csv(
    "data/dataset.csv"
)

print("Loaded!")

print(df.columns)