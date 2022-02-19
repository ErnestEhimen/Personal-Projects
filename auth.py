from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/create-account')
def create_account():
    return "<p>Create a Student account</p>"

@auth.route('/contacts')
def contacts():
    return "<p>Contact Information</p>"


