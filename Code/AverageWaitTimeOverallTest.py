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

# --- test 2: one-sample t-test ---
# claim: GRAS says average wait time is 4 minutes
# H0: mu = 4
# H1: mu != 4

sample_mean = df['wait_time_min'].mean()
t_stat, p_value2 = stats.ttest_1samp(df['wait_time_min'], popmean=4)

print("\n--- test 2: one-sample t-test ---")
print(f"sample mean: {sample_mean:.3f}")
print(f"T-statistic: {t_stat:.3f}, p-value: {p_value2:.3f}")

if p_value2 < 0.05:
    print("reject H0. average wait time is significantly different from 4 minutes")
else:
    print("fail to reject H0. no significant difference from the 4-minute average")