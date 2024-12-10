import sys

from XrayClassification.components.data_ingestion import DataIngestion
from XrayClassification.components.data_transformation import DataTransformation
from XrayClassification.components.model_training import ModelTrainer
from XrayClassification.components.model_evaluation import ModelEvaluation
from XrayClassification.components.model_pusher import ModelPusher

from XrayClassification.entity.config_entity import(
    DataIngestionConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig,
)

from XrayClassification.entity.artifacts_entity import (
    DataIngestionArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact,
    ModelPusherArtifact,
)

from XrayClassification.exception.exception import XRayException
from XrayClassification.logger.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        self.model_evaluation_config = ModelEvaluationConfig()
        self.model_pusher_config = ModelPusherConfig()

################################## START INGESTION ####################################

    def start_data_ingestion(self) -> DataIngestionArtifact:
        
        logging.info("Entered the start_data_ingestion method of Training ")
        
        try:
            
            logging.info("Getting the data")
            
            data_ingestion = DataIngestion(
                data_ingestion_config = self.data_ingestion_config,
            )
            
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            logging.info("Got the train_set and test_set from s3")
            
            logging.info("Excited the start_data_ingestion method of training_pipeline class")

            return data_ingestion_artifact
        
        except Exception as e:
            raise XRayException(e, sys)
        


################### START TRANSFOMATION ####################################

    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataTransformationArtifact:
        
        logging.info("Entered the start_data_transformation method of TrainPipeline class")
        
        try:
            data_transformation = DataTransformation(
                data_ingestion_artifact = data_ingestion_artifact,
                data_transformation_config = self.data_transformation_config,
            )
            data_transformation_artifact = (
                data_transformation.initiate_data_transformation()
            )
            logging.info("Enterd the start_data_transformation method of Training Pipeline class")
            return data_transformation_artifact

        except Exception as e:
            raise XRayException(e, sys)


####################################### START MODEL TRAINER #######################################

    def start_model_trainer(
        self,
        data_transformation_artifact: DataTransformationArtifact
    ) -> ModelTrainerArtifact:
        logging.info("Entered the start_model_trainer method of TrainPipeline class")
        try:
            model_trainer = ModelTrainer(
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_config=self.model_trainer_config
            )

            model_trainer_artifact = model_trainer.initiate_model_trainer()

            logging.info("Exited the start_model_trainer method of TrainPipeline class")
            return model_trainer_artifact
        except Exception as e:
            raise XRayException(e, sys)


##################################### START MODEL EVALUATION ##############################################

    def start_model_evaluation(
        self,
        data_transformation_artifact: DataTransformationArtifact,
        model_trainer_artifact: ModelTrainerArtifact
    ) -> ModelEvaluationArtifact:
        logging.info("Entered the start_model_trainer method of TrainPipeline class")
        try:
            model_evaluation = ModelEvaluation(
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_artifact=model_trainer_artifact,
                model_evaluation_config=self.model_evaluation_config,
            )
            model_evaluation_artifact = model_evaluation.initiate_model_evaluation()

            logging.info("Exited the start_model_trainer method of TrainPipeline class")
            return model_evaluation_artifact
        except Exception as e:
            raise XRayException(e, sys)

########################################## MODEL PUSHER ##################################################

    def start_model_pusher(self) -> ModelPusherArtifact:
        logging.info("Entered the start_model_pusher method of TrainPipeline")
        try:
            model_pusher = ModelPusher(
                model_pusher_config=self.model_pusher_config
            )
            model_pusher_artifact = model_pusher.initiate_model_pusher()

            logging.info("Exited the start_model_pusher method of TrainPipeline")
            return model_pusher_artifact
        except Exception as e:
            raise XRayException(e, sys)



########################################## RUN ##################################################

    def run_pipeline(self) -> None:
        
        logging.info("Entered the run_pipeline method of Training Pipeline class")
        try:
            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()
            data_transformation_artifact: DataTransformationArtifact = self.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact)
            model_trainer_artifact: ModelTrainerArtifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            model_evaluation_artifact: ModelEvaluationArtifact = self.start_model_evaluation(data_transformation_artifact=data_transformation_artifact, model_trainer_artifact=model_trainer_artifact)
            model_pusher_artifact: ModelPusherArtifact = self.start_model_pusher()


            logging.info("Ented the run_pipeline method of Training pipeline class")
            
        except Exception as e:
            raise XRayException(e, sys)

