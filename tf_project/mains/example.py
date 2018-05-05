import tensorflow as tf

from data_loader.data_generator import DataGenerator
from models.example_model import ExampleModel
from trainers.example_trainer import ExampleTrainer
from utils.config import process_config
from utils.dirs import create_dirs
from utils.logger import Logger
from utils.utils import get_args


def main():
    # Capture the config path from the run arguments.
    # Then process the json configuration file.
    try:
        args = get_args()
        config = process_config(args.config)
    except:
        print("Missing or invalid arguments. ")
        exit(0)

    # Create the experiments dirs.
    create_dirs([config.summary_dir, config.checkpoint_dir])

    # Create tensorflow session.
    sess = tf.Session()

    # Create an instance of the model you want.
    model = ExampleModel(config)

    # Load model if exists.
    model.load(sess)

    # Create your data generator.
    data = DataGenerator(config)

    # Create tensorboard logger.
    logger = Logger(sess, config)

    # Create trainer and pass all the previous components to it.
    trainer = ExampleTrainer(sess, model, data, config, logger)

    # Here you train your model.
    trainer.train()


if __name__ == '__main__':
    main()
