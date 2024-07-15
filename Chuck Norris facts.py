import requests


class TestJokes:
    # Получение категорий

    def get_all_categories(self):
        url = 'https://api.chucknorris.io/jokes/categories'
        response = requests.get(url)
        categories = response.json()
        print(f'Вот все категории - {categories}')

        # Проверка статус кода
        print(f'Статус код ответа - {response.status_code}, категории получены')
        assert response.status_code == 200, 'Черт, категории не получены'

        # Проверка количества категорий
        assert len(categories) == 16, f'Ожидалось 16 категорий, но получено {len(categories)}'
        print('Все 16 категорий получены')
        return categories

    def get_sixteen_jokes(self):
        # Получение по одной шутке для каждой из 16 категорий
        categories = self.get_all_categories()  # Получаем все категории
        jokes = []  # Создаем пустой список для хранения шуток

        for category in categories:  # Проходим по каждой категории
            url = f'https://api.chucknorris.io/jokes/random?category={category}'  # Создаем URL для запроса шутки
            response = requests.get(url)  # Отправляем запрос и получаем ответ
            joke = response.json()  # Преобразуем ответ в JSON (словарь Python)
            print(f'Шутка для категории {category}: {joke["value"]}')  # Выводим шутку на экран

            assert response.status_code == 200, f'Черт, шутка по категории {category} не получена'  # Проверяем статус ответа

            check_category = joke.get('categories')  # Проверяем категорию шутки
            assert check_category == [
                category], f'Ожидалась категория {category}, а получена {check_category}'  # Проверяем, что категория правильная
            jokes.append(joke["value"])  # Добавляем шутку в список
        print('Все шутки получены!')

        return jokes  # Возвращаем список шуток


give_me_joke = TestJokes()
all_jokes = give_me_joke.get_sixteen_jokes()
