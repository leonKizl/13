import json
import token

from utilits.http_method import http_metod


base_url = "https://api.dev.redcarpet.blueonline.tv"
token_ = input("Enter your token    ")
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
        new_token = result_post.json()
        newest_token = new_token.get("token")
        print(newest_token)
        return result_post



    @staticmethod
    def parents_control_disable(token_):
        print(f"TOKEN IN DISABLE\n{token_}")
        url_path = "/subscriber/parental/disable?platform=BROWSER&system=tvonline"
        url_disable = base_url + url_path
        json_for_post = {"pin":"1234"}
        result_post = http_metod.post(url_disable,json_for_post,token_)
        print("OSPOWIEDZ\n\n")
        print(result_post.text)


        return result_post


