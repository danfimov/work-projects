import json
import unittest

import requests

SUCCESS = 200
INCORRECT = 400
ADDED = 201


class CouriersTest(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(CouriersTest, self).__init__(*a, **kw)
        # тест проходил на локальной машине, поэтому здесь localhost и соответствующий порт
        self.host = '127.0.0.1:5000'
        self.command = 'couriers'
        self.url = 'http://{}/{}'.format(self.host, self.command)

    @staticmethod
    def print_json(response):
        print('\n\n', json.dumps(response.json(), indent=4, sort_keys=True))

    def test_get_couriers(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, SUCCESS, 'Server status test')

    def test_new_courier(self):
        payload = {"data": [
            {"courier_id": 1,
             "courier_type": "foot",
             "regions": [1, 12, 22],
             "working_hours": ["11:35-14:05", "09:00-11:00"]
             }
        ]}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, ADDED, 'Добавление одного курьера (status)')

        correct_answer = {"couriers": [{"id": 1}]}
        self.assertEqual(response.json(), correct_answer, 'Добавление одного курьера (id)')

    def test_new_couriers(self):
        payload = {"data": [
            {"courier_id": 4,
             "courier_type": "foot",
             "regions": [1, 12, 22],
             "working_hours": ["11:35-14:05", "09:00-11:00"]
             },
            {"courier_id": 5,
             "courier_type": "bike",
             "regions": [1, 12, 22],
             "working_hours": ["11:35-14:05", "09:00-11:00"]
             },
            {"courier_id": 6,
             "courier_type": "car",
             "regions": [1, 12, 22],
             "working_hours": ["11:35-14:05", "09:00-11:00"]
             }
        ]}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, ADDED, 'Добавление нескольких курьеров (status)')

        correct_answer = {"couriers": [{"id": 4}, {"id": 5}, {"id": 6}]}
        self.assertEqual(response.json(), correct_answer, 'Добавление нескольких курьеров (status)')

    def test_new_courier_with_error(self):
        payload = {"data": [
            {"courier_id": 404,
             "courier_type": "so many cars",
             "regions": [1, 12, 22],
             "working_hours": ["11:35-14:05", "09:00-11:00"]
             }
        ]}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, INCORRECT,
                         'Добавление проблемного курьера-1 (status)')

        correct_answer = {
            "validation_error": {
                "couriers": [{"id": 404}]
            }
        }
        self.assertEqual(response.json(), correct_answer, 'Добавление проблемного курьера-1 (id)')

        payload = {"data": [
            {"courier_id": 404,
             "courier_type": "foot",
             "regions": [1, '12', 22],
             "working_hours": ["11:35-14:05", "09:00-11:00"]
             }
        ]}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, INCORRECT,
                         'Добавление проблемного курьера-1 (status)')
        self.assertEqual(response.json(), correct_answer, 'Добавление проблемного курьера-2 (id)')

        payload = {"data": [
            {"courier_id": 404,
             "courier_type": "foot",
             "regions": [1, 12, 22],
             "working_hours": ["11:35-14:0S", "09:00-11:O0"]
             }
        ]}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, INCORRECT,
                         'Добавление проблемного курьера-3 (status)')
        self.assertEqual(response.json(), correct_answer, 'Добавление проблемного курьера-3 (id)')

    def test_new_couriers_with_errors(self):
        payload = {"data": [
            {"courier_id": 404,
             "courier_type": "so many cars",
             "regions": [1, 12, 22],
             "working_hours": ["11:35-14:05", "09:00-11:00"]
             },
            {"courier_id": 405,
             "courier_type": "car",
             "regions": [1, 12, 22],
             "working_hours": ["11:35-14:05", "09:00-11:00"]
             },
            {"courier_id": 406,
             "courier_type": "bike",
             "regions": [1, 12, 22],
             "working_hours": ["11:35-14:05", "09:00-11:00"]
             }
        ]}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, INCORRECT,
                         'Добавление проблемных курьеров-1 (status)')

        correct_answer = {
            "validation_error": {
                "couriers": [{"id": 404}]
            }
        }
        self.assertEqual(response.json(), correct_answer, 'Добавление проблемных курьеров-1 (id)')

        payload = {"data": [
            {"courier_id": 404,
             "courier_type": "so many cars",
             "regions": [1, 12, 22],
             "working_hours": ["11:35-14:05", "09:00-11:00"]
             },
            {"courier_id": 405,
             "courier_type": "car",
             "regions": ['улица Дыбенко - улица Фролова'],
             "working_hours": ["11:35-14:05", "09:00-11:00"]
             },
            {"courier_id": 406,
             "courier_type": "bike",
             "regions": [1, 12, 22],
             "working_hours": ["11:35-14:05", "09:00-11:0S"]
             }
        ]}

        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, INCORRECT,
                         'Добавление проблемных курьеров-2 (status)')

        correct_answer = {
            "validation_error": {
                "couriers": [{"id": 404}, {"id": 405}, {"id": 406}]
            }
        }
        self.assertEqual(response.json(), correct_answer, 'Добавление проблемных курьеров-2 (id)')


if __name__ == '__main__':
    unittest.main(verbosity=2)
