from src.utils.all_utils import read_yaml
import argparse
import pandas as pd
import os

def get_data(config_path):
    config = read_yaml(config_path)

    data_path = config["data_source"]

    train = pd.read_csv(data_path, sep=";")

    print(train.head())


if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)

    

