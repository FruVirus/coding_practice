"""Clustering with DBSCAN

The problems solved by DBSCAN
-----------------------------

If clusters are nested close together, a relatively standard clustering method, like
k-means clustering, might have difficulty identifying the clusters. In addition, high
dimensional data is often non-linear and we need a clustering algorithm that can cluster
high dimensional data points and not be sensitive to outliers.

One of these algorithms is called Density-Based Spatial Clustering of Applications with
Noise (DBSCAN).

DBSCAN uses the densities of points to cluster them. Intuitively, high-density points
should form a cluster and low-density points should be outliers.

How DBSCAN works
----------------

Starting with the raw unclustered data, the first thing we can do is to count the first
thing we can do is count the number of points close to each point. We do this by drawing
a circle around a given point and counting how many other points are within the circle.
The radius of the circle is a hyperparameter of DBSCAN.

We define a Core Point to be one that is close to at least N other points. The number of
close points for a Core Point is also a hyperparameter of DBSCAN.

After defining all the Core Points, we randomly pick a Core Point and assign it to the
first cluster.

Next, the Core Points that are close to the first cluster (i.e., they are within the
circle of the first cluster) are all added to the first cluster.

Then, the Core Points that are close to the growing first cluster join it and extend it
to other Core Points that are close by.

Ultimately, all of the Core Points that are close to the growing first cluster are added
to it and then used to extend it further.

At this point, every single point in the first cluster is a Core Point and because we
can no longer add any more Core Points to the first cluster, we next add all of the
Non-Core Points that are close (defined by the circle radius) to Core Points in the
first cluster. Unlike Core Points, Non-Core Points can only join a cluster---they cannot
extend the cluster further. In other words, a Non-Core Point has to be close to a Core
Point in order to join a cluster. A Non-Core Point close to a Non-Core Point that is
close to a Core Point will NOT join the cluster.

After this process is completed, we are done forming the first cluster. We then pick a
different random Core Point (that is not one of the Core Points in the just formed
cluster) and start the process again until there are no more non-clustered Core Points.

Any remaining Non-Core Points that are not close to any clusters are considered
outliers.

How DBSCAN deals with ties
--------------------------

Clusters are created sequentially. That means if we had a Non-Core Point close to two
clusters, then it will get assigned to the first cluster that is being built and it will
NOT be added to the next cluster being built.
"""
