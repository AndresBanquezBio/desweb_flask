import functools
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from model.medics import (
    get_medics,
    get_medic,
    create_medic,
    update_medic,
    delete_medic
)

bp = Blueprint('medics', __name__, url_prefix='/medics')
CORS(bp)

@bp.route('/', methods=['GET'])
def list():
    retorno = get_medics()
    return jsonify(retorno)

@bp.route('/<int:id>', methods=['GET'])
def get():
    retorno = get_medic(id)
    return jsonify(retorno)

@bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    name = data['name']
    contact = data['contact']
    specialty = data['specialty']
    return jsonify(create_medic(name, contact, specialty))

@bp.route('/<int:medic_id>', methods=['PUT'])
def update(medic_id):
    data = request.get_json()
    name = data['name']
    contact = data['contact']
    specialty = data['specialty']
    return jsonify(update_medic(name, contact, specialty, medic_id))

@bp.route('/<int:medic_id>', methods=['DELETE'])
def delete(medic_id):
    return jsonify(delete_medic(medic_id))