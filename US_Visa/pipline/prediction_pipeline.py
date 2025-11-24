import os
import sys
import glob
import numpy as np
import pandas as pd
from US_Visa.entity.config_entity import USvisaPredictorConfig
from US_Visa.exception import USvisaException
from US_Visa.logger import logging
from US_Visa.utils.main_utils import load_object
from pandas import DataFrame



class USvisaData:
    def __init__(self,
                continent,
                education_of_employee,
                has_job_experience,
                requires_job_training,
                no_of_employees,
                region_of_employment,
                prevailing_wage,
                unit_of_wage,
                full_time_position,
                company_age
                ):
        """
        Usvisa Data constructor
        Input: all features of the trained model for prediction
        """
        try:
            self.continent = continent
            self.education_of_employee = education_of_employee
            self.has_job_experience = has_job_experience
            self.requires_job_training = requires_job_training
            self.no_of_employees = no_of_employees
            self.region_of_employment = region_of_employment
            self.prevailing_wage = prevailing_wage
            self.unit_of_wage = unit_of_wage
            self.full_time_position = full_time_position
            self.company_age = company_age


        except Exception as e:
            raise USvisaException(e, sys) from e
        
    
    def get_usvisa_input_data_frame(self)-> DataFrame:
        """
        This function returns a DataFrame from USvisaData class input
        """
        try:
            
            usvisa_input_dict = self.get_usvisa_data_as_dict()
            return DataFrame(usvisa_input_dict)
        
        except Exception as e:
            raise USvisaException(e, sys) from e


    def get_usvisa_data_as_dict(self):
        """
        This function returns a dictionary from USvisaData class input 
        """
        logging.info("Entered get_usvisa_data_as_dict method as USvisaData class")

        try:
            input_data = {
                "continent": [self.continent],
                "education_of_employee": [self.education_of_employee],
                "has_job_experience": [self.has_job_experience],
                "requires_job_training": [self.requires_job_training],
                "no_of_employees": [self.no_of_employees],
                "region_of_employment": [self.region_of_employment],
                "prevailing_wage": [self.prevailing_wage],
                "unit_of_wage": [self.unit_of_wage],
                "full_time_position": [self.full_time_position],
                "company_age": [self.company_age],
            }

            logging.info("Created usvisa data dict")

            logging.info("Exited get_usvisa_data_as_dict method as USvisaData class")

            return input_data

        except Exception as e:
            raise USvisaException(e, sys) from e
        

    


class USvisaClassifier:
    def __init__(self,prediction_pipeline_config: USvisaPredictorConfig = USvisaPredictorConfig(),) -> None:
        """
        :param prediction_pipeline_config: Configuration for prediction the value
        """
        try:
            # self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise USvisaException(e, sys)

    def predict(self, dataframe) -> str:
        """
        This is the method of USvisaClassifier
        Returns: Prediction in string format
        """
        try:
            logging.info("Entered predict method of USvisaClassifier class")
            
            # Find the most recent model in artifact directory
            import glob
            artifact_dir = "artifact"
            model_paths = glob.glob(os.path.join(artifact_dir, "*", "model_trainer", "trained_model", "model.pkl"))
            
            if not model_paths:
                raise FileNotFoundError("No trained model found in artifact directory")
            
            # Get the most recent model (by directory timestamp)
            latest_model_path = max(model_paths, key=lambda x: os.path.getctime(os.path.dirname(os.path.dirname(os.path.dirname(x)))))
            
            logging.info(f"Loading model from: {latest_model_path}")
            model = load_object(file_path=latest_model_path)
            result = model.predict(dataframe)
            
            return result
        
        except Exception as e:
            raise USvisaException(e, sys)