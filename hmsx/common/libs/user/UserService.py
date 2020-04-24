import hashlib,base64

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