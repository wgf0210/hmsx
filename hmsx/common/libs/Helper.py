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

# 自定义分页操作
def ipagenation(params):
    import math
    ret = {
        'is_prev':True,
        'is_next':True,
        'from':0,
        'end':0,
        'current':0,
        'total_pages':0,
        'page_size':0,
        'total':0,
        'url':params['url']
    }
    total = int(params['total'])
    page_size = int(params['page_size'])
    page = int(params['page'])
    # 向下取整
    total_pages = int(math.ceil(total/page_size))
    if page <= 1:
        ret['is_prev'] = False
    if page >= total_pages:
        ret['is_next'] = False
    ret['from'] = 1
    ret['end'] = total_pages
    ret['current'] = page
    ret['total_pages'] = total_pages
    ret['total'] = total
    # 分页核心：生成器，页数的范围
    ret['range'] = range(ret['from'],ret['end']+1)
    ret['page_size'] = page_size

    return ret