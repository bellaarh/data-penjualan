import pandas as pd

df = pd.read_csv("data_penjualan.csv")

print("--- 5 BARIS PERTAMA ---")
print(df.head())

print("\n--- INFORMASI DATA ---")
print(df.info())

print("\n--- JUMLAH DATA KOSONG ---")
print(df.isnull().sum())

print("\n--- JUMLAH BARIS DUPLIKAT ---")
print(df.duplicated().sum())