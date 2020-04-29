import hashlib,base64,random,string

class Userservice():
    # 生成密码（集合pwd和salt）
    @staticmethod
    def generatepwd(pwd,salt):
        m = hashlib.md5()
        str = '%s-%s'%(base64.encodebytes(pwd.encode('utf-8')),salt)
        m.update(str.encode('utf-8'))

        return m.hexdigest()

    @staticmethod
    def generateAuthCode(user_info=None):
        m = hashlib.md5()
        str = '%s-%s-%s-%s'%(user_info.uid,user_info.login_name,user_info.login_pwd,user_info.login_salt)
        m.update(str.encode('utf-8'))

        return m.hexdigest()

    # 生成一个只包含大小写字母和数字的16位加密字符串
    # random  string.ascii_letters(大小写字母)  string.digits(0-9数字)
    @staticmethod
    def generateSalt(length=16):
        # list = []
        # for i in range(16):
        #     item = random.choice((string.ascii_letters + string.digits))
        #     list.append(item)
        # 列表生成式
        list = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        print(list)
        return (''.join(list))