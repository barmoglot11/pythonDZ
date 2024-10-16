import requests
import sqlite3
import statistics


def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": keyword,
        "area": 1,  # Specify the desired area ID (1 is Moscow)
        "per_page": 10,  # Number of vacancies per page
    }
    headers = {
        "User-Agent": "Your User Agent",  # Replace with your User-Agent header
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])
        num_vacancies = len(vacancies)

        output = list()
        if num_vacancies > 0:
            for i, vacancy in enumerate(vacancies):
                vacancy_title = vacancy.get("name")
                vacancy_url = vacancy.get("alternate_url")
                company_name = vacancy.get("employer", {}).get("name")
                salary_min = vacancy.get("salary", {}).get("from")
                salary_m = vacancy.get("salary", {}).get("to")
                salary_max = salary_m if salary_m is not None else 0
                salary = statistics.mean([salary_max, salary_min])
                output.append((vacancy_title, company_name, vacancy_url, salary))

            return output
        else:
            print("No vacancies found.")

    else:
        print(f"Vacances not found. Error:{response.status_code}")


connection = sqlite3.connect('vacances-sqlite.db')

cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS Vacances 
    (vacance_id INTEGER PRIMARY KEY AUTOINCREMENT, vacance_name TEXT,
    company_name TEXT, vacancu_url text, salary_mean INTEGER)
                ''')

vacances = get_vacancies("Флорист")

cursor.executemany('''
                        INSERT INTO Vacances(vacance_name, company_name, vacancu_url, salary_mean)
                        VALUES (?,?,?,?)
                    ''', vacances)

cursor.execute("SELECT * FROM Vacances")
items = cursor.fetchall()

for item in items:
    print(item)

connection.commit()
connection.close()
