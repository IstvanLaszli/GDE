import json

class ISystem:

    @staticmethod
    def read_data(path):
        with open(path, 'r') as f:
            return json.load(f)
