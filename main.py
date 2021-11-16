import re
import json
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('path_in', help='Get path file input')
parser.add_argument('path_out', help='Get path file output')
args = parser.parse_args()


class validator:

    def __init__(self):
        pass

    def check_email(email: str) -> bool:
        """
                Выполняет проверку корректности адреса электронной почты.
                Если в строке присутствуют пробелы, запятые, двойные точки,
                а также неверно указан домен адреса, то будет возвращено False.

                Parameters
                ----------
                  email : str
                    Строка с проверяемым электронным адресом

                Returns
                -------
                  bool:
                    Булевый результат проверки на корректность
        """
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, email):
            return True
        return False

    def check_height(height: str) -> bool:
        """
                Выполняет проверку корректности роста
                Если значение роста не строковое, состоит из букв, разделено (,), или 1<x<3 то будет ворвращено False

                Параметры
                ---------
                  height : str
                    Параметр для проверки корректности

                Return
                ------
                  bool:
                    Булевый результат на коррестность
        """
        if type(height) != str:
            return False
        if re.findall(',|[a-zA-Z]|[а-яёА-ЯЁ]]', height):
            return False
        if float(height) < 1.00 or float(height) > 2.30:
            return False
        return True

    def check_inn(inn: str) -> bool:
        """
                Выполняет проверку корректности ИНН
                Если ИНН не состоит из последовательности 12 цифр то будет возвращено False

                Параметры
                ---------
                  inn : str
                    Строка для проверки корректности

                Return
                ------
                  bool:
                    Булевый результат на корректность
        """
        if type(inn) != str:
            return False
        if len(inn) == 12:
            return True
        return False

    def check_passport_number(passport_number: int) -> bool:
        """
                Выполняет проверку корректности номера паспорта
                Если серия паспорта не состоит из последовательности 6 цифр то будет возвращено False

                Параметры
                ---------
                passport_number : str
                    Целое число для проверки корректности

                Return
                ------
                    bool:
                    Булевый результат на корректность
        """
        pattern = "\d{6}"
        if re.match(pattern, str(passport_number)):
            return True
        return False

    def check_university(university: str) -> bool:
        """
                Выполняет проверку типа данных параметра
                Если пераметр не имеет тип данных str возвращено False

                Параметры
                ---------
                string:
                    Параметр для проверки типа данных

                Return
                ------
                bool:
                    Булевый результат на корректность
        """
        if type(university) != str:
            return False
        return True

    def check_age(age: int) -> bool:
        """
                Выполняет проверку корректности возроста
                Если значение возроста не типа int или 20<x<90 то будет ворвращено False

                Параметры
                ---------
                  age : int
                    Параметр для проверки корректности

                Return
                ------
                  bool:
                    Булевый результат на коррестность
                """
        if type(age) != int:
            return False
        if age > 90 and age < 20:
            return False
        return True

    def check_political_views(political_views: str) -> bool:
        """
                Выполняет проверку типа данных параметра
                Если пераметр не имеет тип данных str возвращено False

                Параметры
                ---------
                string:
                    Параметр для проверки типа данных

                Return
                ------
                bool:
                    Булевый результат на корректность
        """
        if type(political_views) != str:
            return False
        return True

    def check_worldview(worldview: str) -> bool:
        """
                Выполняет проверку типа данных параметра
                Если пераметр не имеет тип данных str возвращено False

                Параметры
                ---------
                string:
                    Параметр для проверки типа данных

                Return
                ------
                bool:
                    Булевый результат на корректность
        """
        if type(worldview) != str:
            return False
        return True

    def check_address(address: str) -> bool:
        """
                Выполняет проверку корректности адреса
                Если адрес не типа str или указан не в формате "улица пробел номер дома" то возвращено False

                Параметры
                ---------
                address:
                    Параметр для проверки корректности

                Return
                ------
                bool:
                    Булевый результат на корректность
        """
        if type(address) == str:
            pattern = '[а-яА-Я.\s\d-]+\s+[0-9]+$'
            if re.match(pattern, address):
                return True
        return False


data = json.load(open(args.path_in, encoding='windows-1251'))

true_data = list()
email = 0
height = 0
inn = 0
passport_number = 0
university = 0
age = 0
political_views = 0
worldview = 0
address = 0

with tqdm(total=len(data)) as progressbar:
    for person in data:
        temp = True
        if not validator.check_email(person['email']):
            email += 1
            temp = False
        if not validator.check_height(person['height']):
            height += 1
            temp = False
        if not validator.check_inn(person['inn']):
            inn += 1
            temp = False
        if not validator.check_passport_number(person['passport_number']):
            passport_number += 1
            temp = False
        if not validator.check_university(person["university"]):
            university += 1
            temp = False
        if not validator.check_age(person['age']):
            age += 1
            temp = False
        if not validator.check_political_views(person['political_views']):
            political_views += 1
            temp = False
        if not validator.check_worldview(person['worldview']):
            worldview += 1
            temp = False
        if not validator.check_address(person["address"]):
            address += 1
            temp = False
        if temp:
            true_data.append(person)
        progressbar.update(1)

out_put = open(args.path_out, 'w', encoding='utf-8')
beauty_data = json.dumps(true_data, ensure_ascii=False, indent=4)
out_put.write(beauty_data)
out_put.close()

print(f'Число валидных записей: {len(true_data)}')
print(f'Число невалидных записей: {len(data) - len(true_data)}')
print(f'  - Число невалидных адрессов почты:  {email}')
print(f'  - Число невалидных ростовых замеров: {height}')
print(f'  - Число невалидных ИНН: {inn}')
print(f'  - Число невалидных номеров паспорта: {passport_number}')
print(f'  - Число невалидных университетов: {university}')
print(f'  - Число невалидных возрастов:  {age}')
print(f'  - Число невалидных политических взглядов: {political_views}')
print(f'  - Число невалидных мировоззрений: {worldview}')
print(f'  - Число невалидных адрессов: {address}')
