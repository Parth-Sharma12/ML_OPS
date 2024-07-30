import os
import sys
# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.append(src_dir)
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.exception import CustomException

from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionconfig:
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path: str = os.path.join("artifacts","test.csv")
    raw_data_path: str = os.path.join("artifacts","raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestionConfig = DataIngestionconfig(); #This variable will hold all the paths.

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion component")
        try:
            data=pd.read_csv('logs/notebook/data/stud.csv')
            logging.info("data read")

            dir_name = os.path.dirname(self.ingestionConfig.train_data_path) #Getting the directory name we need to create
            os.makedirs(dir_name,exist_ok = True) # Creating a directory with dir_name
            logging.info("Directory Created")

            train , test = train_test_split(data,test_size=.30,random_state=101)
            logging.info("Data Splitted")

            data.to_csv(self.ingestionConfig.raw_data_path , index =False,header = True)
            train.to_csv(self.ingestionConfig.train_data_path , index =False,header = True)
            test.to_csv(self.ingestionConfig.test_data_path , index =False,header = True)
            logging.info("data saved in respective folders")

            return (
                self.ingestionConfig.train_data_path,
                self.ingestionConfig.test_data_path,
                # self.ingestionConfig.raw_data_path
            )

        except Exception as e:
            raise CustomException(e,sys);

        
# if __name__=="__main__":
#     obj=DataIngestion()
#     train_data,test_data=obj.initiate_data_ingestion()

#     data_transformation=DataTransformation()
#     train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

#     modeltrainer=ModelTrainer()
#     print(modeltrainer.initiate_model_trainer(train_arr,test_arr))