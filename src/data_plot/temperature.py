import matplotlib.pyplot as plt

temp_min = [12, 15, 11, 13, 14, 10, 12]
temp_max = [26, 28, 30, 25, 27, 24, 29]

fig, ax = plt.subplots()

ax.boxplot([temp_min, temp_max], vert=True, notch=False)
ax.set_xticklabels(['MIN', 'MAX'])

plt.savefig('images/temperature.png')
