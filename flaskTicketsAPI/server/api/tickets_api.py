from uuid import uuid5
from flask import (make_response, request, jsonify, Blueprint, url_for)
from .data_store import tickets


tickets_blueprint = Blueprint('tickets_api', __name__, url_prefix='/api/')

@tickets_blueprint.route('/tickets', methods=['GET'])
def get_tickets():
    return jsonify(tickets)

@tickets_blueprint.route('/tickets/<ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            return jsonify(ticket)
    return jsonify({'error': 'Ticket not found'}), 404

@tickets_blueprint.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    data['id'] =  str(len(tickets) + 1)
    tickets.append(data)
    location = url_for('.get_ticket', ticket_id=data['id'], _external=True)
    response = jsonify(dict(ticket=data, location=location))
    response.headers['Location'] = location
    return response, 201

@tickets_blueprint.route('/tickets/<ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    data = request.get_json() #extract the json data from the request
    updated_product = None
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            ticket.update(data)
            updated_product = ticket
    return jsonify(updated_product)

@tickets_blueprint.route('/tickets/<ticket_id>', methods=['DELETE'])
def delete_product(ticket_id):
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            tickets.remove(ticket)
            break
    response = make_response("", 204)
    response.mimetype = 'application/json'
    return response

@tickets_blueprint.after_request
def after_request(response):
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    return response