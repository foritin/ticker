import configparser
import os
import box

config_dir = os.path.dirname(os.path.dirname(__file__))
default_config_file = 'base.ini'


class Config:

    def __init__(self):
        self.CONFIG = None

    def load_config(self, config_file=default_config_file):
        config_path = os.path.join(config_dir, 'config', config_file)
        base_loader = configparser.ConfigParser()
        base_loader.read(config_path)
        self.CONFIG = box.Box()
        for one in base_loader.sections():
            setattr(self.CONFIG, one, dict(base_loader[one]))


if __name__ == '__main__':
    instance = Config()
    instance.load_config()