# -*- coding: utf-8 -*-
"""
Created on Tue May  3 17:25:55 2022

@author: 1
"""

from get_eqdatas import get_eqdatas
import matplotlib.pyplot as plt
from datetime import date

df=get_eqdatas('2021-10-01')

x=df.groupby('區域').count()['id'].index
y=df.groupby('區域').count()['id']

plt.figure(figsize=(12,6))
plt.bar(x,y)
plt.ylabel('counts',labelpad=12,fontsize=18)

max_y=df.groupby('區域').count()['id'].max()
plt.text(-1.5,max_y*1.1,f'2021-10-01 ~ {date.today()} earthquake occurrence counting',fontsize=18)
plt.show()