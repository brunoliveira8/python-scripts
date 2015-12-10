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
    n_groups = 4
    
    normal = (70.56, 0, 0, 0 )
    std_normal = (3.64,0,0, 0)
    
    balanced_80 = (0,  48.43, 0, 0)
    std_balanced_80 = (0, 7.03, 0, 0)
    
    balanced_90 = (0, 0, 27.61, 0 )
    std_balanced_90 = (0,0,4.77, 0)
    
    cmst = (0,0,0,75.15)
    std_cmst = (0,0,0,0.75)
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
                     label='MHROF')
    
    rects2 = plt.bar(index, balanced_80, bar_width,
                     alpha=opacity,
                     color='g',
                     yerr=std_balanced_80,
                     error_kw=error_config,
                     label='ALABAMO-80')
    
    
    rects3 = plt.bar(index, balanced_90, bar_width,
                     alpha=opacity,
                     color='y',
                     yerr=std_balanced_90,
                     error_kw=error_config,
                     label='ALABAMO-90')

    rects4 = plt.bar(index, cmst, bar_width,
                     alpha=opacity,
                     color='r',
                     yerr=std_cmst,
                     error_kw=error_config,
                     label='CMST')
    
    

    plt.ylabel('Network Delivery Ratio(%)')
    #plt.xticks(index + bar_width, ('MHROF', 'CMST','Balanced 80', 'Balanced 90'))
    plt.xticks(index + 0.2, ('MHROF','ALABAMO-80', 'ALABAMO-90', 'CMST'))
    #plt.legend(bbox_to_anchor=(1.4, 1))
    
    plt.tight_layout()
    plt.savefig('pdr_bar.eps', format='eps')

def lifetime_graph():
    
    great_value = 15.53
    n_groups = 4
    
    normal = (great_value/15.53, 0, 0, 0 )
    std_normal = (0,0,0, 0)
    
    balanced_80 = (0, great_value/7.71, 0, 0)
    std_balanced_80 = (0, 0, 0, 0)
    
    balanced_90 = (0, 0, great_value/9.58, 0)
    std_balanced_90 = (0,0, 0, 0)
    
    cmst = (0, 0,0,great_value/9.72)
    std_cmst = (0, 0, 0 ,0)
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
                     label='MHROF')
    
    
    rects2 = plt.bar(index, balanced_80, bar_width,
                     alpha=opacity,
                     color='g',
                     yerr=std_balanced_80,
                     error_kw=error_config,
                     label='ALABAMO-80')
    
    
    rects3 = plt.bar(index, balanced_90, bar_width,
                     alpha=opacity,
                     color='y',
                     yerr=std_balanced_90,
                     error_kw=error_config,
                     label='ALABAMO-90')
    
    rects4 = plt.bar(index, cmst, bar_width,
                     alpha=opacity,
                     color='r',
                     yerr=std_cmst,
                     error_kw=error_config,
                     label='CMST')   
    
    
    
    plt.ylabel('Normalized Average Lifetime')
    plt.xticks(index + 0.2, ('MHROF','ALABAMO-80', 'ALABAMO-90', 'CMST'))
    #plt.legend(bbox_to_anchor=(1.4, 1))
    plt.tight_layout()
   
    plt.savefig('lifetime_bar.eps', format='eps')

pdr_graph()
lifetime_graph()