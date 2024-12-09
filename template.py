import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "XrayClassification"

list_of_files = [
    
    #".github/workflows/.gitkeep",
    #"data/.gitkeep",
    
    #"docs/.gitkeep",
    f"{project_name}/__init__.py",
    
    # components
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    
    # configuration 
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/s3_operations.py",

    # constant
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    
    # entity
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/entity/config_entity.py",
    
    # exception
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception.py",
    
    #logger
    f"{project_name}/logger/__init__.py",
    
    #pipeline
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",

    
    #utils
    # f"{project_name}/utils/__init__.py",
    # f"{project_name}/utils/main_utils.py",

    #"template/index.html",
    ".gitignore",
    # "test/unittest/__init__.py",
    # "test/integrationtest/__init__.py",
    #"app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "bentofile.yaml"
]


def create_file(list_files):
    for file_path in list_files:
        file_path = Path(file_path)

        file_dir, file_name = os.path.split(file_path)

        if file_dir != "":
            os.makedirs(file_dir, exist_ok=True)
            logging.info(f"Create directory: {file_dir} for the file {file_name}")

        if (not os.path.exists(file_name)) or (os.path.getsize(file_name)==0):
            with open(file_path, "w") as f:
                logging.info(f"Creating empty file: {file_name}")
            
        else:
            logging.info(f"{file_name} is already created")

if __name__ == '__main__':
    create_file(list_of_files)