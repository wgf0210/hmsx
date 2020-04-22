from flask import Flask
from flask_script import Manager
import os

# 修改Flask类
class Application(Flask):
    def __init__(self,import_name,template_folder=None,root_path=None,static_folder=None):
        super(Application,self).__init__(import_name=import_name,template_folder=template_folder,root_path=root_path,static_folder=static_folder)

app = Application(__name__,template_folder=os.getcwd()+'/web/templates',root_path=os.getcwd(),static_folder=os.getcwd()+'/web/static')
manager = Manager(app)

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '123'

# app.run()