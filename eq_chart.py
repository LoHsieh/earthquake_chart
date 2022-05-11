# -*- coding: utf-8 -*-
"""
Created on Tue May  3 17:25:55 2022

@author: 1
"""

from get_eqdatas import get_eqdatas
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=get_eqdatas('2021-10-01')

x=df.groupby('區域').count()['id'].index
y=df.groupby('區域').count()['id']

plt.figure(figsize=(12,6))
plt.bar(x,y)
# plt.legend()
# plt.xlabel('salary usd(10,000)')
# plt.xticks(np.linspace(1000,4000,10))
# plt.yticks(np.arange(0,40,4))
# plt.ylim(0,40)
plt.show()