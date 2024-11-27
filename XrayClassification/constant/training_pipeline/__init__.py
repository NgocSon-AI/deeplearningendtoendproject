from datetime import datetime
from typing import List

import torch


TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


#################################################################
ARTIFACT_DIR: str= "artifacts"

BUCKET_NAME: str= "xrayclassification"

S3_DATA_FOLDER: str= "data"