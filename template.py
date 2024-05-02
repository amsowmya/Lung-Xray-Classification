import os
from pathlib import Path

list_of_files = [
    "Xray/logger.py",
    "Xray/exception.py",
    "Xray/__init__.py",
    "Xray/cloud_storage/s3_operation.py",
    "Xray/cloud_storage/__init__.py",
    "Xray/components/__init__.py",
    "Xray/components/data_ingestion.py",
    "Xray/components/data_transformation.py",
    "Xray/components/model_training.py",
    "Xray/components/model_evaluation.py",
    "Xray/components/model_pusher.py",
    "Xray/entity/__init__.py",
    "Xray/entity/config_entity.py",
    "Xray/entity/artifact_entity.py",
    "Xray/pipeline/__init__.py",
    "Xray/pipeline/training_pipeline.py",
    "Xray/constant/__init__.py",
    "Xray/constant/training_pipeline/__init__.py",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    ".github/workflows/main.yaml",
    ".github/workflows/ci.yaml",
    "test/unittest/__init__.py",
    "test/integrationtest/__init__.py",
    "bentofile.yaml",
    "experiment/experiment.ipynb",
    "tox.ini",
    "setup.cfg",
    "init_setup.sh"
]

for filename in list_of_files:
    filename = Path(filename)
    filedir, file = os.path.split(filename)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        
    if not os.path.exists(filename) or os.path.getsize(filename)==0:
        with open(filename, 'w'):
            pass 
        print(f"File {filename} created successfully")
    else:
        print(f"File {filename} already exists!!!")
        
        
    