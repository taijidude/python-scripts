import yaml
from datetime import datetime

class Entry: 
    def __init__(self, date, text, etype):
        self.date = date
        self.text = text
        self.etype = etype
    def __repr__(self):
        return "(date="+self.date+", text="+self.text+", etype="+self.etype+")"


entry = Entry(datetime.today().strftime('%d-%m-%Y'), '12das ist ein Test','idea')

entry2 = Entry(datetime.today().strftime('%d-%m-%Y'), '34das ist ein Test','idea')

file = open("learn_yaml.yaml", "w")

yaml.dump(entry, file)
yaml.dump(entry2, file)

file.close()

with open("learn_yaml.yaml") as f:
    data_loaded = yaml.load(f, Loader=yaml.Loader)
    print("1234"+str(data_loaded))

# yaml_file = open("learn_yaml.yaml", 'r')
# yaml_content = yaml.load(yaml_file)

# print("Key: Value")
# for key, value in yaml_content.items():
#     print(f"{key}: {value}")

