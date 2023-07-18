import requests
import json

class Translator():
    def __init__(self):
        print('Translation started')

    def translate(self, text):
        # IAM_TOKEN = 't1.9euelZqQjpOcz8-SmY6SlZPNzo7Oye3rnpWajJvLjM2PkpGanJbIlcyNmsjl8_dmYE5q-e9YCkQ7_d3z9yYPTGr571gKRDv9.GmLil2c77NDlIjWF3irDg0BvJDxXvYhoVrnaeV70yfnXsCGhEV8Q7uj6pkCRtGSsBtOTrr2k1LbMbAQNJ5P3Cg'
        f = open("token.txt", 'r')
        IAM_TOKEN = f.read()
        f.close()
        if IAM_TOKEN[-1] == '\n':
            IAM_TOKEN = IAM_TOKEN[:-1]
        # print(IAM_TOKEN)
        folder_id = 'b1gmeg9v0cp65s78dos1'
        target_language = 'he'
        texts = [text]

        body = {
            "targetLanguageCode": target_language,
            "texts": texts,
            "folderId": folder_id,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(IAM_TOKEN)
        }

        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                 json=body,
                                 headers=headers
                                 )
        try:
            return json.loads(response.text)['translations'][0]['text']
        except BaseException:
            return "Ошибка перевода"