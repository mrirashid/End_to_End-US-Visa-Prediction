import os
from datetime import date
DATABASE_NAME="usVisa"
COLLECTION_NAME='US_DATA'
MONGODB_URL_KEY="MONGODB_URL"
PIPELINE_NAME: str='USVISA'
ARTIFACT_DIR: str="artifact"

MODEL_FILE_NAME="model.pkl"
TARGET_COLUMN="case_status"
CURRENT_YEAR=date.today().year
PREPROCESSING_OBJECT_FILE_NAME="preprocessing.pkl"
FILE_NAME: str="usvisa.csv"
TRAIN_FILE_NAME: str="train.csv"
TEST_FILE_NAME: str="test.csv"
SCHEMA_FILE_NAME=os.path.join("config","schema.yaml")
# Backward-compat alias expected by DataValidation
SCHEMA_FILE_PATH = SCHEMA_FILE_NAME


""" Data Ingestion related Constant"""
DATA_INGESTION_COLLECTION_NAME: str="visa_data"
DATA_INGESTION_DIR_NAME: str= "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str="feature_store"
DATA_INGESTION_INGESTED_DIR: str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float=0.2

"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

"""
Data Transformation ralated constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

"""
Model Trainer related constant start with MODEL_TRAINER VAR NAME
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")

"""
Model Evaluation related constant start with MODEL_EVALUATION VAR NAME
"""
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_EVALUATION_BUCKET_NAME: str = "usvisa-model2024"
MODEL_EVALUATION_S3_MODEL_KEY_PATH: str = "model-registry"


MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02

APP_HOST = "0.0.0.0"
APP_PORT = 8080