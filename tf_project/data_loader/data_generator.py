import numpy as np
from itertools import cycle


class DataGenerator:
    def __init__(self, config):
        self.config = config

        n_samples = 10
        n_features = 2
        n_classes = 1
        self.input = np.random.rand(n_samples, n_features)
        self.y = np.eye(n_classes)[np.random.choice(n_classes, n_samples)]

    def next_batch(self, batch_size):
        num_examples = self.input.shape[0]

        num_steps_per_epoch = int(num_examples // batch_size)
        index_cycler = cycle(list(range(num_steps_per_epoch)))

        while True:
            curr_idx = next(index_cycler)
            batch_start = batch_size * curr_idx
            batch_end = batch_size * (curr_idx + 1)

            yield (self.input[batch_start: batch_end], self.y[batch_start: batch_end])