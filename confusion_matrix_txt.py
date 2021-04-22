import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import copy
import matplotlib as mpl

#valiue
df = pd.DataFrame([[0.001,0.055,0.005,0.006,0.022,0.022,0.007,0.961],
                   [0.001,0.114,0.012,0.001,0.027,0.072,0.914,0.011],
                   [0.000,0.204,0.003,0.029,0.067,0.782,0.044,0.002],
                   [0.000,0.111,0.000,0.039,0.835,0.079,0.022,0.018],
                   [0.000,0.008,0.000,0.923,0.045,0.022,0.003,0.003],
                   [0.000,0.052,0.970,0.000,0.001,0.016,0.007,0.001],
                   [0.000,0.455,0.011,0.001,0.004,0.007,0.003,0.004],
                   [0.997,0.001,0.000,0.000,0.000,0.001,0.000,0.000]],
                   index=['water', 'baregd', 'grass', 'tree', 'bamboo', 'road', 'clutter', 'backgd'], 
                   columns=['backgd', 'clutter', 'road', 'bamboo', 'tree', 'grass', 'baregd', 'water'])
fig, ax = plt.subplots()
im = ax.pcolor(df)
data = df.values
for x in range(data.shape[0]):
    for y in range(data.shape[1]):
        plt.text(x+0.5, y+0.5, data[x,y], horizontalalignment='center', verticalalignment='center')
 
cmap = copy.copy(mpl.cm.get_cmap("PuBu"))
cmap.set_under('w', alpha=1)
cmap.set_over('b',alpha=0.1)

#color
cover_df = pd.DataFrame([[0.001,0.001,0.000,0.000,0.000,0.000,0.000,0.997],
                        [0.055,0.114,0.204,0.111,0.008,0.052,0.455,0.001],
                        [0.005,0.012,0.003,0.000,0.000,0.970,0.011,0.000],
                        [0.006,0.001,0.029,0.039,0.923,0.000,0.001,0.000],
                        [0.022,0.027,0.067,0.835,0.045,0.001,0.004,0.000],
                        [0.022,0.072,0.782,0.079,0.022,0.016,0.007,0.001],
                        [0.007,0.914,0.044,0.022,0.003,0.007,0.003,0.000],
                        [0.961,0.011,0.002,0.018,0.003,0.001,0.004,0.000]],
                         index=['water', 'baregd', 'grass', 'tree', 'bamboo', 'road', 'clutter', 'backgd'],  
                         columns=['backgd', 'clutter', 'road', 'bamboo','tree', 'grass', 'baregd', 'water'])

im2 = ax.pcolor(cover_df, vmin=0, vmax=1, cmap='PuBu', edgecolors='k', linewidths=.3)#
 
fig.colorbar(im2, ax=ax)
plt.yticks(np.arange(0.5, len(df.columns), 1), df.columns.values)
plt.xticks(np.arange(0.5, len(df.index), 1), df.index.values)#, rotation=45

plt.savefig('./CM_txt2.png')
print("完成")

'''
                  [[0.96,0.01,0.00,0.02,0.00,0.00,0.00,0.00],
                   [0.01,0.91,0.04,0.02,0.00,0.01,0.00,0.00],
                   [0.02,0.07,0.78,0.08,0.02,0.02,0.01,0.00],
                   [0.02,0.03,0.07,0.84,0.04,0.00,0.00,0.00],
                   [0.01,0.00,0.03,0.04,0.92,0.00,0.00,0.00],
                   [0.00,0.01,0.00,0.00,0.00,0.97,0.01,0.00],
                   [0.05,0.11,0.20,0.11,0.01,0.05,0.46,0.00],
                   [0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.00]]
'''
