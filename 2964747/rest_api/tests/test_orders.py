import json
import unittest

import requests

SUCCESS = 200
INCORRECT = 400
ADDED = 201


class OrdersTest(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(OrdersTest, self).__init__(*a, **kw)
        # тест проходил на локальной машине, поэтому здесь localhost и соответствующий порт
        self.host = '127.0.0.1:5000'
        self.command = 'orders'
        self.url = 'http://{}/{}'.format(self.host, self.command)

    @staticmethod
    def print_json(response):
        print('\n\n', json.dumps(response.json(), indent=4, sort_keys=True))

    def test_new_order(self):
        payload = {"data": [
            {
                "order_id": 1,
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, ADDED, 'Добавление одного заказа (status)')
        correct_answer = {"orders": [{"id": 1}]}
        self.assertEqual(response.json(), correct_answer, 'Добавление одного заказа (id)')


if __name__ == '__main__':
    unittest.main(verbosity=2)
