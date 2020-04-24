from flask import Blueprint,render_template,request,jsonify,make_response

from common.models.User import User
from common.libs.user.UserService import Userservice
from application import app

import json

router_user = Blueprint('user_page',__name__)

@router_user.route('/login/',methods=['POST','GET'])
def login():
    print('123')
    if request.method == 'GET':
        return render_template('user/login.html')
    resp = {
        'code':200,
        'msg':'登陆成功！',
        'data':{}
    }
    req = request.values
    login_name = req['login_name']
    login_pwd = req['login_pwd']
    # 后端校检 不为空，长度不小于1
    if login_name is None or len(login_name)<1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名'
        return jsonify(resp)
    if login_pwd is None or len(login_pwd)<1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的密码'
        return jsonify(resp)
    # 数据库比对
    user_info = User.query.filter_by(login_name=login_name).first()
    print(user_info.login_name)
    if not user_info:
        resp['code'] = -1
        resp['msg'] = '用户不存在'
        return jsonify(resp)
    if user_info.status != 1:
        resp['code'] = -1
        resp['msg'] = '账号已被禁用,请联系管理员处理'
        return jsonify(resp)
    if user_info.login_pwd != Userservice.generatepwd(login_pwd,user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = '密码错误'
        return jsonify(resp)
    print('账号密码正确')
    # 将用户信息存入到浏览器的cookie中
    # json.dumps()他只能处理dict和list类型，经过处理之后可以直接在前端/浏览器中使用
    response = make_response(json.dumps({'code':200,'msg':'登陆成功！'}))
    # name，value，过期时间
    # value包括login_name，login_pwd，login_salt，uid
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],'%s@%s'%(Userservice.generateAuthCode(user_info),user_info.uid),60*60*24*5)

    return jsonify(resp)
    

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