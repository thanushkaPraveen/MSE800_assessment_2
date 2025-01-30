import json


class StringResources:
    _strings = {}

    @classmethod
    def load_strings(cls, json_file):
        try:
            with open(json_file, 'r') as file:
                cls._strings = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {json_file} was not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON.")

    @classmethod
    def get(cls, key, language="en"):
        language_strings = cls._strings.get(language, {})
        return language_strings.get(key, f"Error: '{key}' not found")