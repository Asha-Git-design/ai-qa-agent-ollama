import requests
import allure

@allure.title("POST Create User on JSONPlaceholder")
@allure.severity(allure.severity_level.NORMAL)
def test_create_user():
    payload = {
        "name": "Asha Mathew",
        "username": "asha2025",
        "email": "asha@example.com"
    }

    with allure.step("Send POST request to create user"):
        response = requests.post("https://jsonplaceholder.typicode.com/users", json=payload)

    with allure.step("Verify response code is 201 Created"):
        assert response.status_code == 201

    with allure.step("Check if response contains posted name"):
        json_data = response.json()
        assert json_data["name"] == "Asha Mathew"
