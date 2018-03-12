import mysql.connector

def create_new_table():

    cnx = mysql.connector.connect(user='testuser', password='test', host='127.0.0.1', database='test')
    cursor = cnx.cursor()

    add_employee = ("CREATE TABLE from_python2 (person_id INTEGER)")

    cursor.execute(add_employee)

    cnx.commit()
    cursor.close()
    cnx.close()


def edit_table():
    cnx = mysql.connector.connect(user='testuser', password='test', host='127.0.0.1', database='test')
    cursor = cnx.cursor()

    add_employee = ("CREATE TABLE from_python (person_id INTEGER)")

    cursor.execute(add_employee)

    cnx.commit()
    cursor.close()
    cnx.close()


def create_new_schema():
    cnx = mysql.connector.connect(user='testuser', password='test', host='127.0.0.1', database='test')
    cursor = cnx.cursor()

    add_employee = ("CREATE TABLE from_python (person_id INTEGER)")

    cursor.execute(add_employee)

    cnx.commit()
    cursor.close()
    cnx.close()
