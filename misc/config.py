from json import *

class Config():
    def __init__(self):
        pass

    @staticmethod
    def get(value):
        return load(open('config.json'))[value]