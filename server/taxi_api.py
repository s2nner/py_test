from flask import Blueprint, jsonify, abort, request

from api.helpers import Helpers
import storage

taxi_api = Blueprint('taxi_api', __name__)
# print(client_api.__dict__)

@taxi_api.route('/taxi_api/api/v1.0/orders', methods=['GET'])
def get_tasks():
    return jsonify({'GET': storage.taxiList})


@taxi_api.route('/taxi_api/api/v1.0/orders/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Helpers.is_client(task_id, storage.taxiList)
    if task is False:
        return jsonify({'GET': False})




    return jsonify({'GET': task})


@taxi_api.route('/taxi_api/api/v1.0/orders', methods=['POST'])
def create_order():
    if not request.json:
        abort(400)
    content = request.get_json(force=True)
    task = Helpers.is_client(content["client_id"], storage.taxiList)
    if task:
        return jsonify({'POST': False})

    order = {
        'id': content["client_id"],
        'time': content["time"],
        'lat': content["lat"],
        'lon': content["lon"],
        'taxi': False,
    }
    storage.taxiList.append(order)
    # return jsonify({'POST': order})
    return "{}".format(content), 201



@taxi_api.route('/taxi_api/api/v1.0/orders/<int:task_id>', methods=['PUT'])
def update_task(task_id):

    task = Helpers.is_client(task_id, storage.taxiList)

    if task is False:
        abort(404)
    if not request.json:
        abort(400)

    content = request.get_json(force=True)

    order = {
        'id': content["client_id"],
        'time': content["time"],
        'lat': content["lat"],
        'lon': content["lon"],
    }

    new = Helpers.list_updater(task_id, storage.taxiList, order)

    return jsonify({'PUT': new})
    # return "{}".format(storage.clientsList), 201

@taxi_api.route('/taxi_api/api/v1.0/orders/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Helpers.is_client(task_id, storage.taxiList)
    if task is False:
        return jsonify({'DELETE': task_id})

    Helpers.list_del(task_id, storage.taxiList)

    # return jsonify({'DELETE': True})
    return "{}".format(storage.taxiList), 201

