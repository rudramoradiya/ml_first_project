from src.my_own_project.logger import logging
from src.my_own_project.exception import CustomException
import sys 
from src.my_own_project.components.data_ingestion import DataIngestion
from src.my_own_project.components.data_ingestion import DataIngestionConfig
from src.my_own_project.components.data_transformation import DataTransformationConfig
from src.my_own_project.components.data_transformation import DataTransformation





if __name__=="__main__":
    logging.info("the execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        # data_tranformation_config=DataTransformationConfig()
        data_tranformation=DataTransformation()
        data_tranformation.initiate_data_transormation(train_data_path,test_data_path)
        


    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)