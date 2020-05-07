# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:53:34 2020

@author: ASUS
"""
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib. animation as animation
#import plotly
from  IPython.display import HTML


##数据处理合并
'''
f = pd.ExcelFile('人口数据.xlsx')
y=f.sheet_names
df = pd.DataFrame()
for i in y[:-2]:
    d = pd.read_excel('人口数据.xlsx', sheet_name= i)
    df = pd.concat([df, d],axis=0)
df.to_excel('新人口数据.xlsx')
'''
##解决字中文体问题

from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="/Library/Fonts/Songti.ttc")



#读取数据
df1 = pd.read_excel('新人口数据.xlsx')  #, usecols=['nation', 'group', 'year', 'value']
df = pd.read_excel(r'C:\Users\ASUS\Desktop\新人口数据.xlsx')  #, usecols=['nation', 'group', 'year', 'value']
current_year = 2018

y=df['nation']
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
colors = dict(zip(
    ['亚洲', '美洲', '非洲', '大洋洲', '欧洲'],
    ['#FF0000', '#00FFFF', '#FFA500', '#00FFFF','#1E90FF']
))
group_lk = df.set_index('nation')['group'].to_dict()

fig, ax = plt.subplots(figsize=(25, 12))

def draw_barchart(year):
    
    dff1 = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(14)  #ascending=false也可
    dff = df[df['year'].eq(year)][0:12].sort_values(by='value', ascending=True)  #ascending=false也可
    print(dff)
    print(df[df['year'].eq(year)])
    ax.clear()
    ax.barh(dff['nation'], dff['value']*100, color=[colors[group_lk[x]] for x in dff['nation']])
    dx = dff['value'].max() / 1000
    plt.xlim(21,55)  #可随数据源修改
    for i, (value, nation) in enumerate(zip(dff['value'], dff['nation'])):
        #pass
        a=100*value-100*dx
        b=100*value-100*dx
        c=100*value+100*dx
        d=100*value
        ax.text(a, i,     nation,           size=14, weight=600, ha='right', va='bottom')
        ax.text(b, i-.25, group_lk[nation], size=10, color='#444444', ha='right', va='baseline')
        ax.text(c, i,     str(f'{d:,.1f}')+'%',  size=14, ha='left',  va='center')
    print(value,'&',dx,i)
    # ... polished styles
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#666667', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Percentage (%)', transform=ax.transAxes, size=12, color='#777777')
    
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    
    ax.text(0.08, 1.10, 'The proportion of women in every country in the world from 2010 to 2018',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    ax.text(0.958, 0.05, 'Made BY XFXZ',
            transform=ax.transAxes, size=12, weight=600, color='#00FFFF',ha='left')
    plt.box(False)
draw_barchart(2018)

animator = animation.FuncAnimation(fig, draw_barchart,frames=range(2010, 2019),interval=1314)
#animator.save('demo-bar-race-womenrate-new.gif')    
    
    