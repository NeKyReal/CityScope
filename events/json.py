import json


# чтение json-файла
def json_reader(filename):
    with open(filename, encoding="utf-8") as data:
        events = json.load(data)
    return events


# запись в json-файл
def json_writer(filename, data):
    with open(filename, "w") as outfile:
        json.dump(data, outfile, indent=4)
