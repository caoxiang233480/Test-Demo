import yaml
import os

Path = os.path.dirname(os.path.realpath(__file__))
yamlPath = os.path.join(Path, "test.yaml")

file = open(yamlPath, 'r', encoding="utf-8")

cfg = file.read()

print(type(cfg))  # 读出来是字符串
print(cfg)

d = yaml.load(cfg)  # 用load方法转字典

print(d)

print(type(d))
