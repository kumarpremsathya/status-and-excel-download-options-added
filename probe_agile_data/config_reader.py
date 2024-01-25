import configparser
import os

def read_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config
