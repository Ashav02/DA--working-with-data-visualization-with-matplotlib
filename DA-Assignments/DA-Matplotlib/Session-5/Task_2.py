""""Plot a histogram of IPL match scores (runs per team in a match) using plt.hist() and experiment with bins=5, bins=10, and bins=15. 
Observe and describe how changing the number of bins affects the shape of the histogram.
 <br><br><em><strong>Hint:</strong> Use any sample array of 50-60 scores between 120 and 220.</em>
"""

import matplotlib.pyplot as plt

scores = [132, 156, 178, 201, 145, 189, 220, 167, 154, 193,
    175, 212, 148, 181, 205, 163, 197, 229, 140, 186,
    158, 202, 174, 191, 136, 215, 169, 184, 151, 208]

#Plot histogram with bins=5, bins=10, and bins=15
plt.hist(scores, bins=5, color='orange', edgecolor='gray')
plt.hist(scores, bins=10, color='blue', edgecolor='gray')
plt.hist(scores, bins=15, color='green', edgecolor='gray')

plt.xlabel('Match Scores')
plt.ylabel('Frequency')
plt.title('Histogram of IPL Match Scores (bins=5)')
plt.grid(alpha=0.3)
plt.show()  
