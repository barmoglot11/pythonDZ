import random

import requests
import sqlite3
import statistics


def get_vacancies(keyword, count):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": keyword,
        "area": 1249,
        "per_page": count,
    }
    headers = {
        "HH-User-Agent": "Your User Agent",  # Replace with your User-Agent header
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])
        num_vacancies = len(vacancies)
        output_vacancy = list()
        output_company = list()
        output_roles = list()
        if num_vacancies > 0:
            for i, vacancy in enumerate(vacancies):
                vacancy_title = vacancy.get("name")
                vacancy_url = vacancy.get("alternate_url")
                company_name = vacancy.get("employer", {}).get("name")
                company_id = vacancy.get("employer", {}).get("id")
                if vacancy.get("salary") is not None:
                    salary_mi = vacancy.get("salary", {}).get("from")
                    salary_min = salary_mi if salary_mi is not None else 0
                    salary_ma = vacancy.get("salary", {}).get("to")
                    salary_max = salary_ma if salary_ma is not None else 0
                    salary = statistics.mean([salary_max, salary_min])
                else:
                    salary = "Не указана"
                profession_roles = []
                for keys in vacancy.get("professional_roles"):
                    profession_roles.extend(keys.get("name").split(', '))
                output_vacancy.append([vacancy_title, company_name, vacancy_url, salary])
                output_company.append([company_id, company_name])
                output_roles.append(profession_roles)

            return output_vacancy, output_company, output_roles
        else:
            print("No vacancies found.")

    else:
        print(f"Vacances not found. Error:{response.status_code}")
        print(response)


connection = sqlite3.connect('../Interface/vacancies-sqlite.db')

cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS Vacancy 
                    (VacancyID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    Organization TEXT,
                    VacancyName TEXT,
                    VacancyDesc TEXT, 
                    URL TEXT, 
                    SalaryMean TEXT)
                ''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS Organization 
                    (OrganizationID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    Organization TEXT NOT NULL)
                ''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Cluster 
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    Profession TEXT,
                    Association TEXT)
                ''')

association_list = {
    "Программист":["Разработчик ПО",
     "Системный администратор",
     "Тестировщик программного обеспечения",
     "Аналитик данных",
     "Инженер по машинному обучению"],
    "Механик":["Автомеханик",
     "Инженер-электрик",
     "Технический специалист",
     "Ремонтник бытовой техники",
     "Машинист"],
    "Продавец":["Консультант по продажам",
     "Менеджер по работе с клиентами",
     "Кассир",
     "Специалист по торговле",
     "Маркетолог"],
    "Флорист":["Декоратор",
     "Ландшафтный дизайнер",
     "Специалист по цветочным композициям",
     "Садовод",
     "Агроном"],
    "Менеджер":["Проектный менеджер",
     "Операционный менеджер",
     "Маркетинговый менеджер",
     "Менеджер по продажам",
     "HR-менеджер"]
}

for names in association_list:

    data_Vacancy = ("AAA", names, "aaaaaaaaaaa", "hh.ru", random.randint(20, 40) * 1000)
    data_Association = (names, ", ".join(association_list[names]))

    cursor.execute('''
                            INSERT INTO Vacancy(Organization, VacancyName, VacancyDesc, URL, SalaryMean)
                            VALUES (?,?,?,?,?)
                        ''', data_Vacancy)

    cursor.executemany('''
                            INSERT INTO Organization( Organization)
                            VALUES (?)
                        ''', "AAA")

    cursor.execute('''
                            INSERT INTO Cluster(Profession, Association)
                            VALUES (?,?)
                        ''', data_Association)



cursor.execute("SELECT * FROM Vacancy")
items = cursor.fetchall()
for item in items:
    print(item)

print("--------------------")

cursor.execute("SELECT * FROM Cluster")
items = cursor.fetchall()
for item in items:
    print(item)

connection.commit()
connection.close()