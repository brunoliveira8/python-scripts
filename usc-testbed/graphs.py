# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:00:09 2015
@author: bruno
"""

"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def pdr_graph():
    n_groups = 3
    
    normal = (70.56, 0, 0 )
    std_normal = (3.64,0,0)
    
    balanced_80 = (0,  48.43, 0)
    std_balanced_80 = (0, 7.03, 0)
    
    balanced_90 = (0, 0, 27.61)
    std_balanced_90 = (0,0,4.77)
    

    fig, ax = plt.subplots()
    
    index = np.arange(n_groups)
    bar_width = 0.35
    
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    
    rects1 = plt.bar(index, normal, bar_width,
                     alpha=opacity,
                     color='b',
                     yerr=std_normal,
                     error_kw=error_config,
                     label='MRHOF')
    
    rects2 = plt.bar(index, balanced_80, bar_width,
                     alpha=opacity,
                     color='g',
                     yerr=std_balanced_80,
                     error_kw=error_config,
                     label='ALABAMO-80')
    
    
    rects3 = plt.bar(index, balanced_90, bar_width,
                     alpha=opacity,
                     color='r',
                     yerr=std_balanced_90,
                     error_kw=error_config,
                     label='ALABAMO-90')

    
    

    plt.ylabel('Network Delivery Ratio(%)')
    #plt.xticks(index + bar_width, ('MHROF', 'CMST','Balanced 80', 'Balanced 90'))
    plt.xticks(index + 0.2, ('MRHOF','ALABAMO-80', 'ALABAMO-90'))
    #plt.legend(bbox_to_anchor=(1.4, 1))
    
    plt.tight_layout()
    plt.savefig('pdr_bar.eps', format='eps')

def lifetime_graph():
    
    great_value = 34.72
    n_groups = 3
    
    normal = (great_value/34.72, 0, 0)
    std_normal = (0,0,0)
    
    balanced_80 = (0, great_value/16.69, 0)
    std_balanced_80 = (0, 0, 0)
    
    balanced_90 = (0, 0, great_value/21.21)
    std_balanced_90 = (0,0, 0)
  
  
    fig, ax = plt.subplots()
    
    index = np.arange(n_groups)
    bar_width = 0.35
    
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    
    rects1 = plt.bar(index, normal, bar_width,
                     alpha=opacity,
                     color='b',
                     yerr=std_normal,
                     error_kw=error_config,
                     label='MRHOF')
    
    
    rects2 = plt.bar(index, balanced_80, bar_width,
                     alpha=opacity,
                     color='g',
                     yerr=std_balanced_80,
                     error_kw=error_config,
                     label='ALABAMO-80')
    
    
    rects3 = plt.bar(index, balanced_90, bar_width,
                     alpha=opacity,
                     color='r',
                     yerr=std_balanced_90,
                     error_kw=error_config,
                     label='ALABAMO-90')

    
    
    plt.ylabel('Normalized Average Lifetime')
    plt.xticks(index + 0.2, ('MRHOF','ALABAMO-80', 'ALABAMO-90'))
    #plt.legend(bbox_to_anchor=(1.4, 1))
    plt.tight_layout()
   
    plt.savefig('lifetime_bar.eps', format='eps')


def lin_graph():
    x = [27.61, 48.43,70.56]
    y = [1.62,2.01,1] # 10, not 9, so the fit isn't perfect
    
    fit = np.polyfit(x,y,1)
    fit_fn = np.poly1d(fit) 
    # fit_fn is now a function which takes in x and returns an estimate for y
    
    plt.plot(x,y,'ro',x, fit_fn(x), '--k')
    plt.xlim(0, 90)
    plt.ylim(0, 3)
   
pdr_graph()
lifetime_graph()

