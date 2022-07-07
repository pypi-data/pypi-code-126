#Import libraries for the below code
import numpy as np
import pandas as pd #datafram functions
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind #ttest functions

#2 bars graph but only an paired t-test for within groups within 1 paramater
def cbar_pttest(df, para, grp, legend, title, ymax):
    #Statistics: mean, sem, count (msc)
    msc = df.groupby([grp,legend])[para].agg(['mean','sem','count']) #for each combination between grp and legend
    msc.reset_index(inplace=True) #converts any columns in index as columns
    pd.DataFrame(msc)

    #Statistics: t.test two tailed unpaired 
    u1,u2 = df[grp].unique(),df[legend].unique()#retrieve unique subgroups name from grp (u1) and legend (u2)
    df1,df2 = df[df[grp]==u1[0]],df[df[grp]==u1[1]] #seperate main df to individual df according to u1
    df1,df2,df3,df4 = df1[df1[legend] == u2[0]],df1[df1[legend] == u2[1]],df2[df2[legend] == u2[0]], df2[df2[legend] == u2[1]] #each seperate df seperated according to u2 
    ttest1, ttest2 = ttest_rel(df1[para], df2[para]), ttest_rel(df3[para],df4[para]) #ttest function for grp and legend
    pval1,pval2 = ttest1[1],ttest2[1] #extract pval for significance annotations for graph
    print(para, pval1,pval2)

    #Bar Graph: Numerical Information for graphs
    y1,y2 = msc[msc[legend]==u2[0]],msc[msc[legend]==u2[1]]
    y1,yerr1,y2,yerr2 = y1['mean'].to_numpy(),y1['sem'].to_numpy(),y2['mean'].to_numpy(),y2['sem'].to_numpy()
    x1=np.arange(len(y1)) #x1 and y1 positions need to be equal

    #Bar Graph: Create
    fig = plt.figure()
    fig, ax = plt.subplots(1,1)
    bar_width = 0.3 #seperate two bar graphs
    b1 = ax.bar(x1, y1,width=bar_width, color='#92414e') #bar graph 1
    b2 = ax.bar(x1+bar_width, y2,width=bar_width,color='#200e11') #bar graph 2
    ax.errorbar(x1, y1, yerr=yerr1,fmt=' ', capsize=(3),zorder=0, ecolor='k')
    ax.errorbar(x1+bar_width, y2, yerr=yerr2,fmt=' ', capsize=(3),zorder=0, ecolor='k')
    ax.legend([b1, b2], labels=u2,
            loc='upper right',bbox_to_anchor=(1,1))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticks(x1+bar_width/2) #you need this to properly position your xtick labels
    ax.set_xticklabels(u1)
    ax.set_title(title)
    ax.set_ylabel(para.replace('_',' ')+'(g)'); ax.set_ylim(top=ymax) #y-label but remove '_' and ymax

    #Significance lines for pval 1
    ymerge = np.array([[i, j] for i, j in zip(yerr1+y1, yerr2+y2)]).ravel() #determine height of sig bar by combining b1 and b2 yerr and y values
    if pval1 <= 0.0001:
        text = '****'
        x = (x1[0]+bar_width)/2 #in between two bars
        y = 1.01*max(ymerge[0],ymerge[1])
        props = {'connectionstyle':'bar','arrowstyle':'-','shrinkA':5,'shrinkB':5,'linewidth':2}
        ax.annotate(text,xy=(x,y*1.08),zorder=10,ha='center',fontsize=15) #text annotation
        ax.annotate('',xy=(x1[0],y),xytext=(x1[0]+bar_width,y),arrowprops=props) #annotates line
    elif pval1 <= 0.001:
        text='***'
        x = (x1[0]+bar_width)/2 #in between two bars
        y = 1.01*max(ymerge[0],ymerge[1])
        props = {'connectionstyle':'bar','arrowstyle':'-','shrinkA':5,'shrinkB':5,'linewidth':2}
        ax.annotate(text,xy=(x,y*1.1),zorder=10,ha='center',fontsize=15) #text annotation
        ax.annotate('',xy=(x1[0],y),xytext=(x1[0]+bar_width,y),arrowprops=props) #annotates line
    elif pval1 <=0.01:
        text='**'
        x = (x1[0]+bar_width)/2 #in between two bars
        y = 1.01*max(ymerge[0],ymerge[1])
        props = {'connectionstyle':'bar','arrowstyle':'-','shrinkA':5,'shrinkB':5,'linewidth':2}
        ax.annotate(text,xy=(x,y*1.08),zorder=10,ha='center',fontsize=15) #text annotation
        ax.annotate('',xy=(x1[0],y),xytext=(x1[0]+bar_width,y),arrowprops=props) #annotates line
    elif pval1 <= 0.05:
        text='*'
        x = (x1[0]+bar_width)/2 #in between two bars
        y = 1.01*max(ymerge[0],ymerge[1])
        props = {'connectionstyle':'bar','arrowstyle':'-','shrinkA':5,'shrinkB':5,'linewidth':2}
        ax.annotate(text,xy=(x,y*1.08),zorder=10,ha='center',fontsize=15) #text annotation
        ax.annotate('',xy=(x1[0],y),xytext=(x1[0]+bar_width,y),arrowprops=props) #annotates line
    else:
        text=''
        
    #Significance line for pval2
    if pval2 <= 0.0001:
        text = '****'
        x = (x1[1]+bar_width)/2 #in between two bars
        y = 1.01*max(ymerge[2],ymerge[3])
        props = {'connectionstyle':'bar','arrowstyle':'-','shrinkA':5,'shrinkB':5,'linewidth':2}
        ax.annotate(text,xy=(x1[1]+0.15,y*1.08),zorder=10,ha='center',fontsize=15) #text annotation
        ax.annotate('',xy=(x1[1],y),xytext=(x1[1]+bar_width,y),arrowprops=props) #annotates line
    elif pval2 <= 0.001:
        text='***'
        x = (x1[1]+bar_width)/2 #in between two bars
        y = 1.01*max(ymerge[2],ymerge[3])
        props = {'connectionstyle':'bar','arrowstyle':'-','shrinkA':5,'shrinkB':5,'linewidth':2}
        ax.annotate(text,xy=(x1[1]+0.15,y*1.08),zorder=10,ha='center',fontsize=15) #text annotation
        ax.annotate('',xy=(x1[1],y),xytext=(x1[1]+bar_width,y),arrowprops=props) #annotates line
    elif pval2 <=0.01:
        text='**'
        x = (x1[1]+bar_width)/2 #in between two bars
        y = 1.01*max(ymerge[2],ymerge[3])
        props = {'connectionstyle':'bar','arrowstyle':'-','shrinkA':5,'shrinkB':5,'linewidth':2}
        ax.annotate(text,xy=(x1[1]+0.15,y*1.08),zorder=10,ha='center',fontsize=15) #text annotation
        ax.annotate('',xy=(x1[1],y),xytext=(x1[1]+bar_width,y),arrowprops=props) #annotates line
    elif pval2 <= 0.05:
        text='*'
        x = (x1[1]+bar_width)/2 #in between two bars
        y = 1.01*max(ymerge[2],ymerge[3])
        props = {'connectionstyle':'bar','arrowstyle':'-','shrinkA':5,'shrinkB':5,'linewidth':2}
        ax.annotate(text,xy=(x1[1]+0.15,y*1.08),zorder=10,ha='center',fontsize=15) #text annotation
        ax.annotate('',xy=(x1[1],y),xytext=(x1[1]+bar_width,y),arrowprops=props) #annotates line
    else:
        text=''
    
    #Figure size and export as .png
    fig.set_size_inches(4.3, 5)
    fig.savefig(para+'_'+grp+'_JR.png',dpi=200)