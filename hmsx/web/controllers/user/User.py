from flask import Blueprint

router_user = Blueprint('user_page',__name__)

@router_user.route('/login/')
def login():
    print('123')
    return 'login页面'