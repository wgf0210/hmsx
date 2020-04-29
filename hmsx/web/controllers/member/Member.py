from flask import Blueprint,request,redirect,jsonify
from common.libs.Helper import ops_render,getcurrentdate,ipagenation
from common.models.member.Member import Member
from common.models.member.MemberComment import MemberComment
from application import app,db
from sqlalchemy import or_

router_member = Blueprint('member_page',__name__)

@router_member.route("/index/")
def index():
    resp_data = {}
    query = Member.query
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    if 'status' in req and int(req['status']) > -1:
        query = query.filter(Member.status == int(req['status']))
    if 'mix_kw' in req:
        rule = or_( Member.nickname.ilike("%{0}%".format(req['mix_kw'])), Member.mobile.ilike("%{0}%".format(req['mix_kw'])) )
        query = query.filter(rule)
    params = {
        "total":query.count(),
        "page_size":2,
        "page":page,
        "url":request.full_path.replace("&p={}".format(page),"")
    }
    pages = ipagenation(params)
    # 当前页数据开始位置  
    offset = (page-1) * 2
    # 当前页数据结束位置  
    limit = page * 2

    list = query.all()[offset:limit]

    resp_data['list'] = list
    resp_data['status'] = app.config['STATUS']
    resp_data['pages'] = pages
    return ops_render("/member/index.html",resp_data)

@router_member.route("/info/")
def info():
    resp_data = {}
    req = request.args
    id = int(req.get('id',0)) if req['id'] else 1
    member_info = Member.query.filter_by(id=id).first()
    resp_data['info'] = member_info
    return ops_render("/member/info.html",resp_data)


@router_member.route("/set/",methods=['GET','POST'])
def set():
    resp_data = {}
    req = request.args
    id = int(req.get('id',0)) if req['id'] else 1
    member_info = Member.query.filter_by(id=id).first()
    resp_data['info'] = member_info
    return ops_render("/member/set.html",resp_data)


@router_member.route("/comment/")
def comment():
    resp_data = {}
    comment_list = MemberComment.query.all()
    resp_data['list'] = comment_list
    member_info = {
        'avatar':'',
        'nickname':'bruce'
    }
    for item in comment_list:
        item.member_info = member_info
    # resp_data['list'].member_info = member_info
    return ops_render("/member/comment.html",resp_data)


@router_member.route('/remove-or-recover/',methods=['POST','GET'])
def removeorrecover():
    resp = {
        'code':200,
        'msg':'操作账号成功！！',
        'data':{}
    }
    req = request.values
    ids = req['id'] if 'id' in req else 0
    acts = req['acts'] if 'acts' in req else ''
    if not ids:
        resp['code'] = -1
        resp['msg'] = '请选择要操作的账号'
        return jsonify(resp)
    if acts not in ['remove','recover']:
        resp['code'] = -1
        resp['msg'] = '亲，操作出现失误了~~'
        return jsonify(resp)
    member_info = Member.query.filter_by(id=ids).first()
    if not member_info:
        resp['code'] = -1
        resp['msg'] = '该账号不存在'
        return jsonify(resp)
    
    if acts == 'remove':
        member_info.status = 0
    elif acts == 'recover':
        member_info.status = 1
    member_info.updated_time = getcurrentdate()
    db.session.add(member_info)
    db.session.commit()

    return jsonify(resp)
