import requests
import pytest

class Test_Swagger:

    def test_create_user(self):
        body = {  "id": 0,"username": "veeresh","firstName": "veeresh","lastName": "yalawar","email": "veereshyalawar3@gmail.com","password": "veeresh","phone": "8867743684","userStatus": 0}
        response = requests.get('https://petstore.swagger.io/v2/user',data=body)
        print(response.text)
        assert response.status_code == 200

    def test_login(self):
        response = requests.get('https://petstore.swagger.io/v2/user/login?username=veeresh&password=veeresh')
        print(response.text)
        assert response.status_code == 200

    def test_logout(self):
        response = requests.get('https://petstore.swagger.io/v2/user/logout')
        print(response.text)
        assert response.status_code == 200

    def test_create_user_with_list(self):

        response = requests.post('https://petstore.swagger.io/v2/user/createWithList')
        print(response.text)
        assert response.status_code == 415

    def test_get_user_by_username(self):
        response = requests.get('https://petstore.swagger.io/v2/user/veeresh')
        print(response.text)
        assert response.status_code == 200

    def test_delete_user(self):
        response = requests.delete('https://petstore.swagger.io/v2/user/veeresh')
        print(response.text)
        assert response.status_code == 200

    def test_update_user(self):
        response = requests.put('https://petstore.swagger.io/v2/user/veeresh1')
        print(response.text)
        assert response.status_code == 200

    def reurn_pet_store_inventory(self):
        response = requests.get('https://petstore.swagger.io/v2/store/inventory')
        print(response.text)
        assert response.status_code == 200


