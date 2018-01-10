# -*- coding: utf-8 -*-
#Author：yrf
#利用capitalize和map函数实现首字母大写，其余小写
def f(x):
	x=x.capitalize()
	return x
r=map(f,['ASD','BBB','SSS','DSA','SDA'])
print (list(r))
