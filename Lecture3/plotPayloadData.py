import numpy as np
from matplotlib import pyplot as plt

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

# ------------- function to plot payload of single partition (EB+, EB-, EE)
def plotPayload(time, paymean, partition, ylim):
    fig, ax = plt.subplots(figsize=(16, 6), dpi=580, facecolor='white')
    ax.scatter(time, paymean)
    ax.set_title( 'Payload '+partition, fontsize=16)
    if ylim: plt.ylim(0,50000/1024)
    trans = ax.get_xaxis_transform()
    plt.xlabel('Time (unix timestamp)')
    plt.ylabel('SuperFragment size (kB)')
    
    for key,value in months.items():
        ax.axvline(value[1], color = 'firebrick')
        plt.text(value[1]+value[1]/100000, .8, key, transform=trans, color='firebrick', fontsize=14)
    
    plt.savefig('images/'+partition+'payload.png')

# ------------- function to plot payload of barrel
def plotPayloadBarrel(time, paymean1, paymean2, partition, ylim):
    fig, ax = plt.subplots(figsize=(16, 6), dpi=580, facecolor='white')
    ax.scatter(time, paymean1, facecolors='none', edgecolors='mediumblue', alpha=0.5, label='EB+')
    ax.scatter(time, paymean2, facecolors='none', edgecolors='cornflowerblue', alpha=0.5, label='EB+')
    ax.set_title( 'Payload '+partition, fontsize=16)
    if ylim: plt.ylim(0,50000/1024)
    trans = ax.get_xaxis_transform()
    plt.xlabel('Time (unix timestamp)')
    plt.ylabel('SuperFragment size (kB)')
    plt.legend()
    
    for key,value in months.items():
        ax.axvline(value[1], color = 'firebrick')
        plt.text(value[1]+value[1]/100000, .8, key, transform=trans, color='firebrick', fontsize=14)
    
    plt.savefig('images/BARRELpayload.png')


plotPayload(data[0],data[1]/1024,'EB+',True)
plotPayload(data[0],data[3]/1024,'EB-',True)
plotPayload(data[0],data[5]/1024,'EE',True)

plotPayloadBarrel(data[0],data[1]/1024, data[3]/1024, 'ECAL barrel',True)
