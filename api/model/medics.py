import functools
import db
import pymysql

def get_medics():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM medics"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_medic(id):
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret = {}
    try:
        sql="SELECT * FROM medics WHERE id = {}".format(id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_medic(name,contact,specialty):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql = "INSERT INTO medics(name,contact,specialty) VALUES('{0}','{1}','{2}')".format(name,contact,specialty)
        cursor.execute(sql)
        con.commit()
        id_med = cursor.lastrowid
        return {"message":"OK","id":id_med}
    finally:
        con.close()

def update_medic(name, contact, specialty, medic_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE medics set name='{0}', contact='{1}', specialty='{2}' WHERE id = {3}".format(name, contact, specialty, medic_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_medic(medic_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM medics WHERE id = {}".format(medic_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
