# -*- coding: utf-8 -*-
#Author：yrf
#利用zipfile实现zip加密包的解密以及解压
import zipfile
import os
from threading import Thread
def extractfile(zFile,password):
	try:
		zFile.extractall(pwd=password)
		passowrd=str(password)
		print ('The password = %s' %(password) )
	except Exception as e:
		pass
def main():
	zFile = zipfile.ZipFile("test.zip")
	passfile=open('dt.txt','r')
	for line in passfile.readlines():
		password=line.strip('\n')
		password=password.encode('utf-8')
		t=Thread(target=extractfile,args=(zFile,password))
		t.start()
main()
	
