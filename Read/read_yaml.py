import yaml
def read_yaml():
    with open("../Data/data02.yaml",'r',encoding='utf-8') as f:
        data = yaml.load(f)

        return data

