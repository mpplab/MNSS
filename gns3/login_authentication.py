# -*- coding: utf-8 -*-
from urllib import request,parse
import json
from gns3.globalvar import GlobalVar

class user(object):

    def login_mark(self,username,password):
        url = r'http://118.190.159.129/app/login'
        req = request.Request(url)
        date = {'account':username,'userPassword':password,'loginFromSystem': 'mnss'}
        data = parse.urlencode(date).encode('utf-8')
        html = request.urlopen(req,data=data).read().decode('utf-8')
        result = json.loads(html)
        GlobalVar.name = result['entity']['nickName']
        GlobalVar.headportrait = GlobalVar.headportrait + result['entity']['picPath']
        return result['success']