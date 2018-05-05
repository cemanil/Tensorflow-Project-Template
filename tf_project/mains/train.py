import tensorflow as tf

from tf_project.data_loader.data_generator import DataGenerator
from tf_project.models.example_model import ExampleModel
from tf_project.trainers.example_trainer import ExampleTrainer
from tf_project.utils import *


def main():
    # Capture the config path from the run arguments.
    # Then process the json configuration file.
    try:
        args = get_args()
        config = process_config(args.config)
    except Exception as err:
        print("Error encountered: {}".format(err))
        return -1

    # Create the results dir.
    create_dirs([config.results_dir, config.summary_dir, config.checkpoint_dir], override=False)

    # Ensure the reproducibility of the project.
    set_project_seed(config.seed)
    copy_file_to_destination(args.config, config.results_dir)
    save_current_commit_id(config.results_dir)

    # Create tensorflow session.
    sess = tf.Session()

    # Create an instance of the model you want.
    model = ExampleModel(config)

    # Load model if exists.
    if config.load_checkpoint_dir is not None:
        model.load(sess)

    # Create your data generator.
    data = DataGenerator(config)

    # Create tensorboard logger.
    logger = Logger(sess, config)

    # Create trainer and pass all the previous components to it.
    trainer = ExampleTrainer(sess, model, data, config, logger)

    # Here you train your model.
    trainer.train()

    # Close the tensorflow session.
    sess.close()
    # Exit with 0.
    return 0


if __name__ == '__main__':
    exit_status = main()

    exit(exit_status)
