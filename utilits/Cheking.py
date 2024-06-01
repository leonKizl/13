import json

from requests import Response


class Status_code():
    @staticmethod
    def check_status_code(response: Response,status_code:int):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Status code is correct - {response.status_code}")
        else:
            print(f"Status code isn't correct - {response.status_code}")

    @staticmethod
    def check_response_value(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print(f" Response includes all tags\n{list(token)}")