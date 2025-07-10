import requests
import allure

@allure.title("GET User by ID from JSONPlaceholder")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_user():
    with allure.step("Send GET request to fetch user ID 1"):
        response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    with allure.step("Verify status code is 200"):
        assert response.status_code == 200

    with allure.step("Check if user name exists in response"):
        json_data = response.json()
        assert "name" in json_data