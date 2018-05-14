from ftplib import FTP
import os

class GlobalVar(object):
    totalLocalConfig = None
    totalserverpath = {}
    area = None
    subthreadinglist = {}
    progressbarlist = []
    downloadurl = 'http://124.167.223.254:2001'
    downloadobjectlist = []
    downloadurllist = {}
    nowurllist = set()
    name = ''
    headportrait = 'http://118.190.159.129:8062'
    settings = {}
    section = ""
    routerTemplet = {}
    ftppath = ['router','switch','client','server','his','lis','pacs','security']
    path = ''

    loginmark = False
    dictionary = {}
    globalmarket = 0
    routersection = 'Dynamips'


# Templet example
    routerTemplet = {}
    vmTemplet = {}
    pixTemplet = {}
    switchTemplet = {}

    test = {
        "allocate_aux_console_ports": False,
        "dynamips_path": "E:\\\u82f1\u96c4\u65f6\u523b\\first\\gns3\\GNS3\\dynamips\\dynamips.exe",
        "ghost_ios_support": True,
        "mmap_support": True,
        "routers": [
            {
                "auto_delete_disks": True,
                "category": 0,
                "chassis": "",
                "default_name_format": "R{0}",
                "disk0": 0,
                "disk1": 0,
                "exec_area": 64,
                "idlemax": 500,
                "idlepc": "",
                "idlesleep": 30,
                "image": "c7200-is-mz.123-22.bin",
                "mac_addr": "",
                "midplane": "vxr",
                "mmap": True,
                "name": "c7200",
                "npe": "npe-400",
                "nvram": 512,
                "platform": "c7200",
                "private_config": "",
                "ram": 512,
                "server": "local",
                "slot0": "C7200-IO-FE",
                "slot1": "",
                "slot2": "",
                "slot3": "",
                "slot4": "",
                "slot5": "",
                "slot6": "",
                "sparsemem": True,
                "startup_config": "C:\\Users\\huangyihe\\GNS3\\configs\\ios_base_startup-config.txt",
                "symbol": ":/symbols/router.svg",
                "system_id": "FTX0945W0MY"
            }
        ],
        "sparse_memory_support": True,
        "use_local_server": True
    }

    def ftplogin(self):
        ftp = FTP()
        ftp.connect("124.167.223.254", 2021)
        ftp.login('mnss','asdf1234*123')
        return ftp

    def getdict(self):
        ftp = self.ftplogin()
        for i in self.ftppath:
            self.dictionary[i] = {}
            ftp.cwd('/{}/'.format(i))
            try:
                for j in ftp.nlst():
                    self.dictionary[i][j] = ftp.size(j)
            except Exception as e:
                self.dictionary[i] = {}
            finally:
                pass
        ftp.quit()

    def savedownload(self):
        with open('download.txt','w') as f:
            for i in GlobalVar.downloadobjectlist:
                GlobalVar.downloadurllist[i.url] = i.size
            f.write(str(GlobalVar.downloadurllist))

    def quitdownload(self):
        with open('download.txt','w') as f:
            for i in GlobalVar.downloadobjectlist:
                GlobalVar.downloadurllist[i.url] = i.total
            f.write(str(GlobalVar.downloadurllist))

    def getpath(self):
        return os.path.join(GlobalVar.totalserverpath['local_server']['images_path'],'IOS')