import yaml

with open('greek.yaml') as file:
    greek = yaml.safe_load(file)

print(greek)
