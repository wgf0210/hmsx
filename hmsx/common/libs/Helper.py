from flask import g,render_template

# 自定义渲染方法
def ops_render(template,context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template,**context)