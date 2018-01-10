# -*- coding: utf-8 -*-
#Author：yrf
#利用基础循环实现首字母大写，其余小写
def f(x):
	x=map(ord,x)
	t=list(x)
	d=[]
	b=1
	for i in t:
		if b == 1:
			if i >= 97:
				i=i-32
				i=chr(i)
				d.append(i)
				b=b+1
			else:
				i=chr(i)
				d.append(i)
				b=b+1
		else:
			if i < 97:
				i=i+32
				i=chr(i)
				d.append(i)
				b=b+1
			else:
				i=chr(i)
				d.append(i)
				b=b+1
			
	d=''.join(d)
	return d
r=map(f,['ASD','Zvbnz','zSZ','DaA','ScA','ass'])
print (list(r))
