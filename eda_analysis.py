import pandas as pd

df = pd.read_excel("Dataset for Data Analytics.xlsx")

print(df.head())
print(df.columns)

print("\nDataset Shape:")
print(df.shape)

print("\nSummary Statistics:")
print(df.describe())

print("\nMedian Values:")
print(df.median(numeric_only=True))

print("\nData Types:")
print(df.dtypes)

print("\nTop 10 Products:")
print(df["Product"].value_counts().head(10))

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

outliers = df[
    (df["TotalPrice"] < Q1 - 1.5 * IQR) |
    (df["TotalPrice"] > Q3 + 1.5 * IQR)

]

print("outliers Found:", len(outliers))

import matplotlib.pyplot as plt

df["TotalPrice"].hist()

plt.title("TotalPrice Distribution")
plt.xlabel("TotalPrice")
plt.ylabel("Frequency")

plt.show()

summary = df.describe()

summary.to_excel(
    "EDA_Summary.xlsx"
)

print("EDA Report Saved")