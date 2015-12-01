from flask import Blueprint, jsonify, abort, request

from api.helpers import Helpers
import storage

from flask import current_app

client_api = Blueprint('client_api', __name__)
# print(client_api.__dict__)

@client_api.route('/cl', methods=['GET'])
def gtt():
    current_app.logger.info('Info')
    return jsonify({'GET': storage.clientsList})


@client_api.route('/client_api/api/v1.0/orders', methods=['GET'])
def get_tasks():
    return jsonify({'GET': storage.clientsList})


@client_api.route('/client_api/api/v1.0/orders/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Helpers.is_client(task_id, storage.clientsList)
    if task is False:
        return jsonify({'GET': False})

    return jsonify({'GET': task})


@client_api.route('/client_api/api/v1.0/orders', methods=['POST'])
def create_order():
    if not request.json:
        abort(400)
    content = request.get_json(force=True)
    task = Helpers.is_client(content["client_id"], storage.clientsList)
    if task:
        return jsonify({'POST': False})

    order = {
        'id': content["client_id"],
        'time': content["time"],
        'lat': content["lat"],
        'lon': content["lon"],
        'taxi': False,
    }
    current_app.logger.info(" client register %d", content["client_id"])
    storage.clientsList.append(order)
    # return jsonify({'POST': order})
    return "{}".format(content), 201



@client_api.route('/client_api/api/v1.0/orders/<int:task_id>', methods=['PUT'])
def update_task(task_id):

    task = Helpers.is_client(task_id, storage.clientsList)

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
        'taxi': content["taxi"],
    }

    new = Helpers.list_updater(task_id, storage.clientsList, order)
    current_app.logger.info(" client update %d", content["client_id"])

    return jsonify({'PUT': new})
    # return "{}".format(storage.clientsList), 201

@client_api.route('/client_api/api/v1.0/orders/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Helpers.is_client(task_id, storage.clientsList)
    if task is False:
        return jsonify({'DELETE': task_id})

    Helpers.list_del(task_id, storage.clientsList)
    current_app.logger.info(" client del %d", task_id)

    # return jsonify({'DELETE': True})
    return "{}".format(storage.clientsList), 201

