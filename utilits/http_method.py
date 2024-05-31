import requests



class http_metod():
    bearer_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwcm9leGUiLCJpYXQiOjE3MTcxNzU5NDguNzQ5MTc0LCJleHAiOjE3MTcyNjIzNDguNzQ5MTc0LCJyZWZyZXNoX3R0bCI6MTcxNzE5NjEwOCwic3Vic2NyaWJlcklkIjozMzI4LCJwbGF0Zm9ybSI6IkJST1dTRVIiLCJkZXZpY2VJZCI6IjUyOWM0MjM5LTBmMWEtNGRmOS1iY2Q4LWE0YmY4ZDU1NmI4NSIsInBjUmF0aW5nIjoiMTgiLCJwY0VuYWJsZWQiOmZhbHNlLCJsb2dpbiI6Imxlb24ua296bG93c2tpQHByb2V4ZS5wbCIsInBlcm1pc3Npb24iOiJhcHAiLCJzdWJzY3JpYmVyVHlwZSI6Im5vcm1hbCIsImxvZ2luQ29udGV4dCI6InB1cmVvdHQiLCJzdWJzY3JpYmVyUGFyZW50SWQiOjMzMjcsImlzQW5vbnltb3VzIjpmYWxzZX0.CnYAP2zIVzuuYgL3LPdSfAE8p90vLDyYISXP7r6CqPg"
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