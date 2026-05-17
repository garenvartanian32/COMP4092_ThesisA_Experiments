import tensorflow as tf

def prod_aggregation(vars_list):
    return tf.reduce_prod(vars_list)
