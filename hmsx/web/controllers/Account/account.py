from flask import Blueprint,request,redirect,jsonify
from sqlalchemy import or_
from common.libs.Helper import ops_render,getcurrentdate
from common.libs.UrlManager import UrlManager
from common.libs.user.UserService import Userservice
from common.models.User import User
from application import db,app

router_account = Blueprint('account_age',__name__)

@router_account.route('/index/')
def index():
    resp_data = {}
    query = User.query
    req = request.values
    if 'status' in req and int(req['status']) > -1:
        query = query.filter(User.status == int(req['status']))
    if 'mix_kw' in req:
        rule = or_(User.nickname.ilike('%{0}%'.format(req['mix_kw'])),User.mobile.ilike('%{0}%'.format(req['mix_kw'])))
        query = query.filter(rule)

    list = query.all()
    resp_data['list'] = list
    resp_data['status'] = app.config['STATUS']
    return ops_render('/account/index.html',resp_data)

@router_account.route('/info/')
def info():
    resp_data = {}
    req = request.args
    uid = int(req.get('id',0))
    reback_url = UrlManager.buildUrl('/account/index/')
    if uid < 1:
        return redirect(reback_url)
    info = User.query.filter_by(uid=uid).first()
    if not info:
        return redirect(reback_url)
    resp_data['info'] = info
    return ops_render('/account/info.html',resp_data)

'''
    带id参数--修改：更新数据库
    不带id参数--添加：创建数据，插入数据库
'''
@router_account.route('/set/',methods=['GET','POST'])
def set():
    if request.method == 'GET':
        resp_data = {}
        req = request.args
        uid = int(req.get('id',0))
        info = None
        if uid:
            info = User.query.filter_by(uid=uid).first()
        resp_data['info'] = info
        return ops_render('/account/set.html',resp_data)
    resp = {
        'code':200,
        'msg':'操作成功！',
        'data':{}
    }
    # 获取前端ajax传递的data
    req = request.values
    id = req['id'] if 'id' in req else 0
    nickname = req['nickname'] if 'id' in req else ''
    mobile = req['mobile'] if 'id' in req else ''
    email = req['email'] if 'id' in req else ''
    login_name = req['login_name'] if 'id' in req else ''
    login_pwd = req['login_pwd'] if 'id' in req else ''
    # 校检
    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = '昵称格式错误'
        return jsonify(resp)
    if mobile is None or len(mobile) < 1:
        resp['code'] = -1
        resp['msg'] = '手机号格式错误'
        return jsonify(resp)
    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = '邮箱格式错误'
        return jsonify(resp)
    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '登录名格式错误'
        return jsonify(resp)
    if login_pwd is None or len(login_pwd) < 6:
        resp['code'] = -1
        resp['msg'] = '密码格式错误'
        return jsonify(resp)
    # 筛选
    is_exits = User.query.filter(User.login_name==login_name,User.uid!=id).first()
    if is_exits:
        resp['code'] = -1
        resp['msg'] = '该登录名已存在，请更换~~~'
        return jsonify(resp)
    user_info = User.query.filter_by(uid=id).first()
    if user_info:
        model_user = user_info
    else:
        model_user = User()
        # 插入格式化的时间
        model_user.created_time = getcurrentdate()
        # 生成16位的加密字符串
        model_user.login_salt = Userservice.generateSalt()
    model_user.nickname = nickname
    model_user.mobile = mobile
    model_user.email = email
    model_user.login_name = login_name
    model_user.login_pwd = login_pwd
    if user_info and user_info.uid == 1:
        resp['code'] = -1
        resp['msg'] = '该用户为tzmm'
        return jsonify(resp)
    model_user.login_pwd = Userservice.generatepwd(login_pwd,model_user.login_salt)
    # 插入格式化时间
    model_user.updated_time = getcurrentdate()

    db.session.add(model_user)
    db.session.commit()

    return jsonify(resp)


@router_account.route('/remove-or-recover/',methods=['GET','POST'])
def removeorrecover():
    resp = {
        'code':200,
        'msg':'操作账号成功！！',
        'data':{}
    }
    req = request.values
    id = req['id'] if 'id' in req else 0
    acts = req['acts'] if 'acts' in req else ''
    if not id:
        resp['code'] = -1
        resp['msg'] = '请选择要操作的账号'
        return jsonify(resp)
    if acts not in ['remove','recover']:
        resp['code'] = -1
        resp['msg'] = '亲，操作出现失误了~~'
        return jsonify(resp)
    user_info = User.query.filter_by(uid=id).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = '该账号不存在'
        return jsonify(resp)
    if user_info and user_info.uid == 1:
        resp['code'] = -1
        resp['msg'] = '该账号是tzmm，不允许操作'
        return jsonify(resp)
    if acts == 'remove':
        user_info.status = 0
    elif acts == 'recover':
        user_info.status = 1
    user_info.updated_time = getcurrentdate()
    db.session.add(user_info)
    db.session.commit()

    return jsonify(resp)

