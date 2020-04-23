import time

class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        ver = '%s'%(int(time.time()))
        path = '/static'+path+'?version'+ver
        return UrlManager.buildUrl(path)

    @staticmethod
    def buildImageUrl(path):
        pass