import numpy as np
import matplotlib.pyplot as plt

N = 9


color_shades = ['#01040B','#010A1A','#011129','#011638','#04656E','#8B95A4','#B9BFC8']
colors = ['#61BB46', '#FDB827', '#F5821F', '#E03A3E', '#963D97', '#009DDC']

ind = np.arange(N) # the x locations for the groups
width = 0.2      # the width of the bars

fig, (ax) = plt.subplots(1,1, sharex = True, figsize=(35,5))
#ax = plt.subplot(6, 1, 1)
ax.set_ylim(0,275) # outliers only
#ax2.set_ylim(0,275) # most of the data

ax.spines['bottom'].set_visible(True)
ax.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop='off') # don't put tick labels at the top
ax.xaxis.tick_bottom()
fig.subplots_adjust(hspace=0.1)

# no layers, CPL, CPL mixed
d2jspec_d = (7, 25, 0, 100, 100, 100, 100, 100, 100)
d2jspec = ax.bar(ind, d2jspec_d, width, color=colors[0], edgecolor='w')
#ax2.bar(ind, d2jspec_d, width, color=colors[0], edgecolor='w')

d2junspec_d = (70, 126, 246, 100, 100, 100, 100, 100, 100)
d2junspec = ax.bar(ind+width, d2junspec_d, width, color=colors[1], edgecolor='w', hatch='/')
#ax2.bar(ind+width, d2junspec_d, width, color=colors[1], edgecolor='w', hatch='/')

dartc_d = (103, 162, 2136, 100, 100, 100, 100, 100, 100)
dart_c = ax.bar(ind+2*width, dartc_d, width, color=colors[5], edgecolor='w', hatch='o')
#ax2.bar(ind+2*width, dartc_d, width, color=colors[5], edgecolor='w', hatch='o')

dart_d = (80, 133, 236, 100, 100, 100, 100, 100, 100)
dart = ax.bar(ind+3*width, dart_d, width, color=colors[3], edgecolor='w', hatch='\\')
#ax2.bar(ind+3*width, dart_d, width, color=colors[3], edgecolor='w', hatch='\\')

# add some text for labels, title and axes ticks
ax.set_ylabel('Runtime (ms)')
#ax.set_title('Average rendering runtime per frame')
ax.set_xticks(ind+width+0.25)
ax.set_xticklabels( ('DeltaBlue', 'Havlak', 'Richards', 'Tracer', 'FluidMotion', 'MatrixMul', 'BarnsleyFern', 'DiamondSquare', 'GameOfLife') )
#ax2.set_yticks(ax2.get_yticks()[:-1])
ax.set_yticks(ax.get_yticks()[1:])

ax.legend( (d2jspec[0], d2junspec[0], dart_c[0], dart[0]), ('dart2java (spec.)', 'dart2java (unspec.)', 'dart -c', 'dart') , loc=2)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        if height == 0:
#            ax2.text(rect.get_x()+rect.get_width()/2., height+10, 'n/a',
#                ha='center', va='bottom', rotation='vertical')     
              pass  
        else:
#            ax2.text(rect.get_x()+rect.get_width()/2., height+10, '%d'%int(height),
 #                   ha='center', va='bottom', rotation='vertical')
            ax.text(rect.get_x()+rect.get_width()/2., height+10, '%d'%int(height),
                    ha='center', va='bottom', rotation='vertical')

autolabel(d2jspec)
autolabel(d2junspec)
autolabel(dart_c)
autolabel(dart)

#d = .015 # how big to make the diagonal lines in axes coordinates
# arguments to pass plot, just so we don't keep repeating them
#kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
#ax.plot((-d,+d),(-d,+d), **kwargs)      # top-left diagonal
#ax.plot((1-d,1+d),(-d,+d), **kwargs)    # top-right diagonal

#kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
#ax2.plot((-d,+d),(1-d,1+d), **kwargs)   # bottom-left diagonal
#ax2.plot((1-d,1+d),(1-d,1+d), **kwargs) # bottom-right diagonal


plt.show()