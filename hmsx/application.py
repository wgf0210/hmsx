from flask import Flask
from flask_script import Manager
import os

# 修改Flask类
class Application(Flask):
    def __init__(self,import_name,template_folder=None,root_path=None,static_folder=None):
        super(Application,self).__init__(import_name=import_name,template_folder=template_folder,root_path=root_path,static_folder=static_folder)

app = Application(__name__,template_folder=os.getcwd()+'/web/templates',root_path=os.getcwd(),static_folder=os.getcwd()+'/web/static')
manager = Manager(app)

# 函数模板
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildUrl,'buildUrl')
app.add_template_global(UrlManager.buildStaticUrl,'buildStaticUrl')
app.add_template_global(UrlManager.buildImageUrl,'buildImageUrl')

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '123'

# app.run()