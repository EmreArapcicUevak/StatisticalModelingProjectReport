
from statsmodels.stats.power import TTestIndPower
import numpy as np
import matplotlib.pyplot as plt

# Initialize power analysis tool
analysis = TTestIndPower()

# Significance level
alpha = 0.05

# Sample sizes from dataset
n1 = df[df['rush_hour'] == True].shape[0]
n2 = df[df['rush_hour'] == False].shape[0]

# Effect sizes from 0 to 2 (Cohen's d)
effect_sizes = np.linspace(0, 2, 100)

# Compute statistical power for each effect size
powers = analysis.power(effect_size=effect_sizes, nobs1=n1, ratio=n2/n1, alpha=alpha, alternative='two-sided')

# Plotting the power curve
plt.figure(figsize=(8,5))
plt.plot(effect_sizes, powers, color='blue')
plt.axhline(0.8, color='red', linestyle='--', label='80% power')
plt.title('Power Curve (Type II Error Analysis)')
plt.xlabel("Effect Size (Cohen's d)")
plt.ylabel('Power (1 - beta)')
plt.grid(True)
plt.legend()
plt.savefig("Plot_PowerCurve.pdf", format='pdf')
plt.show()