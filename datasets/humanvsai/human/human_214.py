def get_mnist(sc, data_type="train", location="/tmp/mnist"):
    from bigdl.dataset import mnist
    from bigdl.dataset.transformer import normalizer
    (images, labels) = mnist.read_data_sets(location, data_type)
    images = images.reshape((images.shape[0], ) + input_shape)
    images = sc.parallelize(images)
    labels = sc.parallelize(labels + 1)  # Target start from 1 in BigDL
    record = images.zip(labels).map(lambda rec_tuple: (normalizer(rec_tuple[0], mnist.TRAIN_MEAN, mnist.TRAIN_STD),
                                    rec_tuple[1])) \
                               .map(lambda t: Sample.from_ndarray(t[0], t[1]))
    return record