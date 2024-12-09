import os
import sys

from XrayClassification.cloud_storage.s3_ops import S3Operation
from XrayClassification.entity.config_entity import ModelPusherConfig
from XrayClassification.entity.artifacts_entity import ModelPusherArtifact
from XrayClassification.exception.exception import XRayException
from XrayClassification.logger.logger import logging

class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig):
        self.model_pusher_config = model_pusher_config
        self.s3 = S3Operation()        


    def initiate_model_pusher(self) -> ModelPusherArtifact:
        """
        Method Name :   initiate_model_pusher
        Description :   This method initiates model pusher.

        Output      :   Model pusher artifact
        """
        logging.info("Entered initiate_model_pusher method of ModelPusher class.")

        try:
            self.s3.upload_file(
                "model/model.pt",
                "model.pt",
                "xrayclassification",
                remove=False,
            )
            logging.info("Uploaded best model to s3 bucket")
            logging.info("Exited initiate_model_pusher method of ModelPusher class.")

        except Exception as e:
            raise XRayException(e, sys)