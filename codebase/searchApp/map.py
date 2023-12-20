#%%
from matplotlib import pyplot as plt
import numpy as np

class MAP(object):
    def __init__(self, nrow, ncol, start, goal, obstacles):
        self.nrow = nrow
        self.ncol = ncol
        self.start=start
        self.goal = goal
        self.obstacles=obstacles

    def plot_map(self):
        plt.ion()
        fig = plt.figure(figsize=(8,8))
        self.fig = fig
        ax  = fig.gca()
        ax.grid(True)
        ax.axis([0,self.ncol,0,self.nrow])
        ax.set_xticks(np.arange(0,self.ncol,1))
        ax.set_yticks(np.arange(0,self.nrow,1))
        ax.set_aspect('equal')
        for i in self.obstacles:
            rect = plt.Rectangle(i,1,1, alpha=0.7, facecolor='black')
            ax.add_patch(rect)
        # start
        x,y= self.start
        rect_start = plt.Rectangle((x,y),1,1, alpha=1, facecolor='green')
        ax.add_patch(rect_start)
        ax.text(x+0.35, y+0.2, 'S', fontsize=30)
        #goal
        x,y= self.goal
        rect_goal  = plt.Rectangle((x,y),1,1, alpha=1, facecolor='orange')
        ax.add_patch(rect_goal)
        ax.text(x+0.35, y+0.2, 'G', fontsize=30)####
        # plt.waitforbuttonpress()

        plt.pause(0.0001)
        return fig


    def set_node(self,x,y,state,g=None,h=None,f=None, stop=False):
        ax = self.fig.gca()
        xy = [patch.xy for patch in ax.patches]
        # t = [ax.patches.pop(index) for index, patch in enumerate(ax.patches) if patch.xy == (x,y)]

        ax.add_patch(plt.Rectangle((x,y),1,1, alpha=1, facecolor=state))

        fontsize = 120/self.nrow
        if g is not None:
            ax.text(x+0.7,  y+0.7, '%.1f'%g, fontsize=fontsize/1.5)####
        if f is not None:
            ax.text(x+0.35, y+0.2, '%.1f'%f, fontsize=fontsize)####
        if h is not None:
            ax.text(x+0.1,  y+0.7, '%.1f'%h, fontsize=fontsize/1.5)####

        plt.pause(0.0001)
        # plt.waitforbuttonpress()
        if stop==True:
            plt.waitforbuttonpress()




