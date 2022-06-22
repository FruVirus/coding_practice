"""t-SNE

Unlike PCA, t-SNE can be used to do nonlinear dimensionality reduction.

t-SNE is an iterative algorithm so unlike PCA you cannot apply it on another dataset.
PCA uses the global covariance matrix to reduce data. You can use that matrix and apply
it to a new set of data with the same result. That’s helpful when you need to try to
reduce your test data and can reuse the matrix created from the training data. t-SNE is
mostly used to understand high-dimensional data and by projecting it into
low-dimensional space (like 2D or 3D). That makes it extremely useful when dealing with
CNN networks.

Overview of what t-SNE does
---------------------------

t-SNE takes a high dimensional dataset and reduces it to a low-dimensional graph that
retains a lot of the original information.

If we just naively projected the data onto one of the axes, we'd just get a big mess
that doesn't preserve the original clustering.

What t-SNE does is find a way to project data into a low dimensional space so that the
clustering in the high dimensional space is preserved.

Overview of how t-SNE works
---------------------------

We'll start with a 2D scatter plot and then we'll put the points on the number line in
a random order. From here on out, t-SNE moves these points, a little bit at a time,
until it has clustered them.

At each step, a point on the line is attracted to points it is near in the scatter plot,
and repelled by points it is far from.

Step 1: Determine high-dimensional similarities
-----------------------------------------------

Step 1: Determine the "similarity" of all the points in the scatter plot.

First, measure the distance between two points. Then plot that distance on a normal
curve that is centered on the point of interest. Lastly, draw a line from the point to
the curve. The length of that line is the "unscaled similarity". We repeat this process
between all pairs of points.

Using a normal distribution means that distant points have very low similarity values
and close points have high similarity values. Ultimately, we measure the distances
between all of the points and the point of interest, plot them on a normal curve, and
then measure the distances from the points to the curve to get the unscaled similarity
scores with respect to the point of interest.

The next step is to scale the unscaled similarities so that they add up to 1. The width
of the normal curve depends on the density of data near the point of interest. Less
dense regions have wider curves. So if a group of points have twice the density as
another group of points (i.e., their curve is half as wide), then scaling the similarity
scores will make them the same for both clusters.

To scale the similarity scores so they sum to 1:

Score / SUm of all scores = Scaled Score

This would imply that the scaled similarity scores for relatively tight clusters would
be comparable to the scaled similarity scores for relatively loose clusters.

In reality, t-SNE has a "perplexity" parameter equal to the expected density around each
point. Perplexity is basically a target number of neighbors for the point of interest.
The higher the perplexity, the higher the value of variance for the normal distribution.

Because the width of the distribution is based on the density of the surrounding points,
the similarity scores between two given nodes is generally not the same. So t-SNE just
averages the two similarity scores from the two directions.

Ultimately, you end up with a matrix of similarity scores.

Step 2: Determine low-dimensional similarities
----------------------------------------------

Now we randomly project the data onto the number line and calculate similarity scores
for the points on the number line.

Just like in the high dimensional case, this means picking a point, measuring the
distance between the point of interest and all other points, and lastly, drawing a line
from the point to the curve. However, this time, we're using the t-distribution.

Using a t-distribution, we calculate "unscaled" similarity scores for all the points and
then scale them like before.

Like before, we end up with a matrix of similarity scores. However, the matrix in the
low dimensional case is initially just a mess.

Step 3: Move points in low-d
----------------------------

The goal in the low dimensional case is that we want to move points such that its
similarity score row in the low dimensional case looks like its similarity score row in
the high dimensional case.

t-SNE moves the points a little bit at a time, and at each step, it chooses a direction
that makes the two similarity score matrices more similar. It uses small steps and moves
one point at time.

To optimize the distribution in the low dimensional space, t-SNE optimizes the KL
divergence between the high and low dimensional distributions.

Why the t-distribution is used instead of the normal distribution
-----------------------------------------------------------------

Without using the t-distribution, the clusters would all clump up in the middle of the
number line and be harder to differentiate. This is because Gaussians have a short tail
and thus, creates a crowding problem near the tails.
"""
