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

# --- test 4: chi-squared test of independence ---
# claim: "tram type distribution is same during rush and off-peak hours"
# H0: tram type and time of day are independent
# H1: tram type and time of day are not independent

contingency_table = pd.crosstab(df['tram_type'], df['rush_hour'])
print(contingency_table)

chi2, p_value4, dof, expected = stats.chi2_contingency(contingency_table)

print("\n--- test 4: chi-squared test of independence ---")
print(f"\nchi-squared statistic: {chi2:.3f}, p-value: {p_value4:.3f}, degrees of freedom: {dof}, expected: {expected}")

if p_value4 < 0.05:
  print("reject H0: type of tram and time of day are dependent, distribution changes")
else:
  print("fail to reject H0: no evidence that tram type distribution is different based on time of day")