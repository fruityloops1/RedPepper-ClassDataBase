from lib import read, write
import yaml
import os

def cleanup():
    for file in os.listdir("Data"):
        data = read("Data/" + file)
        dataText = yaml.dump(data)
        write(data, "Data/" + file)

cleanup()