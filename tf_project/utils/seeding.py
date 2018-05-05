import numpy as np
import tensorflow as tf
import random


def set_project_seed(seed):
    # Numpy.
    np.random.seed(seed)

    # Tensorflow.
    tf.set_random_seed(seed)

    # Random.
    random.seed(seed)
