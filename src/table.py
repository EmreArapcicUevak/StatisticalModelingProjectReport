import pandas as pd

df = pd.read_csv("Data/StatisticalAnalysisOfTrams.csv")
df.to_latex("Data/StatisticalAnalysisOfTrams.tex", index=False)