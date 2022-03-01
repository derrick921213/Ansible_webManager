import yaml
d1=yaml.load(file,Loader=yaml.FullLoader)
with open('inventory.yml','r') as f:
    data = yaml.load(f)
print(yaml.dump(data))