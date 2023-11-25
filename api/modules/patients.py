import functools
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from model.patients import (
    get_patients,
    get_patient,
    create_patient,
    update_patient,
    delete_patient,
    get_patients_by_medic_id
)

bp = Blueprint('patients', __name__, url_prefix='/patients')
CORS(bp)

@bp.route('/', methods=['GET'])
def list():
    retorno = get_patients()
    return jsonify(retorno)

@bp.route('/<int:id>', methods=['GET'])
def get(id):
    retorno = get_patient(id)
    return jsonify(retorno)

@bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    name = data['name']
    lastname = data['lastname']
    contact = data['contact']
    address = data['address']
    gender = data['gender']
    medic_id = data['medic_id']
    return jsonify(create_patient(name, lastname, contact, address, gender, medic_id))

@bp.route('/<int:patient_id>', methods=['PUT'])
def update(patient_id):
    data = request.get_json()
    name = data['name']
    lastname = data['lastname']
    contact = data['contact']
    address = data['address']
    gender = data['gender']
    medic_id = data['medic_id']
    return jsonify(update_patient(name, lastname, contact, address, gender, medic_id, patient_id))

@bp.route('/<int:patient_id>', methods=['DELETE'])
def delete(patient_id):
    return jsonify(delete_patient(patient_id))

@bp.route('/medic/<int:medic_id>', methods=['GET'])
def get_patients_by_medic(medic_id):
    retorno = get_patients_by_medic_id(medic_id)
    return jsonify(retorno)