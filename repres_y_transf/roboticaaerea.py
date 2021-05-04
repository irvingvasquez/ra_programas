# J.I. Vasquez-Gomez

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def plotPolygons(polygons):
    fig, ax = plt.subplots(1)
    for element in polygons:
        points = element.exterior.coords.xy
        
        points = np.transpose(points)
        polygon_shape = matplotlib.patches.Polygon(points, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(polygon_shape)
        plt.axis("equal")
    plt.show()