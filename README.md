# ClusteringAlgorithms--K-Means_and_Mean-Shift
This repository briefly provides a comparison of two clustering algorithms, i.e. K-Means and Mean Shift, in clustering of 1000 sample data  with 2 features in make_classification dataset imported from scikit-learn library.  

We first describe how to use clustering algorithms in scikit-learn. This includes an example of fitting the model and an example of visualizing the result.
We need to install the library. You can install the scikit-learn library using the pip Python installer, as follows:

$ sudo pip install scikit-learn

Next, we need to confirm that the library is installed and you are using a modern version. We then run the following script to print the library version number:

$ import sklearn

$ print(sklearn.\__version\__)

Running the example, you should see 0.22.1 version number or higher. The K-Means algorithm is implemented via the KMeans class and the main configuration to tune is the \textit{n\_clusters} hyper-parameter set to the estimated number of clusters in the data. The Mean Shift algorithm is implemented via the Mean Shift class and the main configuration to tune is the \textit{bandwidth} hyper-parameter.
