import matplotlib.pyplot as plt
import numpy as np

years = [1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000]
germany = [29, 51, 59, 478, 93, 244, 420, 510, 575, 625]
france = [28, 46, 57, 52, 63, 93, 190, 275, 310, 355]
uk = [53, 73, 84, 105, 130, 180, 245, 265, 300, 335]
ussr = [40, 70, 80, 105, 205, 480, 725, 935, 1000, 545]

bar_width = 1

pos_germany = [pos + bar_width - 2 * bar_width for pos in years]
pos_france = [pos + 2 * bar_width - 2 * bar_width for pos in years]
pos_uk = [pos + 3 * bar_width - 2 * bar_width for pos in years]
pos_ussr = [pos + 4 * bar_width - 2 * bar_width for pos in years]

plt.figure(figsize=(10, 6))
plt.bar(pos_germany, germany, width=bar_width, label='Germany')
plt.bar(pos_france, france, width=bar_width, label='France', alpha=0.7)
plt.bar(pos_uk, uk, width=bar_width, label='UK', alpha=0.5)
plt.bar(pos_ussr, ussr, width=bar_width, label='USSR', alpha=0.3)
plt.xlabel('Year')
plt.ylabel('Industrial Production')
plt.title('2D Bar Chart of Industrial Production')
plt.xticks(years)
plt.legend()
plt.show()

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

countries = ['Germany', 'France', 'UK', 'USSR']
data = [germany, france, uk, ussr]
colors = ['r', 'g', 'b', 'y']

for i, country_data in enumerate(data):
    ax.bar(years, country_data, zs=i, zdir='y', color=colors[i], alpha=0.7)

ax.set_xlabel('Year')
ax.set_ylabel('Country')
ax.set_zlabel('Industrial Production')
ax.set_yticks(np.arange(len(countries)))
ax.set_yticklabels(countries)

plt.title('3D Bar Chart of Industrial Production')
plt.show()
