# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets  
from PyQt5.QtWidgets import QFileDialog 
from ftplib import FTP 
from gns3.globalvar import GlobalVar
import urllib.request
from gns3.ui.Avatar_ui import Ui_Avatar
from PyQt5.QtWidgets import QMessageBox
from PIL import Image
import os.path
import glob

class Avatar(QDialog, Ui_Avatar):
    path = ""
    def __init__(self, parent=None):
        super(Avatar, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_3.clicked.connect(self.on_pushButton_3_clicked)
        self.pushButton_4.clicked.connect(self.on_pushButton_4_clicked)
        if GlobalVar.imagepath == "":
            pass
        else:
            imagepath = urllib.request.pathname2url(GlobalVar.imagepath) 
            realpath = imagepath[3:]
            self.frame.setStyleSheet("border-image: url({});".format(realpath))

    def on_pushButton_clicked(self):
        fileName = QFileDialog.getOpenFileName(self,  
                                    "打开",  
                                    "C:/",  
                                    "Image Files (*.jpg;*.png;*.gif)") 
        path = list(fileName)[0]
        imagepath1 = urllib.request.pathname2url(path) 
        Avatar.path = imagepath1[3:]
        self.frame.setStyleSheet("border-image: url({});".format(Avatar.path))

    def on_pushButton_3_clicked(self):
        if self.path == "":
            QMessageBox.information(self,u'提示',u'请选择图片',QMessageBox.Yes )
        else:
            ftp = FTP()
            ftp.connect("139.196.202.32",428)
            ftp.login("{}".format(GlobalVar.userid),"{}".format(GlobalVar.password))
            ftp.encoding = 'UTF-8'
            mark = False
            while mark == False:
                if 'image' in ftp.nlst():
                    ftp.cwd('image')
                    bufsize=1024
                    filename = os.path.basename(self.path)
                    fp = open(Avatar.path,'rb')
                    ftp.storbinary('STOR ' + filename ,fp,bufsize)
                    fp.close()
                    mark = True
                else:
                    ftp.mkd('image')
            ftp.quit()
            os.chdir(GlobalVar.workpath)
            os.chdir("{}/image".format(GlobalVar.userid1))
            savepath = os.path.join(GlobalVar.workpath,"{}/image".format(GlobalVar.userid1))
            for jpgfile in glob.glob("{}".format(Avatar.path)):
                Avatar.convertjpg(0,jpgfile,savepath)
            QMessageBox.information(self,u'提示',u'上传成功',QMessageBox.Yes )
            a = os.path.basename(Avatar.path)
            dictdata = {'imagename':a}
            GlobalVar.imagename = a
            GlobalVar.setuserinfo(0, GlobalVar.userid, dictdata)
            GlobalVar.createfolder(0)
            self.reject()
            
    def on_pushButton_4_clicked(self):
        self.reject()
        
    def convertjpg(self,jpgfile,outdir,width=80,height=80):
        img=Image.open(jpgfile)   
        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    dialog = Avatar(main)
    dialog.show()
    exit_code = app.exec_()
