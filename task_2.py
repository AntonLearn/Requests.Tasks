import requests
import os

def full_path_of_file(root, name):
    return os.path.join(root, name)

def read_params(full_path, mode, code_type):
    with open(full_path, mode, encoding=code_type) as file:
        set_token = file.readline().rstrip()
        set_name_data_file = file.readline().rstrip()
        return [set_token, set_name_data_file]

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": filename, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, full_path, filename):
        href = (self._get_upload_link(filename)).get("href", "")
        response = requests.put(href, data=open(full_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print(f'Файл {filename} успешно записан на Я.Диск!')


if __name__ == '__main__':
    ROOT_PATH = os.getcwd()
    FILE_NAME_OF_PARAMS = 'params.txt'
    full_path_of_file_of_params = full_path_of_file(ROOT_PATH, FILE_NAME_OF_PARAMS)
    TOKEN, NAME_DATA_FILE = read_params(full_path_of_file_of_params, "r", "utf-8")
    full_path_of_file_of_data = full_path_of_file(ROOT_PATH, NAME_DATA_FILE)
    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk(full_path_of_file_of_data, NAME_DATA_FILE)