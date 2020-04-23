from flask import Blueprint,render_template

router_user = Blueprint('user_page',__name__)

@router_user.route('/login/')
def login():
    print('123')
    return render_template('user/login.html')

@router_user.route('/loginout/')
def loginout():
    print('123')
    return 'loginout页面'

@router_user.route('/edit/')
def edit():
    print('123')
    return 'edit页面'

@router_user.route('/resetpwd/')
def resetpwd():
    print('123')
    return '重置密码页面'