from ftplib import FTP
import urllib
import json
import os
class GlobalVar: 
    ftp = FTP()
    ftp.connect("139.196.202.32",428)
    ftp.login("gns3@163.com","gns3**")
    Gdictionary = {}
    Gdictionaryson = []
    ftp.cwd("MGNS")
    b = ftp.nlst()
    for a in b:
        ftp.cwd("{}".format(a))
        Gdictionaryson = ftp.nlst()
        Gdictionary["{}".format(a)] = Gdictionaryson
        ftp.cwd('/MGNS/')
    globalvarmark = 1
    workpath = ""
    uploadpath = ""
    loginmark = False
    userid = ""
    userid1 = ""
    password = ""
    dictuser = {}
    ismodified = 0
    imagepath = ""
    imagename = ""
    
    def getuserismodified(self,userid):
        url = "http://139.196.202.32:8080/secbox/getGNS3UserInfo"
        postdata =urllib.parse.urlencode({    
         "userid":"{}".format(userid)}).encode('utf-8')
        header = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding":"utf-8",
        "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "Host":"c.highpin.cn",
        "Referer":"http://c.highpin.cn/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
        }
        req = urllib.request.Request(url,postdata,header)
        page = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(page)
        return data['ismodified']
    
    def getuserinfo(self,userid):
        url = "http://139.196.202.32:8080/secbox/getGNS3UserInfo"
        postdata =urllib.parse.urlencode({    
         "userid":"{}".format(userid)
        }).encode('utf-8')
        header = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding":"utf-8",
        "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "Host":"c.highpin.cn",
        "Referer":"http://c.highpin.cn/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
        }
        req = urllib.request.Request(url,postdata,header)
        page = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(page)
        return data['userdata']
    
    def getuserinuse(self,userid):
        url = "http://139.196.202.32:8080/secbox/getInUseAction"
        postdata =urllib.parse.urlencode({    
         "userid":"{}".format(userid)
        }).encode('utf-8')
        header = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding":"utf-8",
        "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "Host":"c.highpin.cn",
        "Referer":"http://c.highpin.cn/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
        }
        req = urllib.request.Request(url,postdata,header)
        page = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(page)
        return data['inuse'][:-1]
    
    def setuserinfo(self,userid,dictdata):
        url = "http://139.196.202.32:8080/secbox/setGNS3UserInfo"
        dictuser = {"userid":"{}".format(userid),'username': '', 'sex': 0, 'workplace': '', 'location': '', 'profession': '', 'email': '', 'age': 0,"imagename":GlobalVar.imagename}
        dictuser.update(dictdata)
        postdata =urllib.parse.urlencode(dictuser).encode('utf-8')
        header = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding":"utf-8",
        "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "Host":"c.highpin.cn",
        "Referer":"http://c.highpin.cn/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
        }
        req = urllib.request.Request(url,postdata,header)
        page = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(page)
        return data['ret']
        
    def denlu(self,userid,password):
        url = "http://139.196.202.32:8080/secbox/loginAction"
        postdata =urllib.parse.urlencode({    
        "username":userid,
        "pswd":password,
        }).encode('utf-8')
        header = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding":"utf-8",
        "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "Host":"c.highpin.cn",
        "Referer":"http://c.highpin.cn/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
        }
        req = urllib.request.Request(url,postdata,header)
        page = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(page)
        return data['ret']
    
    def createfolder(self):
        try:
            os.chdir(GlobalVar.workpath)
            os.mkdir("{}".format(GlobalVar.userid1))
            os.chdir("{}".format(GlobalVar.userid1))
            os.mkdir("image")
        except Exception as e: 
            os.chdir(GlobalVar.workpath)
            os.chdir("{}/image".format(GlobalVar.userid1))
            try:
                GlobalVar.imagepath = os.path.join(os.getcwd(),GlobalVar.imagename)
                if os.path.exists(GlobalVar.imagename):
                    pass
                else:
                    ftp = FTP()
                    ftp.connect("139.196.202.32",428)
                    ftp.login("{}".format(GlobalVar.userid),"{}".format(GlobalVar.password))
                    ftp.encoding = 'UTF-8'
                    ftp.cwd('image')
                    bufsize = 1024
                    filename = GlobalVar.imagename
                    file_handle = open(filename,"wb").write
                    ftp.retrbinary('RETR ' +  filename,file_handle,bufsize)
                    ftp.quit()   
            except Exception as e: 
                print(e)
                