from flask import Blueprint,render_template

router_index = Blueprint('index_pagr',__name__)

@router_index.route("/")
def index():

    return render_template("index/index.html")