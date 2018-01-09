# -*- coding: utf-8 -*- 
import crypt
import hashlib
a="//asd/."
var=hashlib.sha512(a.encode('utf-8'))
print (var.hexdigest())


