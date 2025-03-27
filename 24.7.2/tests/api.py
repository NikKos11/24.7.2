import requests

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru"

    def get_api_key(self, email, password):
        """"Метод делает запрос к API сервера и возвращает статус запроса и рузультат в формате
        JSON с уникальным ключом пользователяб наденного по указанным email и паролем"""

        headers = {
            'email': email,
            'password': password
        }
        res =requests.get(self.base_url+'/api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списками найденных питомцев совпадающих с фильтром. На данный момент фильтр может иметь
        любое пустое значение - получить списко всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res =  requests.get(self.base_url+'/api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key, name, animal_type, age, pet_photo):
        """Метод делает запрос к API сервера, возвращает статус запроса и результат в формате JSON
        информацию о новом питомце"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

        res = requests.post(self.base_url+'/api/pets', headers=headers, data=data, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pet_without_photo(self, auth_key, name, animal_type, age):
        """Метод делает запрос к API сервера, возвращает статус запроса и результат в формате JSON
                информацию о новом питомце без изображения питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        res = requests.post(self.base_url+'/api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_photo_of_pet(self, auth_key, pet_id, pet_photo):
        """Метод делает запрос к API сервера, возвращает статус запроса и результат в формате JSON
                        добавляя изображение питомца"""

        headers = {'auth_key': auth_key['key']}

        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

        res = requests.post(self.base_url + '/api/pets/set_photo/{pet_id}', headers=headers, params=pet_id, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def delete_pet(self, auth_key, pet_id):
        """Метод делает запрос к API сервера, возвращает статус запроса, удаляет питомца из
        списка питомцев"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url+'/api/pets/{pet_id}', headers=headers, params=pet_id)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_pet(self, auth_key, pet_id, name, animal_type, age):
        """Метод делает запрос к API сервера, возвращает статус запроса, обновляет информацию
        о питомце и возвращает результат в формате JSON"""

        headers = {'auth_key': auth_key['key']}

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }

        res = requests.put(self.base_url+'/api/pets/{pet_id}', headers=headers, data=data, params=pet_id)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result