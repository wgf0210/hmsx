from flask import Blueprint,render_template,request,jsonify,make_response,redirect,g

from common.models.User import User
from common.libs.user.UserService import Userservice
from common.libs.Helper import ops_render
from common.libs.UrlManager import UrlManager
from application import app,db

import json

router_user = Blueprint('user_page',__name__)

@router_user.route('/login/',methods=['POST','GET'])
def login():
    print('123')
    if request.method == 'GET':
        if g.current_user:
            return redirect(UrlManager.buildUrl('/'))
        return ops_render('user/login.html')
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
    
    return response
    # return jsonify(resp)

@router_user.route('/loginout/')
def loginout():
    response = make_response(redirect(UrlManager.buildUrl('/user/login')))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response

@router_user.route('/edit/',methods=['POST','GET'])
def edit():
    if request.method == 'GET':
        return ops_render('/user/edit.html')
    resp = {
        'code':200,
        'msg':'编辑成功',
        'data':{}
    }
    req = request.values
    nickname = req['nickname'] if 'nickname' in req else ''
    email = req['email'] if 'email' in req else ''
    # 校检
    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的姓名'
        return jsonify(resp)
    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的邮箱'
        return jsonify(resp)
    # 更新数据库
    user_info = g.current_user
    user_info.nickname = nickname
    user_info.email = email
    db.session.add(user_info)
    db.session.commit()
    return jsonify(resp)

@router_user.route('/resetpwd/',methods=['POST','GET'])
def resetpwd():
    if request.method == 'GET':
        return ops_render('/user/reset.html')
    resp = {
        'code':200,
        'msg':'重置密码成功',
        'data':{}
    }
    req = request.values
    old_password = req['old_password'] if 'old_password' in req else ''
    new_password = req['new_password'] if 'new_password' in req else ''
    
    # 校检
    if old_password is None or len(old_password)<6:
        resp['code'] = -1
        resp['msg'] = '请输入正确的原密码'
        return jsonify(resp)
    if new_password is None or len(new_password)<6:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的新密码'
        return jsonify(resp)
    if old_password == new_password:
        resp['code'] = -1
        resp['msg'] = '新密码与原密码不能一致，请重新输入'
        return jsonify(resp)
    # 获取用户信息,修改密码为新密码
    user_info = g.current_user
    user_info.login_pwd = Userservice.generatepwd(new_password,user_info.login_salt)
    db.session.add(user_info)
    db.session.commit()
    # 更新cookie的旧密码
    response = make_response(json.dumps(resp))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],'%s@%s'%(Userservice.generateAuthCode(user_info),user_info.uid),60*60*24*5)
    
    return response