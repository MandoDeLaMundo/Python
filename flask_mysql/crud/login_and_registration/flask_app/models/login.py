from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Login:
    db = "login_and_registration_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())"
        return connectToMySQL(Login.db).query_db(query, data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(Login.db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(Login.db).query_db(query, data)
        if results:
            return cls(results[0])


    @staticmethod
    def is_valid(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", "login")
            is_valid = False
        else:
            query = "SELECT * FROM emails WHERE email = %(email)s;"
            result = connectToMySQL(Login.db).query_db(query, data)
            if result:
                flash ("Email already taken", "login")
                is_valid = False
        return is_valid


    @staticmethod
    def validate_register(data):
        is_valid = True
        user = Login.get_by_email(data)
        if user:
            flash("That email already exists", "register")
            is_valid = False
        if len(data['first_name']) < 2:
            flash("First Name must be at least 2 characters.", "register")
            is_valid = False
        elif not data['first_name'].isalpha():
            flash("First name must consist of only letters", "register")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last Name must be at least 2 characters.", "register")
            is_valid = False
        elif not data['first_name'].isalpha():
            flash("First name must consist of only letters", "register")
            is_valid = False
        if len(data['email']) < 1:
            flash("Must create an email.", "register")
            is_valid = False
        if len(data['password']) < 8:
            flash("Must create a password.", "register")
            is_valid = False
        if (data['confirm_password']) != data['password']:
            flash("Passwords must match.", "register")
            is_valid = False
        return is_valid



    @staticmethod
    def validate_login( data ):
        is_valid = True
        if not Login.is_valid(data["email"]):
            is_valid = False
        else: 
            flash("The email address you entered is a VALID email address! Thank you!", "login")
        return is_valid