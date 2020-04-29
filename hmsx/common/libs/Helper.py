from flask import g,render_template
import datetime

# 自定义渲染方法
def ops_render(template,context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template,**context)

# 自定义时间格式化方法（获取当前时间并格式化）
def getcurrentdate(): 
    return datetime.datetime.now()