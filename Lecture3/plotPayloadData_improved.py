import numpy as np
from matplotlib import pyplot as plt

# ------------------------ plt improved params

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Lucida Grande']})
# --------------------------------------------



data = np.loadtxt('payloadData.txt', skiprows=1)
data = np.transpose(data)
# 0 --> timestamp
# 1 EB+ (mean)
# 2 EB+ (devst)

# 3 EB- (mean)
# 4 EB- (devst)

# 5 EE (mean)
# 6 EE (devst)

#import matplotlib.dates as md

import datetime

timestamps = []
for ts in data[0]:
    timestamps.append(datetime.datetime.fromtimestamp(ts/1000).strftime('%Y-%m-%d %H:%M:%S'))
#print (timestamps)

months = {
          'April'  : ['2024-04',None],
          'May'    : ['2024-05',None],
          'June'   : ['2024-06',None],
          'July'   : ['2024-07',None],
          'August' : ['2024-08',None]
        }


for num,ts in enumerate(timestamps):
    for key,value in months.items():
        if value[0] in ts and value[1] == None:
            #print ("first date of april", ts)
            value[1] = data[0][num]
#print (months)


# ------------- plotting payload all together

fig, ax = plt.subplots(2, figsize=(16, 15), dpi=580, facecolor='white')

ax[1].scatter(data[0], data[5]/1024)
ax[0].scatter(data[0], data[1]/1024, facecolors='none', edgecolors='mediumblue', alpha=0.5, label='EB+')
ax[0].scatter(data[0], data[3]/1024, facecolors='none', edgecolors='cornflowerblue', alpha=0.5, label='EB-')
ax[0].legend(fontsize=14)
ax[0].set_title( 'Payload of ECAL in 2024', fontsize=18)
ax[0].set_ylim(0,50000/1024)
ax[1].set_ylim(0,50000/1024)
trans = ax[0].get_xaxis_transform()
trans1 = ax[1].get_xaxis_transform()
ax[0].set_ylabel('SuperFragment size (kB) - EB partitions', fontsize=16)
ax[1].set_xlabel('Time (unix timestamp)', fontsize=16)
ax[1].set_ylabel('SuperFragment size (kB) - EE partitions', fontsize=16)

for key,value in months.items():
    ax[0].axvline(value[1], color = 'firebrick')
    ax[1].axvline(value[1], color = 'firebrick')
    ax[0].text(value[1]+value[1]/100000, .8, key, transform=trans, color='firebrick', fontsize=18)
    ax[1].text(value[1]+value[1]/100000, .8, key, transform=trans1, color='firebrick', fontsize=18)

plt.subplots_adjust(wspace=0, hspace=0.1)
plt.savefig('images/payload_improved.png')


