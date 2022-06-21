"""Multidimensional Scaling (MDS) and Pricipal Coordinate Analysis (PCoA)

MDS and PCoA
------------

There are two types of MDS: classical/metric and non-metric. Here, we only talk about
classical MDS. Classical MDS is the exact same thing as PCoA.

MDS and PCoA are very similar to PCA, except that instead of converting correlations
into a 2D graph, they convert distances among the samples into a 2D graph. That is, in
order to do MDS/PCoA, we calculate distances between features in a dataset instead of
correlations.

One very common way to calculate distances between two things is to calculate the
Euclidean distance.

Once we calculate the distance between every pair of features, MDS/PCoA would reduce
them to a 2D graph.

The bad news is that if we used the Euclidean distance, the graph would be identical to
a PCA graph. In other words, clustering based on minimizing the linear distances is the
same as maximizing the linear correlations.

The good news is that there are tons of other ways to measure distances. For example, we
can use the average of the absolute value of the log fold change between features
(i.e., average of abs(log(feature_1 / feature_2)) for all data points).

One could also choose the Manhattan Distance, Hamming Distance, Great Circle Distance,
etc.

In summary,

PCA creates plots based on correlations among samples whereas MDS/PCoA creates plots
based on distances among samples. Then they BOTH use eigen decomposition to get
coordinates for a graph. We also get the percent of variation that each axes accounts
for and loading scores to determine which variables have the largest effect.
"""
