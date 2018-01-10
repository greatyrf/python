# -*- coding: utf-8 -*-
#Author：yrf
#利用pexpect实现交互式ssh登录以及运行命令
import pexpect
PROMPT=['#','>>>','\$','>']
def send_command(child, cmd):
	child.sendline(cmd)
	child.expect(PROMPT)
	print (child.before)
def connect(user, host, password, port):
	ssh_key='Are you sure you want to continue connecting'
	connStr='ssh '+user+'@'+host+' -p '+port
	child=pexpect.spawn(connStr)
	ret=child.expect([pexpect.TIMEOUT, ssh_key, '[P|p]assword:'])
	if ret == 0:
		print ('error conneting')
		return
	if ret == 1:
		child.sendline('yes')
		ret =child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
	if ret == 0:
		print ('error conneting')
		return
	child.sendline(password)
	child.expect(PROMPT)
	return child
def main():
	host='10.200.70.132'
	user='root'
	password=''
	port='52000'
	child=connect(user,host,password,port)
	send_command(child,'ls -al /usr/local/nginx/conf/vhost/')
main()

