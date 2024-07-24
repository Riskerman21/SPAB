import numpy as np
from sklearn.cluster import DBSCAN, MeanShift, OPTICS
import folium
from math import atan2
import reverse_geocode
from shapely.ops import unary_union, nearest_points
from shapely.geometry import Polygon, Point, LineString

coordinates = [
    (16.2835000740, 101.8698031800), (16.3057595130, 102.0267518000),
    (16.0925858420, 101.9078737000), (16.3723083280, 101.9508206800),
    (16.1708215480, 101.9587828500), (16.2380845150, 101.9817485400),
    (16.1755097630, 101.8691837800), (16.4350569340, 101.8679269800),
    (16.2382040590, 101.9013466200), (16.3795487020, 101.7985487800),
    (16.3483161080, 102.1353329800), (16.4376633480, 102.1557415500),
    (16.4203982170, 102.0459664100), (16.4117916770, 102.2016966100),
    (16.4774725560, 102.1249522300), (16.3276348030, 102.0886572300),
    (16.3143956690, 102.1866546500), (16.4311571030, 102.2736379700),
    (16.6902412830, 101.5240781900), (16.6940833780, 101.6240743200),
    (16.4860371970, 101.9120247900), (16.5730212880, 101.9360404300),
    (16.5333189920, 101.9837585900), (16.4810754680, 102.9876854100),
    (16.4930915650, 102.8577077900), (16.5162643660, 102.9305271300),
    (16.4716378730, 102.3475954000), (16.5231902870, 102.0772276300),
    (16.6011448140, 102.0244096200), (16.7674059640, 101.2797594900),
    (16.5503250670, 102.2305711700), (16.5144201200, 102.1394749000),
    (16.4914879590, 102.2709630100), (16.6573483970, 102.0398181800),
    (16.5761746340, 101.9997326900), (16.7014646970, 102.8717754700),
    (16.0040664650, 102.9251853800), (16.5460943470, 102.9543215900),
    (16.6579546320, 102.9104176100), (16.3017732850, 102.8800485900),
    (16.6489046480, 101.9357138600), (16.8188093990, 101.9074823700),
    (16.5381642930, 103.0678589900), (16.5467086520, 103.0915988200),
    (16.5079637560, 103.0174095700), (16.0425691040, 103.2724115200),
    (16.0054539960, 103.3179684600), (16.1200245190, 103.3498285800),
    (15.9972431980, 103.2738603800), (16.2453613300, 103.0713892800),
    (16.2643394350, 103.0566498800), (16.1946504730, 103.1953444600),
    (16.1404106530, 102.9733859900), (16.1790463760, 103.0671609200),
    (16.3143091320, 102.9534251200), (16.4310932150, 103.0034085800),
    (16.4681881820, 103.0535873600), (15.9602445220, 103.2155898100),
    (15.9611098990, 103.2157281600), (15.4066779360, 103.0995692800),
    (16.0200424940, 103.1317256600), (15.9090637010, 103.1901285100),
    (15.9190623800, 103.2502402000), (15.0730461200, 103.2828140800),
    (15.8797257400, 103.1678132100), (15.8246094710, 103.3617116000),
    (15.7642084850, 103.3816223800), (15.7068438780, 103.3498784000),
    (15.8768634800, 103.2406806900), (15.8394673830, 103.2485066900),
    (15.8200438250, 103.2614709300), (15.7073967570, 103.0715796000),
    (16.1274257790, 103.0468838800), (15.9722703700, 103.5150678000),
    (15.6955914610, 103.4324176000)
]

def sort_coordinates(coords):
    """
    Sort coordinates to form a proper polygon.

    Parameters:
    coords (list of lists): List of coordinate pairs [x, y].

    Returns:
    list of lists: Sorted list of coordinate pairs.
    """
    centroid = np.mean(coords, axis=0)
    sorted_coords = sorted(coords, key=lambda coord: atan2(coord[1] - centroid[1], coord[0] - centroid[0]))
    return sorted_coords

def chaikin(coords, iterations=2):
    """
    Smooth coordinates using Chaikin's algorithm.

    Parameters:
    coords (list of lists): List of coordinate pairs [x, y].
    iterations (int): Number of iterations to apply the smoothing algorithm.

    Returns:
    list of lists: Smoothed list of coordinate pairs.
    """
    for _ in range(iterations):
        new_coords = []
        for i in range(len(coords)):
            p0 = coords[i]
            p1 = coords[(i + 1) % len(coords)]
            q = [0.75 * p0[0] + 0.25 * p1[0], 0.75 * p0[1] + 0.25 * p1[1]]
            r = [0.25 * p0[0] + 0.75 * p1[0], 0.25 * p0[1] + 0.75 * p1[1]]
            new_coords.extend([q, r])
        coords = new_coords
    return coords

def get_clusters(coordinates, labels):
    """
    Extract clusters from coordinate data based on cluster labels.

    Parameters:
    coordinates (numpy.ndarray): Array of coordinate pairs [x, y].
    labels (numpy.ndarray): Array of cluster labels corresponding to coordinates.

    Returns:
    list of lists: List of clusters, each cluster being a list of coordinate pairs.
    """
    unique_labels = set(labels)
    clusters = []
    for k in unique_labels:
        if k == -1:
            continue  # Skip noise
        class_member_mask = (labels == k)
        cluster = coordinates[class_member_mask].tolist()
        clusters.append(cluster)
    return clusters

def get_buffered_coordinates(cluster, buffer_ratio=0.1):
    polygon = Polygon(cluster)
    buffered_polygon = polygon.buffer(polygon.length * buffer_ratio)
    return list(buffered_polygon.exterior.coords)

def get_ring_coordinates(cluster, buffer_ratio=0.05):
    polygon = Polygon(cluster)
    buffered_polygon = polygon.buffer(polygon.length * buffer_ratio)
    ring_polygon = buffered_polygon.difference(polygon)
    return list(ring_polygon.exterior.coords)
    
def visualise(coordinates, cluster_type):
    """
    Visualise coordinate data using different clustering algorithms and plot them on a map.

    Parameters:
    coordinates (list of lists): List of coordinate pairs [x, y].
    cluster_type (int): Type of clustering algorithm to use (1: DBSCAN, 2: Mean Shift, 3: OPTICS).
    """
    coordinates = np.array(coordinates)

    if cluster_type == 1:
        dbscan = DBSCAN(eps=0.1, min_samples=3).fit(coordinates)
        dbscan_labels = dbscan.labels_
        clusters = get_clusters(coordinates, dbscan_labels)

    elif cluster_type == 2:
        mean_shift = MeanShift().fit(coordinates)
        mean_shift_labels = mean_shift.labels_
        clusters = get_clusters(coordinates, mean_shift_labels)

    else:
        optics = OPTICS(min_samples=3).fit(coordinates)
        optics_labels = optics.labels_
        clusters = get_clusters(coordinates, optics_labels)

    lat_avg = sum([coord[0] for coord in coordinates])/len(coordinates)
    long_avg = sum([coord[1] for coord in coordinates])/len(coordinates)
    midpoint = (lat_avg, long_avg)

    #smaller zoom start is more zoomed out
    m = folium.Map(location=midpoint, zoom_start=7)

    for cluster in clusters:
        cluster = sort_coordinates(cluster)
        cluster = chaikin(cluster)
        folium.Polygon(cluster, color='red', fill=True, fill_opacity=0.2).add_to(m)
        
        ring_coordinates = get_ring_coordinates(cluster)
        folium.Polygon(ring_coordinates, color='yellow', fill=True, fill_opacity=0.2).add_to(m)

    m.save('map.html')

visualise(coordinates, 3)