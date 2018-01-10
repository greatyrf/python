# -*- coding: utf-8 -*-
#Author：yrf
#利用crypt生成哈希sha512加密密码
import crypt
import hashlib
a="//asd/."
var=hashlib.sha512(a.encode('utf-8'))
print (var.hexdigest())


