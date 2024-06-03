import json
import token

import requests

from utilits.http_method import http_metod
headers = {
    "Content-Type": "application/json",
    "API-Device": "Chrome; 125; Mac OS; 10.15.7; Mac OS; 10.15.7;"  # Замените на правильное значение
}
data = {"os":"Mac OS","osVersion":"10.15.7","maker":"unknown","agent":"Chrome","login":"leonid-955@mail.ru","password":"Testowanie99","uid":"529c4239-0f1a-4df9-bcd8-a4bf8d556b85"}
urk_for_log = "https://api.dev.redcarpet.blueonline.tv/subscriber/login?platform=BROWSER&system=tvonline"
Login_in_system = requests.post(urk_for_log,json=data,headers=headers)
result_from_loging = Login_in_system.json()
token_ = result_from_loging.get("token")


base_url = "https://api.dev.redcarpet.blueonline.tv"
# token_ = input("Enter your token    ")
class users_profile():
    @staticmethod

    def subscriber_details():
        url_path = "/subscriber/details?platform=BROWSER&system=tvonline&language=pl"
        url_get_subscriber_details = base_url + url_path
        result_get = http_metod.get(url_get_subscriber_details,token_)
        print(result_get.text)
        return result_get


    @staticmethod
    def subscriber_products():
        url_path = "/subscriber/products?platform=BROWSER&system=tvonline&language=pl"
        url_get_subscriber_products = base_url + url_path
        result_get = http_metod.get(url_get_subscriber_products, token_)
        print(result_get.text)
        return result_get
    @staticmethod
    def parents_control_enable():
        url_path = "/subscriber/parental/enable?platform=BROWSER&system=tvonline"
        print(f"TOKEN PRZED WLACZENIEM KR")
        url_post_18 = base_url + url_path
        json_for_post = {
            "rating": 18
        }
        result_post = http_metod.post(url_post_18,json_for_post,token_)
        print(result_post.text)
        return result_post



    @staticmethod
    def parents_control_disable(token_):
        url_path = "/subscriber/parental/disable?platform=BROWSER&system=tvonline"
        url_disable = base_url + url_path
        json_for_post = {"pin":"1234"}
        result_post = http_metod.post(url_disable,json_for_post,token_)
        print(result_post.text)
        return result_post
    # delete
    @staticmethod
    def parents_control_enable_sixteen(token_):

        url_path = "/subscriber/parental/enable?platform=BROWSER&system=tvonline"
        url_post_18 = base_url + url_path
        json_for_post = {
            "rating": 16
        }
        result_post = http_metod.post(url_post_18, json_for_post, token_)
        print(result_post.text)
        return result_post







