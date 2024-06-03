import requests

from utilits.logger import Logger


class http_metod():

    cookie = ""


    @staticmethod
    def get(url,token):
        Logger.add_request(url,method="GET")

        result = requests.get(url, headers={'Authorization': f"Bearer {token}"}, cookies=http_metod.cookie)

        Logger.add_response(result)

        return result

    @staticmethod
    def post(url, body, token):
        Logger.add_request(url, method="POST")

        result = requests.post(url, json=body, headers={'Authorization': f"Bearer {token}"}, cookies=http_metod.cookie)

        Logger.add_response(result)

        return result

    @staticmethod
    def put(url, body,token):
        Logger.add_request(url, method="PUT")

        result = requests.put(url, json=body, headers={'Authorization': f"Bearer {token}"}, cookies=http_metod.cookie)

        Logger.add_response(result)

        return result

    @staticmethod
    def delete(url, body,token):
        Logger.add_request(url, method="DELETE")

        result = requests.delete(url, json=body, headers={'Authorization': f"Bearer {token}"}, cookies=http_metod.cookie)

        Logger.add_response(result)

        return result