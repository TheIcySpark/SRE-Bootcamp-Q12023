import mysql.connector
import hashlib
import jwt
from flask import abort

database_connection = mysql.connector.connect(
    host='sre-bootcamp-selection-challenge.cabf3yhjqvmq.us-east-1.rds.amazonaws.com',
    user='secret',
    password='jOdznoyH6swQB9sTGdLUeeSrtejWkcw',
    database='bootcamp_tht'
)

encrypt_token = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'

class Token:

    def generate_token(self, username, password):
        cursor = database_connection.cursor()
        cursor.execute('SELECT * FROM users where username = %s LIMIT 1', (username,))
        data = cursor.fetchone()

        if data:
            hash = hashlib.sha512(
                str(password + data[2]).encode('utf-8')).hexdigest()
            if hash == data[1]:
                return jwt.encode({'role': data[3]}, encrypt_token)
        abort(403)


class Restricted:

    def access_data(self, authorization: str):
        decoded_token = jwt.decode(
            authorization, encrypt_token, algorithms=['HS256'])
            
        cursor = database_connection.cursor()
        cursor.execute('SELECT role FROM users where role = %s LIMIT 1', (decoded_token['role'],))
        role = cursor.fetchone()

        if role:
            return 'You are under protected data'
        abort(403)
