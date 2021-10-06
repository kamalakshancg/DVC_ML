import yaml
import os

def read_yaml(path_to_yaml):
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content

def create_dir(dirs):
    for each_dir in dirs:
        os.makedirs(each_dir,exist_ok=True)
        print("directory is created at",each_dir)
    