import numpy as np
from shapely.geometry import Polygon, Point, LineString

def extract_polygons_and_centers(data):
    # Construye un conjunto de polígonos a partir de los datos de obstáculo
    polygons = []
    centers = []
    for i in range(data.shape[0]):
        north, east, alt, d_north, d_east, d_alt = data[i, :]
        obstacle = [north - d_north, north + d_north, east - d_east, east + d_east]
        corners = [(obstacle[0], obstacle[2]), (obstacle[0], obstacle[3]), (obstacle[1], obstacle[3]), (obstacle[1], obstacle[2])]       
        height = alt + d_alt

        poly = Polygon(corners)
        polygons.append((poly, height))

        c = [north, east]
        centers.append(c)
    return polygons, np.asarray(centers)

def get_samples(data):
    xmin = np.min(data[:, 0] - data[:, 3])
    xmax = np.max(data[:, 0] + data[:, 3])

    ymin = np.min(data[:, 1] - data[:, 4])
    ymax = np.max(data[:, 1] + data[:, 4])

    zmin = 0
    # Limit the z axis for the visualization
    zmax = 10

    print("X")
    print("min = {0}, max = {1}\n".format(xmin, xmax))

    print("Y")
    print("min = {0}, max = {1}\n".format(ymin, ymax))

    print("Z")
    print("min = {0}, max = {1}".format(zmin, zmax))

    num_samples = 1000

    xvals = np.random.uniform(xmin, xmax, num_samples)
    yvals = np.random.uniform(ymin, ymax, num_samples)
    zvals = np.random.uniform(zmin, zmax, num_samples)

    samples = list(zip(xvals, yvals, zvals))
    return samples
