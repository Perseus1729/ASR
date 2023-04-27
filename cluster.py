import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Assume that `style_tokens` is a matrix where each row represents a style token
# and each column represents a feature dimension

# Perform PCA to reduce the dimensionality of the style token matrix
pca = PCA(n_components=50)  # choose the number of principal components to keep
style_tokens_pca = pca.fit_transform(style_tokens)

# Perform K-means clustering to group similar style tokens together
kmeans = KMeans(n_clusters=10)  # choose the number of clusters to form
kmeans.fit(style_tokens_pca)
cluster_centers = kmeans.cluster_centers_

# `cluster_centers` now contains the representative style tokens for each cluster
