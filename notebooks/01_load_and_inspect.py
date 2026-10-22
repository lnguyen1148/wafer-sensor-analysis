import pandas as pd
from pathlib import path

data_dir = Path("..")/"data"/"raw"
eq1 = pd.read_csv(data_dir/"equipment1.csv", sep=";")
eq2 = pd.read_csv(data_dir/"equipment2.csv", sep=";")
resp = pd.read_csv(data_dir/"response.csv", sep=";")

print("response rows:", len(resp))
print("unique wafers:", resp[["lot", "wafer"]].drop_duplicates().shape[0])

resp = resp.drop_duplicates().reset_index(drop=True)
print("after dedupe:", resp.shape)
print(resp["class"].value_counts())

# Bad-wafer rate per lot
bad_rate = (resp["class"] == "bad").groupby(resp["lot"]).mean()
print(bad_rate.describe())
print("lots with zero bad wafers:", (bad_rate == 0).sum())
