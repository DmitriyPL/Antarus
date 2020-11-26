from flask import session, redirect, render_template, url_for, request

from app import app


@app.route('/', methods=["GET"])
def main_view():

    return render_template("main.html")
