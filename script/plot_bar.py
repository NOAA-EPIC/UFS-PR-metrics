# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
import numpy.ma as ma
  
# Initialize the lists for X and Y
data = pd.read_csv('ufs-wm.csv')
  
df = pd.DataFrame(data)
  
x = list(df.iloc[:, 0])
y = list(df.iloc[:, 2])
pr= list(df.iloc[:, 1])

y_=np.array(y)
y_mean = np.mean(ma.masked_where(y_ > 50, y_))
print(y_mean)
  
fig, ax = plt.subplots(1,1) 
ax.bar(x,y,width=0.5)
plt.text(20, 200, 'Mean = 14.38days', fontsize=8)
ax.set_xticks(x)
# Set ticks labels for x-axis
ax.set_xticklabels(pr, rotation=60, fontsize=6)
tick_spacing=3
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
# Show the plot
ax.invert_xaxis()
plt.title("UFS-WM PR Turnaround Time")
plt.xlabel("Pull Requests")
plt.ylabel("Days")
plt.tight_layout()

plt.savefig('ufs-wm-pr.png')
plt.show()
