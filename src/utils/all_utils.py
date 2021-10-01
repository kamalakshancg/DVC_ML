import yaml
import os

def read_yaml(path_yaml):
    with open(path_yaml) as yaml_file:
        contents = yaml.safe_load(yaml_file)
    
    return contents