import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 5
means_profile = (0.86,0.88,0.92,0.79,0.72)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.20
opacity = 1

rects1 = plt.bar(index, means_profile, bar_width,
                 alpha=opacity,
                 color='b',
                 label='')



plt.xlabel('LR                  LDA              SVM             RF          KNN')
plt.ylabel('Mearsures')
plt.title('Algorithm Comparison')
plt.legend()

plt.tight_layout()
plt.show()