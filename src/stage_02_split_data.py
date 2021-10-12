from src.utils.all_utils import read_yaml,save_data,create_dir
from sklearn.model_selection import train_test_split
import argparse
import os
import yaml
import pandas as pd


def split_data(config_path,params_path):
    content=read_yaml(config_path)
    params = read_yaml(params_path)
    
    artifacts_dir = content['artifacts']['artifacts_dir']
    raw_local_dir =  content['artifacts']['raw_local_dir']
    raw_local_file = content['artifacts']['raw_local_file']

    raw_local_dir_path = os.path.join(artifacts_dir,raw_local_dir)

    raw_local_file_path = os.path.join(raw_local_dir_path,raw_local_file)
    print(raw_local_file_path)

    df = pd.read_csv(raw_local_file_path)

    split_ratio = params['base']['test_size']
    random_state =  params['base']['random_state']

    train , test = train_test_split(df,test_size=split_ratio,random_state=random_state)
    
    
    split_data_dir = content['artifacts']['split_data_dir'] 
    train_data_file = content['artifacts']['train']   
    test_data_file = content['artifacts']['test']
    
    split_data_dir_path = os.path.join(artifacts_dir,split_data_dir)
    create_dir(dirs=[split_data_dir_path])

    train_data_file_path = os.path.join(split_data_dir_path,train_data_file)
    save_data(train,train_data_file_path)

    test_data_file_path =  os.path.join(split_data_dir_path,test_data_file)
    save_data(test,test_data_file_path)




if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    split_data(config_path=parsed_args.config,params_path =parsed_args.params)