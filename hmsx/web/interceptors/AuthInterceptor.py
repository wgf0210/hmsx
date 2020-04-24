from application import app
from flask import request,redirect

from common.libs.UrlManager import UrlManager

# 每次请求之前都要先经过这里
@app.before_request
def before_request():
    path = request.path

    user_info = check_login()
    if not user_info:
        return redirect(UrlManager.buildUrl('/user/login'))
    return

# 判断用户是否登录，返回用户信息user_info
def check_login():
    return 
