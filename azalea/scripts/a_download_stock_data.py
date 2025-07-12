import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))  # ← back to quant/
sys.path.insert(0, root_path)

from src.utils import get_stock_data

df = get_stock_data('AAPL')  # Example ticker
df.columns = ['_'.join(col) if isinstance(col, tuple) else col for col in df.columns]

# Basic EDA
eda_summary = {
    "head": df.head(),
    "describe": df.describe(),
    "missing": df.isnull().sum()
}

buf = io.StringIO()
df.info(buf=buf)
eda_summary["info"] = buf.getvalue()

# Save text summary
with open("z_eda_summary.md", "w") as f:
    f.write("# EDA Summary\n\n")
    f.write("## Head\n")
    f.write(eda_summary["head"].to_markdown())
    f.write("\n\n## Describe\n")
    f.write(eda_summary["describe"].to_markdown())
    f.write("\n\n## Missing Values\n")
    f.write(eda_summary["missing"].to_markdown())
    f.write("\n\n## Info\n")
    f.write("```\n" + eda_summary["info"] + "\n```")

# Plot example: Closing price over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x=df.index, y="Close_AAPL")
plt.title("Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.tight_layout()
plt.savefig("z_closing_price_plot.png")


def main(ticker='AAPL'):
    #print(raw_data[['Open', 'Close']].head())  # Display the first few rows of the data
    pass

if __name__ == "__main__":
    main()