import hashlib,base64

class Userservice():
    # 生成密码（集合pwd和salt）
    @staticmethod
    def generatepwd(pwd,salt):
        m = hashlib.md5()
        str = '%s-%s'%(base64.encodebytes(pwd.encode('utf-8')),salt)
        m.update(str.encode('utf-8'))

        return m.hexdigest()