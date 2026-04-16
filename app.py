from src.my_own_project.logger import logging
from src.my_own_project.exception import CustomException
import sys 
from src.my_own_project.components.data_ingestion import DataIngestion
from src.my_own_project.components.data_ingestion import DataIngestionConfig




if __name__=="__main__":
    logging.info("the execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)