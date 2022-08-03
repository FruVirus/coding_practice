"""Hierarchical Clustering

Hierarchical clustering is often associated with heatmaps. The columns represent
different samples and the rows represent different features. Hierarchical clustering
orders the rows and/or columns based on similarity. This makes it easy to see
correlations in the data. Heatmaps often come with dendrograms.

Conceptually:

1. We figure out which feature is most similar with feature 1

2. Then figure out which feature is most similar to feature 2, etc.

3. Of the different combinations (from steps 1 and 2), we then figure out which two
genes are the most similar and merge them into a cluster.

4. Go back to step 1, but now treat the new cluster as a single feature and repeat.

5. Once we have two clusters, we merge them into a single cluster and we are done.

Hierarchical clustering is usually accompanied by a dendrogram. It indicates both the
similarity and the order that the clusters were formed. The first formed cluster is the
most similar and has the shortest branch. The second formed cluster is the next most
similar and has the second shortest branch.

In steps 1 and 2, we have to define what "most similar" means. The method for
determining similarity is arbitrarily chosen. However, the Euclidean distance (of the
features) is often chosen. Pick a method that gives you more insight into your data.

In step 3, there are also different ways to compare clusters with individual features.
One simple idea is to use the average of the features in the cluster.

Imagine we have 2D data grouped into 2 clusters and a new data point and we want to find
out which cluster the new data point belongs to. We can compare the new data point to:

1. The average of each cluster (centroid)
2. The closest point in each cluster (single-linkage)
3. The further point in each cluster (complete-linkage)
4. etc.

In summary:

1. Clusters are formed based on some notion of "similarity".
2. Once you have a "sub-cluster", you have to decide how it should be compared to other
individual features, sub-clusters, etc.
3. The height of the branches in the dendrogram shows you what is most similar.
"""
