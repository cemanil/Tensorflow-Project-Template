import tensorflow as tf


class BaseModel:
    def __init__(self, config):
        self.config = config

        # Init the global step.
        self._init_global_step()

        # Init the epoch counter.
        self._init_cur_epoch()

    # Save function that saves the checkpoint in the path defined in the config file.
    def save(self, sess):
        print("Saving model...")
        self.saver.save(sess, self.config.checkpoint_dir, self.global_step_tensor)
        print("Model saved")

    # Load latest checkpoint from the experiment path defined in the config file.
    def load(self, sess):
        latest_checkpoint = tf.train.latest_checkpoint(self.config.checkpoint_dir)
        if latest_checkpoint:
            print("Loading model checkpoint {} ...\n".format(latest_checkpoint))
            self.saver.restore(sess, latest_checkpoint)
            print("Model loaded")

    # Just initialize a tensorflow variable to use it as epoch counter.
    def _init_cur_epoch(self):
        with tf.variable_scope('cur_epoch'):
            self.cur_epoch_tensor = tf.Variable(0, trainable=False, name='cur_epoch')
            self.increment_cur_epoch_tensor = tf.assign_add(self.cur_epoch_tensor, 1)

    # Just initialize a tensorflow variable to use it as global step counter.
    def _init_global_step(self):
        # DON'T forget to add the global step tensor to the tensorflow trainer.
        with tf.variable_scope('global_step'):
            self.global_step_tensor = tf.Variable(0, trainable=False, name='global_step')

    def _init_saver(self):
        self.saver = tf.train.Saver(max_to_keep=self.config.max_to_keep)

    def _build_model(self):
        raise NotImplementedError
