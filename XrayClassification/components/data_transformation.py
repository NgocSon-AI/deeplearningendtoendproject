import os
import sys


from typing import Tuple

import joblib
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from torchvision.datasets import ImageFolder

from XrayClassification.entity.config_entity import DataTransformationConfig

from XrayClassification.entity.artifacts_entity import (
    DataIngestionArtifact,
    DataTransformationArtifact,
)

from XrayClassification.exception.exception import XRayException
from XrayClassification.logger.logger import logging


class DataTransformation:
    def __init__(self, data_transformation_config:DataTransformationConfig, data_ingestion_artifact:DataIngestionArtifact):
        self.data_transformation_config = data_transformation_config
        self.data_ingestion_artifact = data_ingestion_artifact
    
    # 
    def transforming_training_data(self)->transforms.Compose:
        try:
            
            logging.info("Entered the transforming_training_data method of Data transformation class")
            
            train_transform: transforms.Compose = transforms.Compose(
                [
                    transforms.Resize(self.data_transformation_config.RESIZE),
                    
                    transforms.CenterCrop(self.data_transformation_config.CENTER_CROP),
                    
                    # Biến đổi màu sắc của hình ảnh theo các thông số được chỉ định, như độ sáng, độ tương phản, độ bão hòa và sắc thái.
                    transforms.ColorJitter(**self.data_transformation_config.color_jitter_transforms),  

                    #Lật ngang hình ảnh một cách ngẫu nhiên.
                    transforms.RandomHorizontalFlip(),
                    
                    transforms.RandomRotation(self.data_transformation_config.RANDOM_ROTATION),

                    transforms.ToTensor(),

                    #  Chuẩn hóa tensor, giúp cải thiện tốc độ và độ chính xác của mô hình
                    transforms.Normalize(**self.data_transformation_config.normalize_transforms),
                ]
            )

            logging.info("Exited the transforming_training_data method of Data transformation class")
            return train_transform
        
        except Exception as e:
            raise XRayException(e, sys)
    
    def transforming_testing_data(self)->transforms.Compose:
        try:
            logging.info("Entered the transforming_training_data method of Data transformation class")
            
            test_transform: transforms.Compose = transforms.Compose(
                [
                    transforms.Resize(self.data_transformation_config.RESIZE),
                    transforms.CenterCrop(self.data_transformation_config.CENTER_CROP),
                    transforms.ToTensor(),
                    transforms.Normalize(**self.data_transformation_config.normalize_transforms),
                ]
            )
            
            logging.info("Exited the transforming_training_data method of Data transformation class")
            return test_transform
        
        except Exception as e:
            raise XRayException(e, sys)
        

    def data_loader(self, train_transform: transforms.Compose, test_transform: transforms.Compose) -> Tuple[DataLoader, DataLoader]:
        try:
            logging.info("Entered the data_loader method of Data transformation class")
            # Load data from artifacts/train
            train_data: Dataset = ImageFolder(
                os.path.join(self.data_ingestion_artifact.train_file_path),
                transform=train_transform,
            )
            # Load data from artifacts/test 
            test_data: Dataset = ImageFolder(
                os.path.join(self.data_ingestion_artifact.test_file_path),
                transform=test_transform,
            )
            logging.info("Create train and test data paths")

            train_loader: DataLoader = DataLoader(
                train_data,
                **self.data_transformation_config.data_loader_params
            )
            test_loader: DataLoader = DataLoader(
                test_data,
                **self.data_transformation_config.data_loader_params
            )

            logging.info("Exited the data_loader method of Data transformation class")

            return train_loader, test_loader
        except Exception as e:
            raise XRayException(e, sys)

    def initiate_data_transformation(self) -> DataIngestionArtifact:
        try:
            logging.info("Entered the initiate_data_transformation method of Data transformation class")
            train_transform:transforms.Compose = self.transforming_training_data()
            test_transform:transforms.Compose = self.transforming_testing_data()

            # Tạo thư mục để lưu trữ
            os.makedirs(self.data_transformation_config.artifact_dir, exist_ok=True)

            # Lưu các biến đổi cho train và test data
            joblib.dump(train_transform, self.data_transformation_config.train_transforms_file)
            joblib.dump(test_transform, self.data_transformation_config.test_transforms_file)

            # Tạo DataLoader
            train_loader, test_loader = self.data_loader(
                train_transform=train_transform,
                test_transform=test_transform
            )
            # Tạo đối tượng DataTransformationArtifact
            data_transformation_artifact: DataTransformationArtifact = DataTransformationArtifact(
                transformed_train_object = train_loader,
                transformed_test_object = test_loader,
                train_transform_file_path = self.data_transformation_config.train_transforms_file,
                test_transform_file_path = self.data_transformation_config.test_transforms_file,
            )
            logging.info("Exited the initiate_data_transformation method of Data transformation class")

            return data_transformation_artifact
        except Exception as e:
            raise XRayException(e, sys)