from src.utils.all_utils import read_yaml,create_dir
import argparse
import pandas as pd
import os

def load_data_and_save_data(config_path):
    #reading the yaml file 
    config = read_yaml(config_path)

    data_path = config["data_source"]

    train = pd.read_csv(data_path, sep=";")
    
    #getting the path to create directory to save the data
    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file = config['artifacts']['raw_local_file']

    #creating the path for directory
    raw_local_dir_path = os.path.join(artifacts_dir,raw_local_dir)
    
    #creating the directory
    create_dir(dirs=[raw_local_dir_path])

     #creating the path for file
    raw_local_path_file = os.path.join(raw_local_dir_path,raw_local_file)
    
    #saving the .csv file
    train.to_csv(raw_local_path_file,sep=";",index=False)






if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    load_data_and_save_data(config_path=parsed_args.config)

    

