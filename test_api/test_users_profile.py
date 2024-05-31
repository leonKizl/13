from utilits.Cheking import Status_code
from utilits.api import users_profile
import requests


class Test_response():
    def test_subscr_det(self):
        print("\nGET - subscriber/details")
        result_get = users_profile.subscriber_details()
        Status_code.check_status_code(result_get,200)
        Status_code.check_response_value(result_get,['last_logged_at', 'hide_unavailable_products', 'subscriber_local_active', 'login', 'active', 'tester', 'addresses', 'default_address_hash', 'source', 'representative_name', 'icon', 'profile_name', 'firstname', 'lastname', 'country', 'birthdate', 'email', 'phone_number', 'provider', 'is_registration_email_sent', 'login_token', 'is_pin_required_for_profile_change', 'parental_control_rating', 'id', 'email_approved', 'email_approval_required', 'payment_methods', 'missingAgreements', 'need_complete_registration']
)

class Test_subscr_products():
    def test_subscriber_products(self):
        print("\nGET - subscribers/products")
        result_get = users_profile.subscriber_products()
        Status_code.check_status_code(result_get, 200)
# class Test_subscr_parent_conr():
#     def test_parent_cont_enable(self):
#         print("\nPOST subscriber/parental/enable")
#         result_post = users_profile.parents_control_enable()
#         Status_code.check_status_code(result_post, 200)
#         new_token = result_post.json()
#         newest_token = new_token.get("token")
#         print(newest_token)
# #
        # print("\n POST - PARENTAL CONTROL DISABLE")
        # result_post = users_profile.parents_control_disable(newest_token)
#
