
# 连接到数据库
SQLALCHEMY_DATABASE_URI = 'mysql://root:002598@127.0.0.1/hmsx_db?charset=utf8'
# 消除警告
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 设置服务器端口
SERVER_PORT = 5000
# cookie
AUTH_COOKIE_NAME = '1903hmsx'
# 拦截器忽略规则
IGNORE_URLS = ['^/user/login']
IGNORE_CHECK_LOGIN_URLS = [
    '^/static',
    '^/favicon.ico'
]

STATUS = {
    '1':'正常',
    '0':'已删除'
}

UPLOAD = {
    'ext':['jpg','png','bmp','jpeg','gif'],
    'prefix_path':'\\web\\static\\upload',
    'prefix_url':'\\static\\upload'
}