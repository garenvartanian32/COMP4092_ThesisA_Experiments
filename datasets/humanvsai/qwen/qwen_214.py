def get_mnist(sc, data_type='train', location='/tmp/mnist'):
    from pyspark.mllib.util import MLUtils
    from pyspark.mllib.regression import LabeledPoint
    from pyspark.sql import SparkSession
    import os
    spark = SparkSession(sc)
    if not os.path.exists(location):
        os.makedirs(location)
    if not os.path.exists(os.path.join(location, f'{data_type}.data')):
        import urllib.request
        urllib.request.urlretrieve(f'http://yann.lecun.com/exdb/mnist/{data_type}-images-idx3-ubyte.gz', os.path.join(location, f'{data_type}-images-idx3-ubyte.gz'))
        urllib.request.urlretrieve(f'http://yann.lecun.com/exdb/mnist/{data_type}-labels-idx1-ubyte.gz', os.path.join(location, f'{data_type}-labels-idx1-ubyte.gz'))
    images_path = os.path.join(location, f'{data_type}-images-idx3-ubyte.gz')
    labels_path = os.path.join(location, f'{data_type}-labels-idx1-ubyte.gz')
    images_rdd = spark.sparkContext.binaryFiles(images_path).flatMap(lambda x: x[1].split(b'\x00\x00\x08\x03')[1:])
    labels_rdd = spark.sparkContext.binaryFiles(labels_path).flatMap(lambda x: x[1].split(b'\x00\x00\x08\x01')[1:])

    def parse_mnist(images, labels):
        images = [int.from_bytes(image[i:i + 784], byteorder='big') / 255.0 for i in range(0, len(images), 784)]
        labels = [int.from_bytes(label[i:i + 1], byteorder='big') for i in range(0, len(labels), 1)]
        return [LabeledPoint(label, image) for (label, image) in zip(labels, images)]