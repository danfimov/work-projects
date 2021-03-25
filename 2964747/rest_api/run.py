import time
from datetime import datetime

from flask import Flask, jsonify, request, make_response

import db
from courier import Courier
from order import Order

app = Flask(__name__)


# необязательная возможность посмотреть на список всех курьеров
@app.route('/couriers', methods=['GET'])
def get_couriers():
    conn = db.connect()
    return jsonify({'data': db.get_couriers(conn)})


# 1) POST /couriers
@app.route('/couriers', methods=['POST'])
def add_couriers():
    elements, errors, conn = [], [], db.connect()
    ids = db.get_couriers_id(conn)
    for element in request.json['data']:
        try:
            if element['courier_id'] in ids:
                raise (ValueError, 'Такой id уже существует в базе данных')
            c = Courier(element['courier_id'], element['courier_type'], element['regions'],
                        element['working_hours'])
            elements.append(c)
        except Exception:
            errors.append({'id': element['courier_id']})

    # если в процессе добавления возникли ошибки
    if errors:
        return jsonify({'validation_error': {'couriers': errors}}), 400

    db.insert_couriers(conn, elements)
    return jsonify({'couriers': [{'id': elem.courier_id} for elem in elements]}), 201


# 2) PATCH /couriers/$courier_id
@app.route('/couriers/<int:courier_id>', methods=['PATCH'])
def patch_courier(courier_id):
    # TODO: 2 - прокатить тесты
    conn = db.connect()
    try:
        courier = db.get_courier_by_id(conn, courier_id)
    except:
        return jsonify({'Error': 'Bad courier_id'}), 400

    for key in request.json().keys():
        try:
            db.patch_courier(conn, key, request.json[key], courier_id)
        except:
            return jsonify({'Error': 'Bad property'}), 400

    courier = db.get_courier_by_id(conn, courier_id)
    max_weight = 10 * (courier.courier_type == 'foot') + 15 * (
            courier.courier_type == 'bike') + 50 * (courier.courier_type == 'car')

    orders_updated = []
    for order_id in courier:
        order = db.get_order_by_id(conn, order_id)

        flag = True
        if max_weight < order.weight:
            flag = False
            continue

        if order.region not in courier.regions:
            flag = False
            continue

        for time_d in order.delivery_hours:
            for time_w in courier.working_hours:
                if not time_in_gap(time_d, time_w):
                    flag = False
                    break

        if flag:
            orders_updated.append(order.order_id)

    for order in courier.orders:
        if order not in orders_updated:
            db.patch_order_added_time(conn, 0, order.order_id)

    db.patch_courier(conn, 'orders', orders_updated, courier_id)
    courier = db.get_courier_by_id(conn, courier_id)
    return jsonify(courier), 200


# 3) POST /orders
@app.route('/orders', methods=['POST'])
def add_orders():
    elements, errors, conn = [], [], db.connect()
    ids = db.get_orders_id(conn)
    for element in request.json['data']:
        try:
            if element['order_id'] in ids:
                raise (ValueError, 'Такой id уже существует в базе данных')
            c = Order(element['order_id'], element['weight'], element['region'],
                      element['delivery_hours'])
            elements.append(c)
        except Exception:
            errors.append({'id': element['order_id']})

    # если в процессе добавления возникли ошибки
    if errors:
        return jsonify({'validation_error': {'orders': errors}}), 400

    db.insert_orders(conn, elements)
    return jsonify({'orders': [{'id': elem.order_id} for elem in elements]}), 201


def time_in_gap(time_gap, time):
    time_gap_1 = int(time_gap[:2]) * 60 + int(time_gap[3:5])
    time_gap_2 = int(time_gap[6:8]) * 60 + int(time_gap[9:])

    time_1 = int(time[:2]) * 60 + int(time[3:5])
    time_2 = int(time[6:8]) * 60 + int(time[9:])

    return time_gap_1 <= time_1 <= time_gap_2 or time_gap_1 <= time_2 <= time_gap_2


# 4) POST /orders/assign
@app.route('/orders/assign', methods=['POST'])
def orders_assign():
    # TODO: 4 - прокатить тесты
    conn = db.connect()
    courier_id = request.json['courier_id']

    opened_orders = db.get_opened_orders(conn)

    try:
        courier = db.get_courier_by_id(conn, courier_id)
    except:
        return jsonify({'Error': 'Bad courier_id'}), 400

    max_weight = 10 * (courier.courier_type == 'foot') + 15 * (
            courier.courier_type == 'bike') + 50 * (courier.courier_type == 'car')

    courier_new_orders = []

    for order in opened_orders:
        flag = True
        if max_weight < order.weight:
            flag = False
            continue

        if order.region not in courier.regions:
            flag = False
            continue

        for time_d in order.delivery_hours:
            for time_w in courier.working_hours:
                if not time_in_gap(time_d, time_w):
                    flag = False
                    break

        if flag:
            courier_new_orders.append(order.order_id)

    assign_time = datetime.now(tz=None)
    assing_time_db = time.mktime(assign_time.timetuple())

    for order in courier_new_orders:
        db.patch_order_added_time(conn, assing_time_db, order.order_id)

    # обновление информации о количестве развозов курьера
    try:
        num_assigns = db.get_assign_by_id(conn, courier_id)
    except:
        num_assigns = 1
        db.insert_assign(conn, courier_id, num_assigns)

    db.patch_assign(conn, courier_id, num_assigns + 1)

    return jsonify({'orders': [{'id': elem.order_id} for elem in courier_new_orders],
                    'assign_time': assign_time.__str__()}), 200


# 5) POST /orders/complete
@app.route('/orders/complete', methods=['POST'])
def order_complete():
    # TODO: 5 - прокатить тесты
    conn = db.connect()

    courier_id = request.json['courier_id']
    order_id = request.json['order_id']

    # TODO: настроить более компактный парсинг даты
    date_time_str = request.json['complete_time']
    date_time_str = date_time_str[2:10] + ' ' + date_time_str[11: date_time_str.find('.')]
    date_time_obj = datetime.strptime(date_time_str, '%y-%m-%d %H:%M:%S')
    date_time_float = time.mktime(date_time_obj.timetuple())

    opened_orders = db.get_opened_orders(conn)

    try:
        courier = db.get_courier_by_id(conn, courier_id)
        order = db.get_order_by_id(conn, order_id)
    except:
        return jsonify({'Error': 'Bad courier_id or order_id'}), 400

    db.patch_order_done_time(conn, date_time_float, order_id)
    return jsonify({'order_id': order_id}), 200


# 6) GET /couriers/courier_id
@app.route('/couriers/<int:courier_id>', methods=['GET'])
def courier_info(courier_id):
    # TODO: 6 - прокатить тесты
    conn = db.connect()
    courier = db.get_courier_by_id(conn, courier_id)

    info = {'courier_id': courier.courier_id, 'courier_type': courier.courier_type,
            'regions': courier.regions, 'working_hours': courier.working_hours}

    # расчет рейтинга

    orders_done = []  # выделяем только доставленные из списка заказов курьера
    for order_id in courier.orders:
        order = db.get_order_by_id(conn, order_id)
        if order.done_time != 0:
            orders_done.append(order)

    order_regions = {}  # распределяем доставленные заказы по районам
    for order in orders_done:
        if order.region not in order_regions.keys():
            order_regions[order.region] = [order]
        else:
            order_regions[order.region].append(order)

    min_mean = None
    for region in order_regions.keys():
        orders = order_regions[region]
        orders.sort(key=lambda x: x.done_time)

        current_mean = orders[0].done_time - orders[0].added_time

        if len(orders) > 1:
            for i in range(1, len(orders)):
                current_mean += orders[i].done_time - orders[i - 1].done_time

        current_mean /= len(orders)
        if min_mean:
            min_mean = min(current_mean, min_mean)
        else:
            min_mean = current_mean

    rating = (60 * 60 - min(min_mean, 60 * 60)) / (60 * 60) * 5
    info['rating'] = rating

    max_weight_coefficient = courier.max_weight_coefficient
    info['earnings'] = db.get_assign_by_id(conn, courier_id) * 500 * max_weight_coefficient

    return jsonify(info), 200


# на всякий случай ошибка 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run()
