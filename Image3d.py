from mpl_toolkits.mplot3d import Axes3D
import io
import PIL
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import matplotlib.pyplot as plt
import matplotlib.lines as mlines

global fig
global ax

def start_3d(outline=None, bgcolor='#283653', cubecolor=(1.0, 1.0, 1.0, 0.0), spinecolor=(1.0, 1.0, 1.0, 0.0)):
    global fig,ax
    plt.rcParams['figure.facecolor'] = bgcolor
    plt.rcParams['axes.facecolor'] = bgcolor
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.grid(False)
    ax.set_aspect('equal')

    # Inner cube colors
    ax.xaxis.set_pane_color(cubecolor)
    ax.yaxis.set_pane_color(cubecolor)
    ax.zaxis.set_pane_color(cubecolor)
    ax.xaxis.line.set_color(spinecolor)
    ax.yaxis.line.set_color(spinecolor)
    ax.zaxis.line.set_color(spinecolor)

    # Hide axes ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

def cuboid_data(o, size=(1,1,1)):
    X = [[[-0.5, 0.5, -0.5], [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5]],
         [[-0.5, -0.5, -0.5], [-0.5, -0.5, 0.5], [0.5, -0, 0.5], [0.5, -0.5, -0.5]],
         [[0.5, -0.5, 0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [0.5, 0.5, 0.5]],
         [[-0.5, -0.5, 0.5], [-0.5, -0.5, -0.5], [-0.5, 0.5, -0.5], [-0.5, 0.5, 0.5]],
         [[-0.5, 0.5, -0.5], [-0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, -0.5]],
         [[-0.5, 0.5, 0.5], [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5]]]

    X = np.array(X).astype(float)
    for i in range(3):
        X[:,:,i] *= size[i]
    X += np.array(o)
    return X

def plot_cube(positions,sizes=None,colors=None, size=(1,1,1), **kwargs):
    if not isinstance(colors,(list,np.ndarray)): colors=["C0"]*len(positions)
    if not isinstance(sizes,(list,np.ndarray)): sizes=[size]*len(positions)
    g = []
    for p,s,c in zip(positions,sizes,colors):
        g.append( cuboid_data(p, size=s) )
    return Poly3DCollection(np.concatenate(g),  
                            facecolors=np.repeat(colors,6, axis=0), **kwargs)

def make_voxels(positions, colors=None, size=(1,1,1), lims_min=(0,0,0), lims_max=(10,10,10)):
    global fig,ax
    if colors == None:
        colors= [[0.27450980392156865, 0.9176470588235294, 0.7411764705882353]] * len(positions)

    pc = plot_cube(positions, colors=colors, size=size) # to outline: edgecolor="k"
    ax.add_collection3d(pc)
    # Graph ranges
    ax.set_xlim([lims_min[0],lims_max[0]])
    ax.set_ylim([lims_min[1],lims_max[1]])
    ax.set_zlim([lims_min[2],lims_max[2]])

def draw_line(start, end, color=(0.38823529411764707, 0.5490196078431373, 0.611764705882353), size=2, style='solid'):
    global ax
    ax.plot([start[0], end[0]], [start[1],end[1]],[start[2],end[2]], color=color, linewidth=size, linestyle=style)


def to_pil():
    global fig
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    return PIL.Image.open(buf)

def example():
    start_3d()
    draw_line( (3,6,9), (1,1,1) )
    make_voxels([[1,1,1]])
    plt.show()
