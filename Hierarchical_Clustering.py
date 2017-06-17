from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
import glob
import os
import cPickle

with open('root_vectors.p', 'rb') as fp:
  array_1 = cPickle.load(fp)

np.random.seed(4711)  # for repeatability of this tutorial
##a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100,])
##b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50,])
##X = np.concatenate((a, b),)
p = np.array([array_1[0], array_1[1],array_1[2],array_1[3],array_1[4]])

print (array_1[8])
X = p

Z = linkage(X, 'complete', metric='cosine')

plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
    labels =["organism","plant","animal","mammal","fish"],
)
plt.show()
