import json
import csv
import re


def readJsonFile(filename):
    with open(filename, "r") as rf:
        config_data = json.load(rf)
        return config_data

def writeToCSV(filename, data):
    with open(filename, "w") as wf:
        writer = csv.writer(wf)
        writer.writerows(data)


def contentInclude(content, str):
    if(re.findall(content, str))