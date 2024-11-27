import sys

from XrayClassification.exception.exception import XRayException
from XrayClassification.pipeline.training_pipeline import TrainPipeline

def start_training():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()

    except Exception as e:
        raise XRayException(e, sys)
    
if __name__ == "__main__":
    start_training()