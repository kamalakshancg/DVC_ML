from src.utils.all_utils import read_yaml,create_dir
import argparse
import pandas as pd
import os

def get_data(config_path):
    config = read_yaml(config_path)

    data_path = config["data_source"]

    train = pd.read_csv(data_path, sep=";")
    print(train.head())
    
    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file = config['artifacts']['raw_local_file']


    raw_local_dir_path = os.path.join(artifacts_dir,raw_local_dir)

    create_dir(dirs=[raw_local_dir_path])

    raw_local_path_file = os.path.join(raw_local_dir_path,raw_local_file)
    
    train.to_csv(raw_local_path_file,sep=";",index=False)
    




#     artifacts:
#   artifacts_dir: artifacts
#   raw_local_dir: raw_local_dir
#   raw_local_file: data.csv



if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)

    

