import sys
from US_Visa.exception import USvisaException
from US_Visa.logger import logging
from US_Visa.components.data_ingestion import DataIngestion

from US_Visa.entity.config_entity import DataIngestionConfig
from US_Visa.entity.artifact_entity import DataIngestionArtifact


class TrainingPipeline:
    def __init__(self):
        try:
            self.data_ingestion_config = DataIngestionConfig()
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

    def run_pipeline(self) -> None:
        """
        Run the (current) pipeline: data ingestion stage.
        """
        try:
            logging.info("Pipeline run started.")
            _ = self.start_data_ingestion()
            logging.info("Pipeline run completed.")
        except Exception as e:
            raise USvisaException(e, sys) from e
