import pytest
import math
from bunch import Bunch
from tf_project.data_loader.data_generator import DataGenerator


def _create_datagenerator_object():
    config = Bunch(dict())
    return config, DataGenerator(config)


def _get_batch_size():
    return 2


def _get_all_input_and_output(data_generator):
    return data_generator.input, data_generator.y


def test_datagenerator_init():
    config, data_generator = _create_datagenerator_object()

    assert data_generator.config == config


def test_datagenerator_num_elements_in_batch():
    config, data_generator = _create_datagenerator_object()

    batch_size = _get_batch_size()

    inputs, outputs = next(data_generator.next_batch(batch_size))

    assert inputs.shape[0] == batch_size
    assert outputs.shape[0] == batch_size


def test_datagenerator_batch_dim():
    config, data_generator = _create_datagenerator_object()

    batch_size = _get_batch_size()
    inputs, outputs = next(data_generator.next_batch(batch_size))

    assert len(inputs.shape) == len(data_generator.input.shape)
    assert len(outputs.shape) == len(data_generator.y.shape)


def test_datagenerator_next_batch_covers_whole_dataset():
    config, data_generator = _create_datagenerator_object()
    batch_size = _get_batch_size()

    inputs, outputs = _get_all_input_and_output(data_generator)
    total_batches = int(math.ceil(len(inputs) / batch_size))

    all_input_set_correct = set(map(tuple, inputs))
    all_input_set = set()
    for batch_num in range(total_batches):
        batch_inputs, batch_output = next(data_generator.next_batch(batch_size))
        all_input_set.update(set(map(tuple, batch_inputs)))

    assert all_input_set == all_input_set_correct


