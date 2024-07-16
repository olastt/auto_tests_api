import requests


class UserJoke:
    """Получаем категорию от пользователя"""
    def user_print_category(self):
        category = input("Введите желаемую категорию: ")
        return category

    def get_categories(self):
        """Получаем все категории"""
        url = 'https://api.chucknorris.io/jokes/categories'
        response = requests.get(url)
        categories = response.json()
        print(f'Категории получены, статус код - {response.status_code}')
        return categories

    def check_category_exists(self, category, categories):
        """Проверяем что введенная категория существует в нашем списке категорий"""
        if category in categories:
            print(f'Категория "{category}" найдена.')
            return True
        else:
            print(f'Искомая Вами категория "{category}" не найдена.')
            return False

    def get_random_joke(self, category):
        """Получаем рандомную шутку для введенной категории"""
        url = f'https://api.chucknorris.io/jokes/random?category={category}'
        response = requests.get(url)
        if response.status_code == 200:
            joke = response.json().get('value')
            print(f'Шутка для категории {category}: {joke}')
        else:
            print('Не удалось получить шутку.')


user_joke = UserJoke()
user_category = user_joke.user_print_category()
all_categories = user_joke.get_categories()

"""Здесь проверяем, что если категория существует (вызываем метод где пользователь
 вводит категорию и вызываем все категории - то выполнится следующий блок кода, где вызывается рандомная шутка
 по введенной категории"""
if user_joke.check_category_exists(user_category, all_categories):
    user_joke.get_random_joke(user_category)
