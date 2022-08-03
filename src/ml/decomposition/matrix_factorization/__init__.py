"""
Matrix Factorization
====================

Matrix factorization is a simple embedding model. Given the feedback matrix A (m x n),
where m is the number of users (or queries) and n is the number of items, the model
learns:

    - A user embedding matrix U (m x d), where row i is the embedding for user i.
    - An item embedding matrix V (n x d), where row j is the embedding for item j.

The embeddings are learned such that the product U * V.T is a good approximation of the
feedback matrix A.

Matrix factorization typically gives a more compact representation than learning the
full matrix. The full matrix has O(n * m) entries, while the embedding matrices U, V
have O((n + m) * d) entries, where the embedding dimension d is typically much smaller
than m and n. As a result, matrix factorization finds latent structure in the data,
assuming that observations lie close to a low-dimensional subspace.
"""
