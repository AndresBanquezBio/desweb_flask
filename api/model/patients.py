import functools
import db
import pymysql

def get_patients():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql = "SELECT * FROM patients"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_patient(patient_id):
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret = {}
    try:
        sql = "SELECT * FROM patients WHERE id = {}".format(patient_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_patient(name, lastname, contact, address, gender, medic_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql = "INSERT INTO patients(name, lastname, contact, address, gender, medic_id) VALUES('{0}','{1}','{2}','{3}','{4}',{5})".format(name, lastname, contact, address, gender, medic_id)
        cursor.execute(sql)
        con.commit()
        patient_id = cursor.lastrowid
        return {"message": "OK", "id": patient_id}
    finally:
        con.close()

def update_patient(name, lastname, contact, address, gender, medic_id, patient_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql = "UPDATE patients SET name='{0}', lastname='{1}', contact='{2}', address='{3}', gender='{4}', medic_id={5} WHERE id = {6}".format(name, lastname, contact, address, gender, medic_id, patient_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message": "OK"}
    finally:
        con.close()

def delete_patient(patient_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql = "DELETE FROM patients WHERE id = {}".format(patient_id)
        cursor.execute(sql)
        con.commit()
        return {"message": "OK"}
    finally:
        con.close()

def get_patients_by_medic_id(medic_id):
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql = "SELECT * FROM patients WHERE medic_id = {}".format(medic_id)
        cursor.execute(sql)
        ret = cursor.fetchall()
        return ret
    finally:
        con.close()