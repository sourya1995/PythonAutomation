from flask import (make_response, request, jsonify, Blueprint, url_for)
from .data_store import products


products_blueprint = Blueprint('products_api', __name__, url_prefix='/api/')

@products_blueprint.route('/products', methods=['GET'])
def list_products():
    return jsonify(products)

@products_blueprint.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    for product in products:
        if product['id'] == product_id:
            return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

@products_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    data['id'] = str(len(products) + 1)
    products.append(data)
    location = url_for('.get_product', product_id=data['id'], _external=True)
    response = jsonify(dict(product=data, location=location))
    response.headers['Location'] = location
    return response, 201

@products_blueprint.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json() #extract the json data from the request
    updated_product = None
    for product in products:
        if product['id'] == product_id:
            product.update(data)
            updated_product = product
    return jsonify(updated_product)

@products_blueprint.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            break
    response = make_response("", 204)
    response.mimetype = 'application/json'
    return response

@products_blueprint.after_request
def after_request(response):
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    return response