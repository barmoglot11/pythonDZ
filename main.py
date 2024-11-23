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

profession_name = ["Программист", "Механик", "Продавец", "Флорист", "Менеджер"]
data_to_insert = []
for names in profession_name:
    data_to_insert.append(("AAA", names, "abcabc", "hh.ru", random.randint(30, 45) * 1000))
    cursor.executemany('''
                            INSERT INTO Vacancy(Organization, VacancyName, VacancyDesc, URL, SalaryMean)
                            VALUES (?,?,?,?,?)
                        ''', data_to_insert)




cursor.execute("SELECT * FROM Vacancy")

items = cursor.fetchall()


for item in items:
    print(item)

connection.commit()
connection.close()
