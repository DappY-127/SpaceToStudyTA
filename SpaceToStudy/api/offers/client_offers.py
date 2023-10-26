import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class OffersApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "offers"

    def get_offers(self):
        url = f"{self.url}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def get_offers_by_id(self, offers_id):
        url = f"{self.url}/{offers_id}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Post offer")
    def post_offer(self, data):
        url = f"{self.url}"
        response = requests.post(url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response
