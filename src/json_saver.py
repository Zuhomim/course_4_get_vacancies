import json


class JSONSaver:

    def __init__(self, filename):
        self.__filename = filename

    @property
    def filename(self):
        return self.__filename

    def write_json(self, data):
        with open(f"../json/{self.filename}.json", 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
