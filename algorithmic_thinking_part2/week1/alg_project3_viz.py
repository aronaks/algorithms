"""
Example code for creating and visualizing
cluster of county-based cancer risk data

Note that you must download the file
http://www.codeskulptor.org/#alg_clusters_matplotlib.py
to use the matplotlib version of this code
"""

# Flavor of Python - desktop or CodeSkulptor
DESKTOP = True

import math
import urllib

import alg_cluster
import timer2

# conditional imports
if DESKTOP:
    import alg_project3_solution  # desktop project solution
    import alg_clusters_matplotlib
else:
    # import userXX_XXXXXXXX as alg_project3_solution   # CodeSkulptor project solution
    import alg_clusters_simplegui
    import codeskulptor

    codeskulptor.set_timeout(30)

###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib.urlopen(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print("Loaded", len(data_lines), "data points")
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])]
            for tokens in data_tokens]


############################################################
# Code to create sequential clustering
# Create alphabetical clusters for county data

def sequential_clustering(singleton_list, num_clusters):
    """
    Take a data table and create a list of clusters
    by partitioning the table into clusters based on its ordering

    Note that method may return num_clusters or num_clusters + 1 final clusters
    """

    cluster_list = []
    cluster_idx = 0
    total_clusters = len(singleton_list)
    cluster_size = float(total_clusters) / num_clusters

    for cluster_idx in range(len(singleton_list)):
        new_cluster = singleton_list[cluster_idx]
        if math.floor(cluster_idx / cluster_size) != \
                math.floor((cluster_idx - 1) / cluster_size):
            cluster_list.append(new_cluster)
        else:
            cluster_list[-1] = cluster_list[-1].merge_clusters(new_cluster)

    return cluster_list


#####################################################################
# Code to load cancer data, compute a clustering and
# visualize the results


def run_example():
    """
    Load a data table, compute a list of clusters and
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    data_table = load_data_table(DATA_896_URL)

    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    # cluster_list = sequential_clustering(singleton_list, 15)
    # print "Displaying", len(cluster_list), "sequential clusters"

    # question 5
    # cluster_list = alg_project3_solution.hierarchical_clustering(singleton_list, 9)
    # print "Displaying", len(cluster_list), "hierarchical clusters"

    # question 6
    # cluster_list = alg_project3_solution.kmeans_clustering(singleton_list, 9, 5)
    # print "Displaying", len(cluster_list), "k-means clusters"

    # question 7
    # cluster_list = alg_project3_solution.kmeans_clustering(singleton_list, 9, 5)
    # kmeans_result = alg_project3_solution.compute_distortion(cluster_list, data_table)
    # print("Displaying", kmeans_result, "kmeans_result")
    # cluster_list = alg_project3_solution.hierarchical_clustering(singleton_list, 9)
    # hierarchical_result = alg_project3_solution.compute_distortion(cluster_list, data_table)
    # print("Displaying", hierarchical_result, "hierarchical_result")

    # question 10
    kmeans_res = []
    for clusters_number in range(6, 21):
        cluster_list = alg_project3_solution.kmeans_clustering(singleton_list, clusters_number, 5)
        kmeans_res.append([clusters_number, alg_project3_solution.compute_distortion(cluster_list, data_table)])

    hier_res = []
    for clusters_number in range(20, 5, -1):
        cluster_list = alg_project3_solution.hierarchical_clustering(singleton_list, clusters_number)
        hier_res.append([clusters_number, alg_project3_solution.compute_distortion(cluster_list, data_table)])

    hier_res.reverse()
    # draw the clusters using matplotlib or simplegui
    if DESKTOP:
        # alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)
        # alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)  # add cluster centers
        create_separate_plots(kmeans_res, hier_res)
    else:
        alg_clusters_simplegui.PlotClusters(data_table, cluster_list)  # use toggle in GUI to add cluster centers


def compute_running_times():
    clusters_number = []
    # running_times_computed1 = []
    running_times_computed2 = []
    for current_clr_num in range(500, 2000, 500):
        clusters = alg_project3_solution.gen_random_clusters(current_clr_num)
        clusters_number.append(current_clr_num)
        # running_times_computed1.append(timer2.bestof(alg_project3_solution.slow_closest_pair, clusters))
        # running_times_computed2.append(timer2.bestof(alg_project3_solution.fast_closest_pair, clusters))

        # running_times_computed1.append(timer2.bestof(alg_project3_solution.kmeans_clustering, clusters, 5, 2))
        running_times_computed2.append(timer2.bestof(alg_project3_solution.hierarchical_clustering, clusters, 500))

    # alg_clusters_matplotlib.plt.plot(clusters_number, running_times_computed1, label='k-means')
    alg_clusters_matplotlib.plt.plot(clusters_number, running_times_computed2, label='hierarchical')
    alg_clusters_matplotlib.plt.xlabel('the number of initial clusters')
    alg_clusters_matplotlib.plt.ylabel('the running time of the function (s)')
    alg_clusters_matplotlib.plt.legend()
    alg_clusters_matplotlib.plt.show()


def create_separate_plots(kmeans_results, hierarchical_results):
    alg_clusters_matplotlib.plt.plot([r[0] for r in hierarchical_results], [r[1] for r in hierarchical_results],
                                     label='hierarchical')
    alg_clusters_matplotlib.plt.plot([r[0] for r in kmeans_results], [r[1] for r in kmeans_results],
                                     label='kmeans')
    alg_clusters_matplotlib.plt.title('The distortion computed for 896 points')
    alg_clusters_matplotlib.plt.xlabel('the number of output clusters')
    alg_clusters_matplotlib.plt.ylabel('the distortion associated with each output clustering')
    alg_clusters_matplotlib.plt.legend()
    alg_clusters_matplotlib.plt.show()


run_example()
