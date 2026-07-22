import pandas as pd

df = pd.read_csv("data_penjualan.csv")

df.columns = df.columns.str.strip()

df = df.drop_duplicates()

df["Paid Fees"] = df["Paid Fees"].str.replace("USD ", "", regex=False)
df["Paid Fees"] = df["Paid Fees"].str.replace(".", "", regex=False)
df["Paid Fees"] = pd.to_numeric(df["Paid Fees"])

df["Paid Fees"] = df["Paid Fees"].fillna(0)
df["Enrolled Courses"] = df["Enrolled Courses"].fillna(0)

df["Training Models"] = df["Training Models"].fillna("Not Enrolled")
df["Training Levels"] = df["Training Levels"].fillna("Not Enrolled")

df.to_csv("data_bersih.csv", index=False)

print("Pembersihan data selesai! File 'data_bersih.csv' berhasil dibuat.")