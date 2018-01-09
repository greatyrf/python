#python test
#首字母大写，其余小写
from functools import reduce
def f(x):
	x=x.capitalize()
	return x
r=map(f,['ASD','BBB','SSS','DSA','SDA'])
print (list(r))
