import json

class Configuration(object):
    def __init__(self, configurationFile):
        _configFile = open(configurationFile)
        _configData = json.load(_configFile)
        _configFile.close()
        self.connectionString = _configData['connectionString']
        self.hourSpan = _configData['hourSpan']
   



