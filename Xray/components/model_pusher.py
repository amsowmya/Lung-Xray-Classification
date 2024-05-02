import sys

from Xray.cloud_storage.s3_ops import S3Operation
from Xray.entity.config_entity import ModelPusherConfig
from Xray.exception import XRayException
from Xray.logger import logging

class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig):
        self.model_pusher_config = model_pusher_config
        self.s3 = S3Operation()
        
    def initiate_model_pusher(self):
        logging.info("Entered initiate_model_pusher method of ModelPusher class")
        try:
            self.s3.upload_file(
                self.model_pusher_config.trained_model_path,
                "model.pt",
                "xraylungimgsbucket",
                remove=False
            )
            logging.info("Uploaded best model to s3 bucket")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")
        except Exception as e:
            raise XRayException(e, sys)
