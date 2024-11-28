import sys

from XrayClassification.components.data_ingestion import DataIngestion
from XrayClassification.components.data_transformation import DataTransformation
from XrayClassification.components.model_training import ModelTrainer

from XrayClassification.entity.config_entity import(
    DataIngestionConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)

from XrayClassification.entity.artifacts_entity import (
    DataIngestionArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
)

from XrayClassification.exception.exception import XRayException
from XrayClassification.logger.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_trainer_config = ModelTrainerConfig()

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


#################### START MODEL TRAINER ##################################################

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



#################### RUN ##################################################

    def run_pipeline(self) -> None:
        
        logging.info("Entered the run_pipeline method of Training Pipeline class")
        try:
            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()
            data_transformation_artifact: DataTransformationArtifact = self.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact)
            model_trainer_artifact: ModelTrainerArtifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            logging.info("Ented the run_pipeline method of Training pipeline class")
            
        except Exception as e:
            raise XRayException(e, sys)

