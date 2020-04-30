from flask import Blueprint,request
from application import app,db
import os,datetime

router_upload = Blueprint('upload_page',__name__)

@router_upload.route('/ueditor',methods=['GET','POST'])
def ueditor():
    print('---------------------------123')
    return 'upload'

@router_upload.route('/pic',methods=['GET','POST'])
def uploadpic():
    file_target = request.files
    filename = file_target['pic'].filename
    print('-------------------',file_target['pic'].filename)
    # 将图片保存到static/upload/pic.jpg
    # 当前项目路径app.root_path
    root_path = app.root_path + app.config['UPLOAD']['prefix_path']
    file_dir = datetime.datetime.now().strftime('%Y%m%d')
    save_dir = root_path + '\\' + file_dir
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
        os.chmod(save_dir,stat.S_IRWXU | stat.S_IRGRP | stat.S_IRWXO)

    return 'pic'
