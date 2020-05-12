"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import random

import alg_cluster


######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2),
            max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    closest = (float('inf'), -1, -1)
    cluster_num = len(cluster_list)
    if cluster_num == 2:
        distance = cluster_list[0].distance(cluster_list[1])
        closest = (distance, 0, 1)
        return closest
    for idx1 in range(cluster_num - 1):
        for idx2 in range(idx1 + 1, cluster_num):
            closest_pair_now = pair_distance(cluster_list, idx1, idx2)
            closest = closest_pair(closest_pair_now, closest)
    return closest


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    cluster_list.sort(key=lambda cluster: cluster.horiz_center())
    cluster_num = len(cluster_list)
    if cluster_num <= 3:
        closest = slow_closest_pair(cluster_list)
    else:
        middle_idx = int(round(cluster_num / 2.0))
        left_clusters = cluster_list[0:middle_idx]
        right_clusters = cluster_list[middle_idx:cluster_num]

        left_closest_pair = fast_closest_pair(left_clusters)
        right_closest_pair = fast_closest_pair(right_clusters)
        right_closest_pair = (right_closest_pair[0],
                              right_closest_pair[1] + middle_idx,
                              right_closest_pair[2] + middle_idx)
        closest = min(left_closest_pair, right_closest_pair)
        mid = (cluster_list[middle_idx - 1].horiz_center() + cluster_list[middle_idx].horiz_center()) / 2

        strip_pair = closest_pair_strip(cluster_list, mid, closest[0])
        closest = strip_pair if strip_pair[0] < closest[0] else closest

    return closest


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.
    """
    strips = set()
    for idx in range(len(cluster_list)):
        if abs(cluster_list[idx].horiz_center() - horiz_center) < half_width:
            strips.add(idx)
    strips_indexes = list(strips)
    strips_indexes.sort(key=lambda inx: cluster_list[inx].vert_center())
    strips_num = len(strips_indexes)
    closest = (float('inf'), -1, -1)
    for cl_idx1 in range(0, strips_num - 1):
        for cl_idx2 in range(cl_idx1 + 1, min(cl_idx1 + 4, strips_num)):
            closest_pair_current = pair_distance(cluster_list, strips_indexes[cl_idx1], strips_indexes[cl_idx2])
            closest = closest_pair(closest_pair_current, closest)
    return closest


def closest_pair(current_closest, potential_closest):
    """
    Helper function to compute the closest pair
    """
    if potential_closest < current_closest:
        closest_res = potential_closest
    elif current_closest[0] == potential_closest[0]:
        arb = random.choice([True, False])
        closest_res = potential_closest if arb else current_closest
    else:
        closest_res = current_closest
    return closest_res


######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    current_num_clusters = len(cluster_list)
    while current_num_clusters > num_clusters:
        pair = fast_closest_pair(cluster_list)
        cluster_list[pair[1]].merge_clusters(cluster_list[pair[2]])
        del cluster_list[pair[2]]
        current_num_clusters = len(cluster_list)
    return cluster_list


######################################################################
# Code for k-means clustering

def nearest_center_for_cluster(k_centers, cluster):
    """
    Helper function that computes Euclidean distance between k_centers and a cluster given
    Input: k_centers is a list of clusters chosen as central and a cluster for determining which center is closer to it

    Output: an id of a closest center
    """

    nearest_clr = -1
    min_dist = float('inf')
    for cntr in range(len(k_centers)):
        vert_dist = cluster.vert_center() - k_centers.get(cntr)[1]
        horiz_dist = cluster.horiz_center() - k_centers.get(cntr)[0]
        current_dist = math.sqrt(vert_dist ** 2 + horiz_dist ** 2)
        if current_dist < min_dist:
            min_dist = current_dist
            nearest_clr = cntr
    return nearest_clr


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
    num_clusters_given = len(cluster_list)
    cluster_list_sorted = sorted(cluster_list, key=lambda cluster: cluster.total_population(), reverse=True)

    k_sets = []
    k_centers = dict()
    for idx in range(num_clusters):
        k_centers.update({idx: (cluster_list_sorted[idx].horiz_center(), cluster_list_sorted[idx].vert_center())})

    for _ in range(num_iterations):
        k_sets = [alg_cluster.Cluster(set(), 0, 0, 0, 0) for _ in range(num_clusters)]
        for idx in range(num_clusters_given):
            nearest_clr = nearest_center_for_cluster(k_centers, cluster_list_sorted[idx])
            k_sets[nearest_clr].merge_clusters(cluster_list_sorted[idx])

        for i_clr in range(num_clusters):
            k_centers.update({i_clr: (k_sets[i_clr].horiz_center(), k_sets[i_clr].vert_center())})
    return k_sets


def gen_random_clusters(num_clusters):
    """
    Creates a list of clusters where each cluster in this list corresponds to one randomly generated point in the square
    with corners (+1, -1)

    Input: Integers number of clusters
    Output: List of clusters whose length is num_clusters
    """
    clusters_list = [alg_cluster.Cluster(set(), random.uniform(1, -1), random.uniform(1, -1), 0, 0)
                     for _ in range(num_clusters)]
    return clusters_list


def compute_distortion(cluster_list, data_table):
    """
    Takes a list of clusters and uses cluster_error to compute its distortion
    """
    return sum([cluster.cluster_error(data_table) for cluster in cluster_list])
