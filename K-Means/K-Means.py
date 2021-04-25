from numpy import where
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# define dataset
X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)

# create scatter plot for samples from each class
for class_value in range(2):
    # get row indexes for samples with this class
    row_ix = where(y == class_value)
    # create scatter of these samples
    fig = plt.scatter(X[row_ix, 0], X[row_ix, 1])
    plt.xlabel("x1")
    plt.ylabel("x2")
# show the plot
pyplot.show()