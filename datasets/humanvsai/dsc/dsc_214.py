import numpy as np
from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import Vectors
from tensorflow.keras.datasets import mnist

def get_mnist(sc, data_type="train", location="/tmp/mnist"):
    """Download or load MNIST dataset to/from the specified path.
    Normalize and transform input data into an RDD of Sample"""

    # Load MNIST data
    (x_train, y_train), (x_test, y_test) = mnist.load_data(location)

    # Select train or test data
    if data_type == "train":
        data = x_train
        labels = y_train
    else:
        data = x_test
        labels = y_test

    # Flatten the images and normalize pixel values
    data = data.reshape((data.shape[0], -1)).astype('float32') / 255

    # Convert to RDD of Sample
    samples = [LabeledPoint(label, Vectors.dense(data[i])) for i, label in enumerate(labels)]
    rdd = sc.parallelize(samples)

    return rdd