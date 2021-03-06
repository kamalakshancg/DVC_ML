from src.utils.all_utils import read_yaml,save_data,create_dir,save_model
from sklearn.linear_model import LinearRegression,ElasticNet
import argparse
import os
import yaml
import pandas as pd





def train_data(config_path,params_path):

    content = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts_dir = content['artifacts']['artifacts_dir']
    split_data_dir_path = content['artifacts']['split_data_dir']
    train_file = content['artifacts']['train']

    alpha_val = params["model_params"]["ElasticNet"]["alpha"]
    l1_ratio_val= params["model_params"]["ElasticNet"]['l1_ratio']
    random_state_val = params['base']['random_state']


    train_file_path = os.path.join(artifacts_dir,split_data_dir_path,train_file)

    traindf = pd.read_csv(train_file_path,sep=";")
    trainy = traindf["quality"]
    trainx = traindf.drop("quality",axis=1)

    ElasticNet_model = ElasticNet(alpha=alpha_val,l1_ratio=l1_ratio_val,random_state=random_state_val)
    ElasticNet_model.fit(trainx,trainy)
    print("training done!!")

    model_dir_name = content["artifacts"]["model_dir"]
    ElasticNet_model_file = content["artifacts"]["elasticnet_model"]
    model_dir_path =  os.path.join(artifacts_dir,model_dir_name)
    create_dir(dirs=[model_dir_path])

    ElasticNet_model_file_path = os.path.join(model_dir_path,ElasticNet_model_file)

    save_model(ElasticNet_model_file_path,ElasticNet_model)





if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    train_data(config_path=parsed_args.config,params_path =parsed_args.params)