"""
Clustering Metrics
==================

Evaluating the performance of a clustering algorithm is not as trivial as counting the
number of errors or the precision and recall of a supervised classification algorithm.
In particular any evaluation metric should not take the absolute values of the cluster
labels into account but rather if this clustering define separations of the data similar
to some ground truth set of classes or satisfying some assumption such that members
belong to the same class are more similar than members of different classes according to
some similarity metric.

To measure the distinctness of clusters, common metrics are:

1. Silhouette Coefficient (ground truth labels are not known)
2. Calinski-Harabaz Index (ground truth labels are not known)
3. Davies-Bouldin Index (ground truth labels are not known)
4. Fowlkes-Mallows scores (ground truth labels are known)

Side Note

Convex clustering is one method that can be used to cluster observations. Instead of
directly assigning each observation to a cluster, it assigns each observation to a point
called the “cluster centroid”. Two observations are then said to belong to the same
cluster if they share the same cluster centroid. k-means clustering and hierarchical
clustering are examples of convex clustering.

Silhouette Coefficient
----------------------

To study the separation distance between the clusters formed by the algorithm silhouette
analysis could be used. The distance between the cluster can be calculated by different
types of distance metrics (Euclidean, Manhattan, Minkowski, Hamming). Silhouette score
returns the average silhouette coefficient applied on all the samples.

The Silhouette Coefficient is calculated using the mean intra-cluster distance (a) and
the mean nearest-cluster distance (b) for each sample. The Silhouette Coefficient for a
sample is (b - a) / max(a, b). To clarify, b is the distance between a sample and the
nearest cluster that the sample is not a part of. Note that Silhouette Coefficient is
only defined if number of labels is 2 <= n_labels <= n_samples - 1.

s = (b - a) / max(a, b)

a: The mean distance between a sample and all other points in the same class.
b: The mean distance between a sample and all other points in the next nearest cluster.

The best value is 1 and the worst value is -1. Values near 0 indicate overlapping
clusters. Negative values generally indicate that a sample has been assigned to the
wrong cluster, as a different cluster is more similar. The score is higher when clusters
are dense and well separated, which relates to a standard concept of a cluster.

Advantages

The score is bounded between -1 for incorrect clustering and +1 for highly dense
clustering. Scores around zero indicate overlapping clusters.

The score is higher when clusters are dense and well separated, which relates to a
standard concept of a cluster.

Drawbacks

The Silhouette Coefficient is generally higher for convex clusters than other concepts
of clusters, such as density based clusters like those obtained through DBSCAN.

Calinski-Harabaz Index
----------------------

The index is the ratio of the sum of between-clusters dispersion and of within-cluster
dispersion for all clusters (where dispersion is defined as the sum of distances
squared). The higher the index the better is clustering.

s = tr(B_k) / tr(W_k) * (n_E - k) / (k - 1)

n_E: Number of samples in the dataset
k: Number of clusters
tr(B_k): Trace of the between group dispersion matrix
tr(W_k): Trace of the within-cluster dispersion matrix

Advantages

The score is higher when clusters are dense and well separated, which relates to a
standard concept of a cluster.

The score is fast to compute.

Drawbacks

The Calinski-Harabasz index is generally higher for convex clusters than other concepts
of clusters, such as density based clusters like those obtained through DBSCAN.

Davies-Bouldin Index
--------------------

Davies Bouldin index is based on the principle of within cluster and between cluster
distances. It is commonly used for deciding the number of clusters in which the data
points should be labeled. It is different from the other two as the value of this index
should be small.

This index signifies the average ‘similarity’ between clusters, where the similarity is
a measure that compares the distance between clusters with the size of the clusters
themselves. Zero is the lowest possible score. Values closer to zero indicate a better
partition.

The index is defined as the average similarity between each cluster C_i for
i = 1, ..., k and its most similar one C_j. In the context of this index, similarity is
defined as a measure R_(ij) that trades off:

    - s_i, the average distance between each point of cluster i and the centroid of that
cluster – also know as cluster diameter.
    - d_(ij), the distance between cluster centroids i and j.

A simple choice to construct R_(ij) so that it is nonnegative and symmetric is:

R_(ij) = (s_i + s_j) / d_(ij)

Then the Davies-Bouldin index is defined as:

DB = (1 / k) * sum(max(R_(ij)) i != j) for i = 1 to k

Advantages

The computation of Davies-Bouldin is simpler than that of Silhouette scores.

The index is solely based on quantities and features inherent to the dataset as its
computation only uses point-wise distances.

Drawbacks

The Davies-Boulding index is generally higher for convex clusters than other concepts of
clusters, such as density based clusters like those obtained from DBSCAN.

The usage of centroid distance limits the distance metric to Euclidean space.

Fowlkes-Mallows scores
----------------------

The Fowlkes-Mallows score FMI is defined as the geometric mean of the pairwise precision
and recall:

FMI = TP / sqrt((TP + FP) * (TP + FN))

The score ranges from 0 to 1. A high value indicates a good similarity between two
clusters.

TP = True Positive − number of pair of points belonging to the same clusters in true as
well as predicted labels both.

FP = False Positive − number of pair of points belonging to the same clusters in true
labels but not in the predicted labels.

FN = False Negative − number of pair of points belonging to the same clusters in the
predicted labels but not in the true labels.

Advantages

Random (uniform) label assignments have a FMI score close to 0.0 for any value of
n_clusters and n_samples (which is not the case for raw Mutual Information or the
V-measure for instance).

Upper-bounded at 1: Values close to zero indicate two label assignments that are largely
independent, while values close to one indicate significant agreement. Further, values
of exactly 0 indicate purely independent label assignments and a FMI of exactly 1
indicates that the two label assignments are equal (with or without permutation).

No assumption is made on the cluster structure: can be used to compare clustering
algorithms such as k-means which assumes isotropic blob shapes with results of spectral
clustering algorithms which can find cluster with “folded” shapes.

Drawbacks

Contrary to inertia, FMI-based measures require the knowledge of the ground truth
classes while almost never available in practice or requires manual assignment by human
annotators (as in the supervised learning setting).
"""
