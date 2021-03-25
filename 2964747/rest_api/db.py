import json
import sqlite3

from courier import Courier
from order import Order

# Orders

CREATE_ORDERS_TABLE = 'CREATE TABLE IF NOT EXISTS orders (' \
                      'order_id INTEGER PRIMARY KEY,' \
                      'weight REAL,' \
                      'region INTEGER,' \
                      'delivery_hours TEXT,' \
                      'added_time FLOAT,' \
                      'done_time FLOAT);'

INSERT_ORDER = 'INSERT INTO orders ' \
               '(order_id, weight, region, delivery_hours, added_time, done_time) ' \
               'VALUES (?, ?, ?, ?, ?, ?);'

GET_ORDERS_TABLE = 'SELECT * FROM orders;'
GET_ORDER_BY_ID = 'SELECT * FROM orders WHERE order_id=?;'
GET_ORDERS_ID = 'SELECT order_id FROM orders;'
GET_OPENED_ORDERS = 'SELECT * FROM orders WHERE added_time=0;'

PATCH_ORDER_ADDED_TIME = 'UPDATE orders SET added_time=? WHERE order_id=?;'
PATCH_ORDER_DONE_TIME = 'UPDATE orders SET done_time=? WHERE order_id=?;'

# Couriers

CREATE_COURIERS_TABLE = 'CREATE TABLE IF NOT EXISTS couriers (' \
                        'courier_id INTEGER PRIMARY KEY,' \
                        'courier_type TEXT,' \
                        'regions TEXT,' \
                        'working_hours TEXT,' \
                        'orders TEXT);'

GET_COURIERS_TABLE = 'SELECT * FROM couriers;'
GET_COURIER_BY_ID = 'SELECT * FROM orders WHERE courier_id=?;'
GET_COURIERS_ID = 'SELECT courier_id FROM couriers;'

INSERT_COURIER = 'INSERT INTO couriers (courier_id, courier_type, regions, working_hours, orders) ' \
                 'VALUES (?, ?, ?, ?, ?);'

PATCH_COURIER = 'UPDATE couriers SET ?=? WHERE courier_id=?;'

# Assigns

CREATE_ASSIGNS_TABLE = 'CREATE TABLE IF NOT EXISTS assigns (' \
                       'courier_id INTEGER,' \
                       'num_assigns INTEGER);'

GET_ASSIGN_BY_ID = 'SELECT num_assigns FROM assigns WHERE courier_id=?'
INSERT_ASSIGN = 'INSERT INTO assigns (courier_id, num_assigns) VALUES (?, ?)'
PATCH_ASSIGN = 'UPDATE assings SET num_assigns=? WHERE courier_id=?'


def get_assign_by_id(connection, courier_id):
    with connection:
        return connection.execute(GET_ASSIGN_BY_ID, courier_id).fetchone()[0]


def insert_assign(connection, courier_id, num_assigns):
    with connection:
        connection.execute(INSERT_ASSIGN, (courier_id, num_assigns))


def patch_assign(connection, courier_id, num_assigns):
    with connection:
        connection.execute(PATCH_ASSIGN, (num_assigns, courier_id))


# Tables and connect

def connect():
    return sqlite3.connect('data.db')


def create_tables(connection):
    with connection:
        connection.execute(CREATE_COURIERS_TABLE)
        connection.execute(CREATE_ORDERS_TABLE)
        connection.execute(CREATE_ASSIGNS_TABLE)


# Couriers

def patch_courier(connection, property, value, id):
    with connection:
        if type(value) == list:
            value = json.dumps(value)
        connection.execute(PATCH_COURIER, (property, value, id))


def get_couriers(connection):
    with connection:
        data = connection.execute(GET_COURIERS_TABLE).fetchall()
        couriers = []
        for element in data:
            courier = Courier(element[0],
                              element[1],
                              json.loads(element[2]),
                              json.loads(element[3]),
                              json.loads(element[4]))

            couriers.append(courier)
        return couriers


def get_couriers_id(connection):
    with connection:
        data = connection.execute(GET_COURIERS_ID).fetchall()
        return [elem[0] for elem in data]


def get_courier_by_id(connection, courier_id):
    with connection:
        element = connection.execute(GET_COURIER_BY_ID, courier_id).fetchall()[0]
        courier = Courier(element[0],
                          element[1],
                          json.loads(element[2]),
                          json.loads(element[3]),
                          json.loads(element[4]))
        return courier


def insert_couriers(connection, couriers):
    with connection:
        for courier in couriers:
            connection.execute(INSERT_COURIER, (courier.courier_id,
                                                courier.courier_type,
                                                json.dumps(courier.regions),
                                                json.dumps(courier.working_hours),
                                                json.dumps(courier.orders)))


# Orders

def patch_order_added_time(connection, new_time, order_id):
    with connection:
        connection.execute(PATCH_ORDER_ADDED_TIME, (new_time, order_id))


def patch_order_done_time(connection, new_time, order_id):
    with connection:
        connection.execute(PATCH_ORDER_DONE_TIME, (new_time, order_id))


def get_orders_id(connection):
    with connection:
        data = connection.execute(GET_ORDERS_ID).fetchall()
        return [elem[0] for elem in data]


def get_order_by_id(connection, order_id):
    with connection:
        data = connection.execute(GET_ORDER_BY_ID, order_id).fetchall()[0]
        order = Order(data[0], data[1], data[2], json.loads(data[3]), data[4], data[5])
        return order


def get_opened_orders(connection):
    with connection:
        return connection.execute(GET_OPENED_ORDERS).fetchall()


def insert_orders(connection, orders):
    with connection:
        for order in orders:
            connection.execute(INSERT_ORDER,
                               (order.order_id,
                                order.weight,
                                order.region,
                                json.dumps(order.delivery_hours),
                                order.added_time,
                                order.done_time))


# создание базы данных (если еще нет) при подключении этого файла к любому исполняемому
_connection_db = connect()
create_tables(_connection_db)
