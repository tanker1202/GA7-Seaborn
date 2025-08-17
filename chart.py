# chart.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Generate synthetic data ---
np.random.seed(42)
months = pd.date_range(start='2024-01-01', periods=12, freq='M').strftime('%b')
segments = ['Retail', 'Wholesale', 'Online']

data = []
for segment in segments:
    base_revenue = np.random.randint(100000, 200000)  # base monthly revenue
    seasonal_trend = np.sin(np.linspace(0, 2*np.pi, 12)) * 20000  # seasonal pattern
    noise = np.random.normal(0, 5000, 12)  # random variation
    monthly_revenue = base_revenue + seasonal_trend + noise
    for month, revenue in zip(months, monthly_revenue):
        data.append({'Month': month, 'Segment': segment, 'Revenue': max(0, revenue)})

df = pd.DataFrame(data)

# --- 2. Seaborn styling ---
sns.set_style("whitegrid")
sns.set_context("talk")
palette = sns.color_palette("Set2")

# --- 3. Create the lineplot ---
# Directly set figure size in pixels: 512px / 100 dpi = 5.12 inches
fig = plt.figure(figsize=(8, 8))  # exact 512x512 pixels
ax = sns.lineplot(data=df, x='Month', y='Revenue', hue='Segment', marker='o', palette=palette)
plt.title("Monthly Revenue Trend by Customer Segment", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.xticks(rotation=45)

# --- 4. Save chart ---
fig.savefig('chart.png', dpi=64, bbox_inches='tight')  # exact 512x512 pixels
plt.close(fig)

