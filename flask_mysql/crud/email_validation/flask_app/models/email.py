from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_validation_schema').query_db(query)
        emails = []
        for email in results:
            emails.append( cls(email))
        return emails


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query, data)
        if results:
            return cls(results[0])


    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL('email_validation_schema').query_db(query, data)



    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash("First Name must be at least 2 characters.", "register")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last Name must be at least 2 characters.", "register")
            is_valid = False
        if len(data['email']) < 1:
            flash("Must create an email.", "register")
            is_valid = False
        if len(data['password']) < 8:
            flash("Must create a password.", "register")
            is_valid = False
        if len(data['password_confirm']) != data['password']:
            flash("Passwords must match.", "register")
            is_valid = False
        return is_valid


    @staticmethod
    def validate_login( data ):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "login")
            is_valid = False
        if EMAIL_REGEX.match(data['email']): 
            flash("The email address you entered is a VALID email address! Thank you!", "login")
        return is_valid