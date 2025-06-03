import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from google.colab import files
from statsmodels.stats.power import TTestIndPower

sheet_url = "https://docs.google.com/spreadsheets/d/1iE6yzRM2TUnQBB84oONAYN-Gcyi0DyJYGSgQQp3whSA/export?format=csv"
df = pd.read_csv(sheet_url)

df.rename(columns={'Tram ID': 'tram_id', 'Station': 'station', 'Direction': 'direction', 'Tram Type': 'tram_type', 'Wait Time (s)': 'wait_time_sec', 'Timestamp': 'timestamp', 'Time Slot': 'time_slot'}, inplace=True)
df['wait_time_min'] = (df['wait_time_sec'] / 60).round(2)
df['timestamp'] = pd.to_datetime(df['timestamp'], dayfirst=True, format="%d.%m.%Y. %H:%M:%S")

df[['tram_id', 'station', 'direction', 'tram_type', 'timestamp', 'wait_time_min', 'time_slot']].head()

# add rush hour labelling
def label_rush_hour(timestamp):
    hour = timestamp.hour
    return (6 <= hour <= 8) or (16 <= hour <= 18)

df['rush_hour'] = df['timestamp'].apply(label_rush_hour)

# --- test 1: one-sample proportion test ---
# claim: “the proportion of new trams is 50%.”
# H₀: p = 0.50
# H₁: p ≠ 0.50

n_total = len(df)
n_new = len(df[df['tram_type'] == "New"])
p_sample = n_new / n_total
p0 = 0.5

z_stat = (p_sample - p0) / np.sqrt(p0 * (1-p0) / n_total)
p_value1 = 2 * (1- stats.norm.cdf(abs(z_stat)))

print("\n--- test 1: one-sample proportion z-test ---")
print(f"Z-statistic: {z_stat:.3f}, p-value: {p_value1:.3f}")
if p_value1 < 0.05:
  print("reject H0. proportion of new trams is significantly different from 50%")
else:
  print("fail to reject H0. there is no significant difference from a 50% proportion")