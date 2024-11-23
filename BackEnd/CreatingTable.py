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


connection = sqlite3.connect('../Interface/vacances-sqlite.db')

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

for names in profession_name:

    vacancies, company, roles = get_vacancies(profession_name, 10)

    association = ",".join([element for element in roles[0] if element != profession_name])

    cursor.executemany('''
                            INSERT INTO Vacancy(vacance_name, company_name, vacancu_url, salary_mean)
                            VALUES (?,?,?,?)
                        ''', vacancies)

    cursor.executemany('''
                            INSERT INTO Organization(OrganizationID, Organization)
                            VALUES (?,?)
                        ''', company)

    cursor.executemany('''
                            INSERT INTO Vacancy(vacance_name, company_name, vacancu_url, salary_mean)
                            VALUES (?,?,?,?)
                        ''', (profession_name, association))



cursor.execute("SELECT * FROM Vacances")

items = cursor.fetchall()


for item in items:
    print(item)

connection.commit()
connection.close()