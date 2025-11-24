import sys
from US_Visa.exception import USvisaException
from US_Visa.logger import logging
from US_Visa.components.data_ingestion import DataIngestion
from US_Visa.entity.config_entity import DataIngestionConfig
from US_Visa.entity.artifact_entity import DataIngestionArtifact
from US_Visa.components.data_validation import DataValidation
from US_Visa.entity.config_entity import DataValidationConfig
from US_Visa.entity.artifact_entity import DataValidationArtifact


class TrainingPipeline:
    def __init__(self):
        try:
            self.data_ingestion_config = DataIngestionConfig()
            self.data_validation_config = DataValidationConfig()
            logging.info("TrainingPipeline initialized with DataIngestionConfig.")
        except Exception as e:
            raise USvisaException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        Start the data ingestion component.
        """
        try:
            logging.info("Entered start_data_ingestion of TrainingPipeline.")
            logging.info("Fetching data from MongoDB (via DataIngestion component).")

            ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            artifact: DataIngestionArtifact = ingestion.initiate_data_ingestion()

            logging.info("Train/Test files prepared by DataIngestion.")
            logging.info("Exiting start_data_ingestion of TrainingPipeline.")
            return artifact
        except Exception as e:
            raise USvisaException(e, sys) from e
        
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data validation component
        """
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config
                                             )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")

            logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )

            return data_validation_artifact

        except Exception as e:
            raise USvisaException(e, sys) from e
            

    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            
        except Exception as e:
            raise USvisaException(e, sys) 
