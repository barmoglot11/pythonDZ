import random
import sqlite3

import requests
from pywebio import input, output, start_server


connection = sqlite3.connect('./Interface/vacancies-sqlite.db')

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
    "Программист": [
        "Разработчик ПО",
        "Системный администратор",
        "Тестировщик программного обеспечения",
        "Аналитик данных",
        "Инженер по машинному обучению"
    ],
    "Механик": [
        "Автомеханик",
        "Инженер-электрик",
        "Технический специалист",
        "Ремонтник бытовой техники",
        "Машинист"
    ],
    "Продавец": [
        "Консультант по продажам",
        "Менеджер по работе с клиентами",
        "Кассир",
        "Специалист по торговле",
        "Маркетолог"
    ],
    "Флорист": [
        "Декоратор",
        "Ландшафтный дизайнер",
        "Специалист по цветочным композициям",
        "Садовод",
        "Агроном"
    ],
    "Менеджер": [
        "Проектный менеджер",
        "Операционный менеджер",
        "Маркетинговый менеджер",
        "Менеджер по продажам",
        "HR-менеджер"
    ]
}
data_to_insert = []
for names in association_list:
    data_to_insert.append(("AAA", names, "abcabc", "hh.ru", random.randint(30, 45) * 1000))
    cursor.executemany('''
                            INSERT INTO Vacancy(Organization, VacancyName, VacancyDesc, URL, SalaryMean)
                            VALUES (?,?,?,?,?)
                        ''', data_to_insert)
    cursor.execute('''
            INSERT INTO Organization(Organization)
            VALUES (?)
        ''', ("AAA",))

    cursor.execute('''
            INSERT INTO Cluster(Profession, Association)
            VALUES (?,?)
        ''', (names, '<br/>'.join(association_list[names])))



cursor.execute("SELECT * FROM Vacancy")
items = cursor.fetchall()
for item in items:
    print(item)

cursor.execute("SELECT * FROM Organization")
items = cursor.fetchall()
for item in items:
    print(item)

cursor.execute("SELECT * FROM Cluster")
items = cursor.fetchall()
for item in items:
    print(item)
connection.commit()
connection.close()
