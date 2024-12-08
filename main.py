import random
import sqlite3

import requests


connection = sqlite3.connect('./Interface/vacancies-sqlite.db')

cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS Organization 
                    (OrganizationID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    OrganizationName TEXT NOT NULL)
                ''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS Cluster 
                    (ClusterID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    ClusterProfession TEXT,
                    Association TEXT)
                ''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS Vacancy 
                    (VacancyID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    OrganizationName TEXT,
                    OrganizationID INT,
                    VacancyName TEXT,
                    VacancyDesc TEXT, 
                    URL TEXT, 
                    Salary TEXT,
                    ClusterID INT,
                    FOREIGN KEY (OrganizationID) REFERENCES Organization (OrganizationID),
                    FOREIGN KEY (ClusterID) REFERENCES Cluster (ClusterID))
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
    organization_name = names[0] * 3
    organization_id = random.randint(1, 5)
    vacancy_name = names
    vacancy_desc = "abcabc"
    url = "hh.ru"
    salary = random.randint(30, 45) * 1000
    cluster_id = random.randint(1, 5)

    cursor.execute('''
                INSERT INTO Organization(OrganizationName)
                VALUES (?)
            ''', (names[0]*3,))

    cursor.execute('''
                INSERT INTO Cluster(ClusterProfession, Association)
                VALUES (?,?)
            ''', (names, ','.join(association_list[names])))

    data_to_insert.append((organization_name, organization_id, vacancy_name, vacancy_desc, url, salary, cluster_id))

    # Вставка всех данных в Vacancy за один раз
    cursor.executemany('''
        INSERT INTO Vacancy(OrganizationName, OrganizationID, VacancyName, VacancyDesc, URL, Salary, ClusterID)
        VALUES (?,?,?,?,?,?,?)
    ''', data_to_insert)




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
