import sqlite3


def get_vacancy():
    connection = sqlite3.connect('vacances-sqlite.db')

    cursor = connection.cursor()

    cursor.execute("SELECT vacance_name FROM Vacances WHERE salary_mean BETWEEN 100000 AND 150000")
    items = cursor.fetchall()

    for item in items:
        print(item)

    connection.commit()
    connection.close()


get_vacancy()
