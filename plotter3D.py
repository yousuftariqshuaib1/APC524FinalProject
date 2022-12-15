
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib.colors import Normalize
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib

def vector_3D_plotter(state: np.array):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    colors = np.array([0, 0.5, 1])
    norm = Normalize()
    norm.autoscale(colors)
    
    x = np.array([state[3], state[3], state[3]])
    y = np.array([state[4], state[4], state[4]])
    z = np.array([state[5], state[5], state[5]])
    
    u = np.array([state[0], state[6], state[9]])
    v = np.array([state[1], state[7], state[10]])
    w = np.array([state[2], state[8], state[11]])
    
    colormap = cm.inferno
    
    ax.quiver(x, y, z, u, v, w, color=colormap(norm(colors)), length=4000, normalize=True)
    ax.set_xlim(-5000.0, 5000.0)
    ax.set_ylim(-5000.0, 5000.0)
    ax.set_zlim(0, 15000.0)
    
    plt.savefig('images/vector3DPlot.jpg')
    plt.close(fig)
    
    
