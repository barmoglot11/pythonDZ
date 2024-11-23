import sqlite3


def get_vacancy():
    connection = sqlite3.connect('../Interface/vacances-sqlite.db')

    cursor = connection.cursor()

    cursor.execute("SELECT vacance_name FROM Vacances")
    items = cursor.fetchall()

    for item in items:
        print(item)

    connection.commit()
    connection.close()


get_vacancy()
