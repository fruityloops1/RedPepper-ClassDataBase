from lib import read, write
import yaml
import os

def cleanup():
    for file in os.listdir("Data"):
        data = read("Data/" + file)

        # add missing stuff
        if not 'Args' in data:
            data['Args'] = None
        if not 'Switches' in data:
            data['Switches'] = None
        if not 'RailRequired' in data:
            data['RailRequired'] = False

        dataText = yaml.dump(data)
        write(data, "Data/" + file)

cleanup()