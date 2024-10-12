import requests
from pywebio import input, output, start_server


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

        if num_vacancies > 0:
            for i, vacancy in enumerate(vacancies):
                # Extract relevant information from the vacancy object
                vacancy_id = vacancy.get("id")
                vacancy_title = vacancy.get("name")
                vacancy_url = vacancy.get("alternate_url")
                company_name = vacancy.get("employer", {}).get("name")
                output.put_text(f"ID: {vacancy_id}")
                output.put_text(f"Title: {vacancy_title}")
                output.put_text(f"Company: {company_name}")
                output.put_text(f"URL: {vacancy_url}")
                output.put_text("")  # Add an empty line for separation

                if i < num_vacancies - 1:
                    output.put_text("---------")  # Add separation line
        else:
            output.put_text("No vacancies found.")
    else:
        output.put_text(f"Request failed with status code: {response.status_code}")


def search_vacancies():
    keyword = input.input("Enter a keyword to search for vacancies:", type=input.TEXT)
    output.clear()
    output.put_text("Searching for vacancies...")
    get_vacancies(keyword)


if __name__ == '__main__':
    start_server(search_vacancies, port=8080)