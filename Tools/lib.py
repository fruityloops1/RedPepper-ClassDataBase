import yaml

def read(path: str):
    with open(path, "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def write(data, path: str):
    with open(path, "w") as f:
        f.write(yaml.dump(data))