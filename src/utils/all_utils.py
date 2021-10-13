import yaml
import os
import pickle

def read_yaml(path_to_yaml):
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content

def create_dir(dirs):
    for each_dir in dirs:
        os.makedirs(each_dir,exist_ok=True)
        print("directory is created at",each_dir)
    
def save_data(data,data_path):
    data.to_csv(data_path,index=False)
    print("Data is saved at localtion {0}".format(data_path))

def save_model(file_path,model):
    with open(file_path,"wb") as fptr:
        pickle.dump(model,fptr)
        print("model saved!!!")

    