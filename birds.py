#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 10:37:57 2017

@author: tvanheijst
"""

import matplotlib.pyplot as plt
import numpy as np
birddata = pd.read_csv('c:/Users/theijst/Winscript/bird_tracking.csv')
bird_names = pd.unique(birddata.bird_name)

np.isnan(speed).any()
np.sum(np.isnan(speed))

ind=np.isnan(speed)
plt.hist(speed[~ind], bins=np.linpace(0,30,20), normed =True)

#pandas plt
birddata.speed_2d.plot(kind=hist, range=(0,30))
plt.xlabel("2d speed");
plt.savefig()

import datetime
time_1=datetime.today()
date_str=birddata.date_time[0]
datetime.datetime.strptime(date_str[:-3],"%Y-%m-%d")

birddata["timestamp"]=pd.series(timestamps, index=birddata.index)

elapsed_time=[time-time[0] for time in times]

elapsed_days = elapsed_time[1000] /datetime.timedeltaa(days=1)

for (i,t) enumerate (elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        compute mean speed
        daily_mean-speed.append(dnp.mean(data.speeds_2d[ind]))
        next_day += 1
        indes[]

#cartopy
import cartopy.crs as ccrs
iport cartopy.feature as cfeature

proj = ccrs.Mercator

for name in bird_names:
    ix
# First, use `groupby` to group up the data.
grouped_birds = birddata.groupby("bird_name")

# Now operations are performed on each group.
mean_speeds = grouped_birds.speed_2d.mean()

# The `head` method prints the first 5 lines of each bird.
grouped_birds.head()

# Find the mean `altitude` for each bird.
# Assign this to `mean_altitudes`.
mean_altitudes = grouped_birds.altitude.mean()

# Convert birddata.date_time to the `pd.datetime` format.
birddata.date_time = pd.to_datetime(birddata.date_time)

# Create a new column of day of observation
birddata["date"] = birddata.date_time.dt.date

# Check the head of the column.
birddata.date.head()

grouped_bydates = birddata.groupby("date")
mean_altitudes_perday = grouped_bydates.altitude.mean()

grouped_birdday = birddata.groupby(["bird_name","date"])
mean_altitudes_perday = grouped_birdday.altitude.mean()

# look at the head of `mean_altitudes_perday`.
mean_altitudes_perday.head()

eric_speed = birddata.groupby('bird_name').get_group('Eric')
eric_daily_speed  = eric_speed.groupby("date").speed_2d.mean()
sanne_speed = birddata.groupby('bird_name').get_group('Sanne')
sanne_daily_speed  = sanne_speed.groupby("date").speed_2d.mean()
nico_speed = birddata.groupby('bird_name').get_group('Nico')
nico_daily_speed  = nico_speed.groupby("date").speed_2d.mean()

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()
