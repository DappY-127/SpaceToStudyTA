import allure
from jsonschema import validate

from SpaceToStudy.api.users.client import UsersApiClient
from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import BaseAPITestRunner
from tests.utils.value_provider import ValueProvider


class TestAPIUsers(BaseAPITestRunner):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/402",
                     "Create test for api/users find all users")
    def test_find_all_users_unauthorized(self):
        expected_status_code = 401
        expected_code = "UNAUTHORIZED"
        expected_message = "The requested URL requires user authorization."
        client = UsersApiClient(ValueProvider.get_base_api_url())
        response = client.get_users()
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/404",
                     "Create test for api/users Find user by ID ")
    def test_find_user_by_id_unauthorized(self):
        expected_status_code = 401
        expected_code = "UNAUTHORIZED"
        expected_message = "The requested URL requires user authorization."
        user_id = "644f6f1777e2551b87786650"

        client = UsersApiClient(ValueProvider.get_base_api_url())
        response = client.get_users_by_id(user_id)
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
