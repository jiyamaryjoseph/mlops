import os
from pathlib import Path



list_of_files=[
    
    ".github/workflows/.python tegitkeep",
    "src/__init__.py",
    "src/component/_init__.py",
    "src/component/data_ingestion.py",
    "src/component/data_transformation.py",
    "src/component/model_trainer.py",
    "src/component/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/traning_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirement.txt",
    "requirement.dev",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
    
    
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        # logging.info(f"Creating directory : {filedir} for file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as file:
            pass
            
    
    

