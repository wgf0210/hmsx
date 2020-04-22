from application import app
from web.controllers.user.User import router_user

app.register_blueprint(router_user,url_prefix='/user')