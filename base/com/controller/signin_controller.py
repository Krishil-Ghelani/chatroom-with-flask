from base import app
from flask import render_template


@app.route('/')
def sign_in():
    return render_template('signIn.html')