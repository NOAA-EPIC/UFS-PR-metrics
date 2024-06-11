# Import the necessary modules
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import numpy.ma as ma
import pandas as pd
import sys

# Initialize the lists for X and Y
try:
    app = sys.argv[1]
except:
    print('Usage: plot_bar.py <app (ufs-wm, srw, upp)> <mean outlier cutoff in days>')
    exit(1)

mean_outlier = 50
try:
    data = pd.read_csv(f"../ufs-weather-model/{app}-prtime.csv")
except:
    print(f"Invalid app or .csv dataset not available for '{app}'")
    exit(1)

df = pd.DataFrame(data)

x = list(df.iloc[:, 0])
y = list(df.iloc[:, 2])
pr = list(df.iloc[:, 1])

y_ = np.array(y)
y_mean = np.mean(ma.masked_where(y_ > mean_outlier, y_))
print(y_mean)

fig, ax = plt.subplots(1, 1)
ax.bar(x, y, width=0.5)
plt.text(20, y_.max(), f"Mean = {y_mean:.2f} days", fontsize=8)
ax.set_xticks(x)
# Set ticks labels for x-axis
ax.set_xticklabels(pr, rotation=60, fontsize=6)
tick_spacing = 10
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax.yaxis.set_major_locator(ticker.MultipleLocator(15))
# Show the plot
# ax.invert_xaxis()
plt.title(f"{app.upper()} PR Turnaround Time")
plt.xlabel("Pull Requests")
plt.ylabel("Days")
plt.tight_layout()

plt.savefig(f"../ufs-weather-model/{app}-prtime.png")
plt.show()
