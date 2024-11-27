import sys

from XrayClassification.components.data_ingestion import DataIngestion


from XrayClassification.entity.artifacts_entity import (
    DataIngestionArtifact,
)
from XrayClassification.entity.config_entity import(
    DataIngestionConfig,

)
from XrayClassification.exception.exception import XRayException
from XrayClassification.logger.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

    
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
        
    def run_pipeline(self) -> None:
        
        logging.info("Entered the run_pipeline method of Training Pipeline class")
        try:
            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()
            logging.info("Ented the run_pipeline method of Training pipeline class")
            
        except Exception as e:
            raise XRayException(e, sys)

