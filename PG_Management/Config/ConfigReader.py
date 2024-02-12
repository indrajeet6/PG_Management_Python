from configparser import ConfigParser
import os

def getConfig(strSection, strOption):
    Config = ConfigParser()
    strCWD = os.path.realpath(os.path.dirname(__file__))
    strConfigFilePath = os.path.join(strCWD,"config.ini")
    Config.read (strConfigFilePath)
    return Config.get(strSection, strOption)
