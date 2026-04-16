## here the generic code is written means functionality used at many place

import os
import sys 
from src.my_own_project.exception import CustomException
from src.my_own_project.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

#my sql config
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")


def read_sql_data():
    logging.info("reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection established",mydb)
        df=pd.read_sql_query('Select * from student',mydb)
        print(df.head())

        return df

    except Exception as e:
        raise CustomException(e,sys)
