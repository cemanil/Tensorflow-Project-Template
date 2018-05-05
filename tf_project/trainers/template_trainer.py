from tf_project.base.base_train import BaseTrain


class TemplateTrainer(BaseTrain):
    def __init__(self, sess, model, data, config, logger):
        super(TemplateTrainer, self).__init__(sess, model, data, config, logger)

    def train_epoch(self):
        """
        Implement the logic of epoch:
        - Loop on the number of iterations in the config and call the train step.
        - Add any summaries you want using the summary.
        """
        pass

    def train_step(self):
        """
        Implement the logic of the train step:
        - Run the tensorflow session.
        - Return any metrics you need to summarize.
       """
        pass
