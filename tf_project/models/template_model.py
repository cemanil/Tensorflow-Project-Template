from tf_project.base.base_model import BaseModel


class TemplateModel(BaseModel):
    def __init__(self, config):
        super(TemplateModel, self).__init__(config)

        self._build_model()
        self._init_saver()

    def _build_model(self):
        # Here you build the tensorflow graph of any model you want and also define the loss.
        raise NotImplementedError

    def _init_saver(self):
        # Here you initialize the tensorflow saver that will be used in saving the checkpoints.
        # self.saver = tf.train.Saver(max_to_keep=self.config.max_to_keep)
        raise NotImplementedError
