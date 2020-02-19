#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:30:40 2020

@author: Miller
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def compound_calc(p_sum, rate, freq, time):
    new_sum = p_sum * (1 + rate / freq) ** (freq * time)
    return new_sum

days = list(range(1,366))
progress = list()
#x and y axes
x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0, 365)
ax.set_ylim(100,3900)
line, = ax.plot(0,0)
present_sum = 100
plt.title("Moving Compound Interest")

for day in days:
    progress.append(present_sum)
    present_sum = compound_calc(present_sum, 0.01, day, 1)

#plt.scatter(days, progress)

def animation_frame(day):
    x_data.append(day)
    y_data.append(progress[day - 1])
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,
    
animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(1,366,1),
                          interval=10, repeat=False)
plt.show()