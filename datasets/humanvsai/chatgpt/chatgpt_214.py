from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import StandardScaler
from pyspark.sql.functions import monotonically_increasing_id
from pyspark.sql import Row
from pyspark import SparkContext

def load_MNIST(path):
    """
    :param path: str, the path that contains the MNIST dataset.
    :return: data: RDD, RDD of Sample objects of normalized and transformed data.
    """
    # Initialize a spark context
    sc = SparkContext.getOrCreate()
    # Load training and test data
    train_file = path+"/train-images-idx3-ubyte"
    label_file = path+"/train-labels-idx1-ubyte"
    test_file = path+"/t10k-images-idx3-ubyte"
    test_label_file = path+"/t10k-labels-idx1-ubyte"
    with open(train_file, "rb") as f:
        train_data = f.read()
    with open(label_file, "rb") as f:
        train_labels = f.read()
    with open(test_file, "rb") as f:
        test_data = f.read()
    with open(test_label_file, "rb") as f:
        test_labels = f.read()
    # Extract relevant information
    _, train_len, rows, cols = map(int, train_data[:16].split())
    train_img = list(map(int, train_data[16:]))
    _, train_label_len = map(int, train_labels[:8].split())
    train_labels = list(map(int, train_labels[8:]))
    test_length, test_len, test_rows, test_cols = map(int, test_data[:16].split())
    test_img = list(map(int, test_data[16:]))
    _, test_label_len = map(int, test_labels[:8].split())
    test_labels = list(map(int, test_labels[8:]))
    # Convert into a Pyspark dataframe
    train_rdd = sc.parallelize(train_img)
    test_rdd = sc.parallelize(test_img)
    num_features = rows*cols
    train_df = train_rdd.map(lambda x: Row(features=Vectors.dense([float(i) for i in x[:num_features]]))).toDF()
    test_df = test_rdd.map(lambda x: Row(features=Vectors.dense([float(i) for i in x[:num_features]]))).toDF()
    # Normalize data
    scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures")
    scalerModel = scaler.fit(train_df)
    train_df = scalerModel.transform(train_df).select("scaledFeatures")
    test_df = scalerModel.transform(test_df).select("scaledFeatures")
    # Add index column
    train_df = train_df.withColumn("index", monotonically_increasing_id())
    test_df = test_df.withColumn("index", monotonically_increasing_id())
    # Add labels to RDD
    train_labels_rdd = sc.parallelize(train_labels).zipWithIndex().map(lambda x: (x[1],x[0]))
    test_labels_rdd = sc.parallelize(test_labels).zipWithIndex().map(lambda x: (x[1],x[0]))
    train_df_labeled = train_df.join(train_labels_rdd, train_df.index == train_labels_rdd[0], how="inner")
    test_df_labeled = test_df.join(test_labels_rdd, test_df.index == test_labels_rdd[0], how="inner")
    # Convert data into labelled Sample objects
    train_data = train_df_labeled.rdd.map(lambda x: Sample(float(x[0][0]), x[1]))
    test_data = test_df_labeled.rdd.map(lambda x: Sample(float(x[0][0]), x[1]))
    data = train_data.union(test_data)
    return data
