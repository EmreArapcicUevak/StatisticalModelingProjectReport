import pandas as pd

import pandas as pd

df = pd.read_csv("Data/StatisticalAnalysisOfTrams.csv")

column_widths = [
    "p{0.1\\textwidth}",
    "p{0.12\\textwidth}",
    "p{0.12\\textwidth}",
    "p{0.08\\textwidth}",
    "p{0.11\\textwidth}",
    "p{0.12\\textwidth}",
    "p{0.1\\textwidth}",
    "p{0.15\\textwidth}"
]
column_format = "".join(column_widths)  # no spaces

latex_body = df.to_latex(
    index=False,
    escape=False,
    header=True,
    longtable=True,
    column_format=column_format
)

# Save to file
with open("Data/StatisticalAnalysisOfTrams.tex", "w") as f:
    f.write(latex_body)