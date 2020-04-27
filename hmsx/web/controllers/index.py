from flask import Blueprint,render_template
from common.libs.Helper import ops_render

router_index = Blueprint('index_pagr',__name__)

@router_index.route("/")
def index():

    return ops_render("index/index.html")