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

# --- test 3: two-sample t-test ---
# claim: "the average wait time is the same during rush hours and off-peak hours."
# H0: mu1 = mu2
# H1: mu1 != mu2

rush_waits = df[df['rush_hour'] == True]['wait_time_min']
offpeak_waits = df[df['rush_hour'] == False]['wait_time_min']
t_stat2, p_value3 = stats.ttest_ind(rush_waits, offpeak_waits, equal_var=False)

print("\n--- test 3: two-sample t-test ---")
print(f"rush mean: {rush_waits.mean():.3f}, off-peak mean: {offpeak_waits.mean():.3f}")
print(f"T-statistic: {t_stat2:.3f}, p-value: {p_value3:.3f}")

if p_value2 < 0.05:
  print("reject H0. there is a significant difference in wait times between rush hour and off-peak")
else:
  print("fail to reject H0. no significant difference in average wait time during rush hour and off-peak hours")
