import random as rd
import numpy as np
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patch
inside = 0
outside = 0
coords = []
#----Plotting the circle and the rectangle-------
x = np.linspace(0,1,200)
y = np.sqrt((0.5**2)-((x-0.5)**2))+0.5 #Upper half of circle
neg_y = -np.sqrt(0.25-((x-0.5)**2))+0.5 #Lower half of circle
fig,ax=plt.subplots()
ax.plot(x,y,'blue')
ax.plot(x,neg_y,'blue')
rect = patch.Rectangle((0,0),1,1,linewidth=1,fill=False)
ax.add_patch(rect)
ax.axis('equal')
ax.axis('off')
#---------Loop the creates each frame for animation--------
for i in range (1,100):
    x_rand = rd.random()  #Random x coordinate
    y_rand = rd.random()  #Random y coordinate
    if ((x_rand-0.5)**2+(y_rand-0.5)**2<(1/4)):  #If the (x,y) coordinate falls inside the circle
        ax.plot(x_rand, y_rand, 'ro', markersize=1)
        inside=inside+1
    else:
        ax.plot(x_rand, y_rand, 'go', markersize=1)
        outside=outside+1
    pi = 4*(inside/(inside+outside))
    ax.set_title("$\pi$ = "+ str(format(pi,'.7f')))
    plt.savefig("path_to_the_folder/frame"+str(i))
    plt.close()m