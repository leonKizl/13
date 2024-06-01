import requests



class http_metod():

    cookie = ""


    @staticmethod
    def get(url,token):

        result = requests.get(url, headers={'Authorization': f"Bearer {token}"}, cookies=http_metod.cookie)

        return result

    @staticmethod
    def post(url, body, token):

        result = requests.post(url, json=body, headers={'Authorization': f"Bearer {token}"}, cookies=http_metod.cookie)

        return result

    @staticmethod
    def put(url, body,token):

        result = requests.put(url, json=body, headers={'Authorization': f"Bearer {token}"}, cookies=http_metod.cookie)

        return result

    @staticmethod
    def delete(url, body,token):

        result = requests.delete(url, json=body, headers={'Authorization': f"Bearer {token}"}, cookies=http_metod.cookie)

        return result