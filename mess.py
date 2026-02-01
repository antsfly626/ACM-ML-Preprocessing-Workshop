# mess up dataset add uneeded col

import pandas as pd

df = pd.read_csv("laptopData.csv")

df = df.rename(columns={"Weight": "Weight (kg)"})

kg_numeric = pd.to_numeric(
    df["Weight (kg)"]
    .str.replace("kg", "", regex=False)
    .str.strip(),
    errors="coerce"
)

df["Weight (lbs)"] = (kg_numeric * 2.20462).round(2).astype("string") + " lbs"

cols = list(df.columns)
kg_idx = cols.index("Weight (kg)")
cols.remove("Weight (lbs)")
cols.insert(kg_idx + 1, "Weight (lbs)")

df = df[cols]


df.to_csv("laptopData.csv", index=False)

# fix something
df = pd.read_csv("laptopData.csv")
df = df[df["Weight (kg)"] != "?"]
df.to_csv("laptopData.csv", index=False)
