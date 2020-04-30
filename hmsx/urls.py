from application import app
from web.controllers.user.User import router_user
from web.controllers.index import router_index
from web.controllers.Account.account import router_account
from web.controllers.member.Member import router_member
from web.controllers.goods.Goods import router_goods

# 拦截器的路由
from web.interceptors.AuthInterceptor import *

# 蓝图路由
app.register_blueprint(router_user,url_prefix='/user')
app.register_blueprint(router_index,url_prefix='/')
app.register_blueprint(router_account,url_prefix='/account')
app.register_blueprint(router_member,url_prefix='/member')
app.register_blueprint(router_goods,url_prefix='/goods')