import requests

import os

from src.engine import Engine


class SuperJobAPI(Engine):

    def get_request(self, keyword, count_page):
        __API_KEY = os.getenv("SUPER_JOB_API_KEY")
        all_vacancies = []
        params = {
            "keyword": keyword.lower(),
            "page": 0,
            "count": 20
        }
        headers = {
            "Host": "api.superjob.ru",
            "X-Api-App-Id": __API_KEY,
            "Authorization": "Bearer r.000000010000001.example.access_token"
        }
        vacancies = \
            requests.get("https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers).json()["objects"]
        for i in range(count_page):
            params["page"] = i
            all_vacancies.extend(vacancies)

        return all_vacancies

    def get_vacancies(self, keyword, count_page=5):
        all_vacancies = []
        vacancies = self.get_request(keyword.lower(), count_page)
        for vacancy in vacancies:
            all_vacancies.append({
                "name": vacancy["profession"],
                "description": vacancy["work"],
                "company_name": vacancy["firm_name"],
                "salary_from": vacancy["payment_from"] if vacancy["payment_from"] else 0,
                "salary_to": vacancy["payment_to"] if vacancy["payment_to"] else 0,
                "url": vacancy["link"]
            })

        return all_vacancies

    def get_filtered_vacancies(self):
        pass
