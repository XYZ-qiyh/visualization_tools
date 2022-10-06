# https://matplotlib.org/stable/gallery/mplot3d/voxels.html#d-voxel-volumetric-plot
import numpy as np
import matplotlib.pyplot as plt


# prepare some coordinates
x, y, z = np.indices((8, 8, 8))

# draw cuboids in the top left and bottom right corners, and a link between
cube = (x < 5) & (y < 5) & (z < 5)

# combine the objects into a single boolean array
voxelarray = cube

# set the colors of each object
colors = np.empty(voxelarray.shape, dtype=object)
colors[cube] = 'cornflowerblue' #lightsteelblue

# and plot everything
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.axis('off')
plt.savefig("cost_volume.png", bbox_inches='tight', pad_inches=0.05, dpi=300)

plt.show()
