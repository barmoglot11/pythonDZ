import random
import sqlite3

import requests

connection = sqlite3.connect('db/vacancies-sqlite.db')

cursor = connection.cursor()
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
