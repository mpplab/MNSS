import os
from gns3.globalvar import GlobalVar

class get(object):
    def __init__(self):
        self.routersettings = GlobalVar.totalLocalConfig['Dynamips']
        print(self.routersettings)
    # router Templet example
    c7200templet = {
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
        "image": "",
        "mac_addr": "",
        "midplane": "vxr",
        "mmap": True,
        "name": "",
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
        "startup_config": '',
        "symbol": ":/symbols/router.svg",
        "system_id": "FTX0945W0MY",
    }
    c3660templet = {
        "auto_delete_disks": True,
        "category": 0,
        "chassis": "3660",
        "default_name_format": "R{0}",
        "disk0": 0,
        "disk1": 0,
        "exec_area": 64,
        "idlemax": 500,
        "idlepc": "",
        "idlesleep": 30,
        "image": "",
        "iomem": 5,
        "mac_addr": "",
        "mmap": True,
        "name": "",
        "nvram": 256,
        "platform": "c3600",
        "private_config": "",
        "ram": 192,
        "server": "local",
        "slot0": "Leopard-2FE",
        "slot1": "",
        "slot2": "",
        "slot3": "",
        "slot4": "",
        "slot5": "",
        "slot6": "",
        "sparsemem": True,
        "startup_config": '',
        "symbol": ":/symbols/router.svg",
        "system_id": "FTX0945W0MY"
    }
    c3640templet = {
        "auto_delete_disks": True,
        "category": 0,
        "chassis": "3640",
        "default_name_format": "R{0}",
        "disk0": 0,
        "disk1": 0,
        "exec_area": 64,
        "idlemax": 500,
        "idlepc": "",
        "idlesleep": 30,
        "image": "",
        "iomem": 5,
        "mac_addr": "",
        "mmap": True,
        "name": "",
        "nvram": 256,
        "platform": "c3600",
        "private_config": "",
        "ram": 192,
        "server": "local",
        "slot0": "",
        "slot1": "",
        "slot2": "",
        "slot3": "",
        "sparsemem": True,
        "startup_config": '',
        "symbol": ":/symbols/router.svg",
        "system_id": "FTX0945W0MY"
    }
    c3620templet = {
        "auto_delete_disks": True,
        "category": 0,
        "chassis": "3620",
        "default_name_format": "R{0}",
        "disk0": 0,
        "disk1": 0,
        "exec_area": 64,
        "idlemax": 500,
        "idlepc": "",
        "idlesleep": 30,
        "image": "",
        "iomem": 5,
        "mac_addr": "",
        "mmap": True,
        "name": "",
        "nvram": 256,
        "platform": "c3600",
        "private_config": "",
        "ram": 192,
        "server": "local",
        "slot0": "",
        "slot1": "",
        "sparsemem": True,
        "startup_config": '',
        "symbol": ":/symbols/router.svg",
        "system_id": "FTX0945W0MY"
    }

    def getRouterTemplet(self,imagename):

        temp = {}
        print(imagename)
        print('get')
        if 'c7200' in imagename:
            print('1')
            temp = self.c7200templet
        elif 'c3660' in imagename:
            temp = self.c3660templet
        elif 'c3640' in imagename:
            temp = self.c3640templet
        elif 'c3620' in imagename:
            temp = self.c3620templet
        else:
            pass
        temp['startup_config'] = os.path.join(GlobalVar.totalserverpath["configs_path"],'ios_base_startup-config.txt')
        temp["image"] = imagename
        temp["name"] = imagename[:-4]
        print(self.routersettings)
        self.routersettings['routers'].append(temp)
        print(self.routersettings)
        return self.routersettings


