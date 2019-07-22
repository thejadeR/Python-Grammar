# python--数据类型bytes
# 在Python3以后，字符串和bytes类型彻底分开了。字符串是以字符为单位进行处理的，bytes类型是以字节为单位处理的。

# bytes数据类型在所有的操作和使用甚至内置方法上和字符串数据类型基本一样，也是不可变的序列对象。

# bytes对象只负责以二进制字节序列的形式记录所需记录的对象，至于该对象到底表示什么（比如到底是什么字符）则由相应的编码格式解码所决定。
# Python3中，bytes通常用于网络数据传输、二进制图片和文件的保存等等。
# 可以通过调用bytes()生成bytes实例，其值形式为 b'xxxxx'，其中 'xxxxx' 为一至多个转义的十六进制字符串（单个 x 的形式为：\x12，其中\x为小写的十六进制转义字符，12为二位十六进制数）组成的序列，
# 每个十六进制数代表一个字节（八位二进制数，取值范围0-255），对于同一个字符串如果采用不同的编码方式生成bytes对象，就会形成不同的值.

# b = b''         # 创建一个空的bytes
# b = byte()      # 创建一个空的bytes
# b = b'hello'    #  直接指定这个hello是bytes类型
# b = bytes('string',encoding='编码类型')  #利用内置bytes方法，将字符串转换为指定编码的bytes
# b = str.encode('编码类型')   # 利用字符串的encode方法编码成bytes，默认为utf-8类型

# bytes.decode('编码类型')：将bytes对象解码成字符串，默认使用utf-8进行解码。

# 对于bytes，我们只要知道在Python3中某些场合下强制使用，以及它和字符串类型之间的互相转换，其它的基本照抄字符串。
# 简单的省事模式：
# string = b'xxxxxx'.decode() 直接以默认的utf-8编码解码bytes成string
# b = string.encode() 直接以默认的utf-8编码string为bytes

# 【例子】
import re
import subprocess

P = subprocess.Popen('/sbin/ifconfig',stdout=subprocess.PIPE)

# 因为shell进程返回的结果给python管道对象的是bytes数据类型，所以切割和用正则匹配都要用bytes格式，当然也可以直接在最开始的时候就解码成字符串数据类型
res = re.search(rb'\d+\.\d+\.\d+\.\d+', P.stdout.read().split(b"\n")[1]).group()
print(res, type(res))

# 使用utf-8解码bytes类型数据
print(res.decode('utf-8'))



import subprocess
import re
p = subprocess.Popen('sleep 2;ifconfig',stdout=subprocess.PIPE,shell=True)
print("p:",p.stdout)
res = re.search(rb'\d+\.\d+\.\d+\.\d+', p.stdout.read().split(b"\n")[1]).group()
print(res, type(res))
print(res.decode('utf-8'),type(res.decode('utf-8')))


# 使用什么标准编码的，就用什么标准解码，数据类型和编码是两个不同的概念
# str1 = "afaff".encode("utf-16")
# print(type(str1)) # <class 'bytes'>
# print(str1.decode("gbk"))  #UnicodeDecodeError: 'gbk' codec can't decode byte 0xff in position 0: illegal multibyte sequence
# print(str1.decode("utf-16")) # afaff

# 把数据转成bytes类型，并使用”utf-8“编码
# str2 = bytes("你好世界","utf-8")
# print(type(str2),str2)  # <class 'bytes'> b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\x96\xe7\x95\x8c'

# bytes对象自带有解码成字符串的功能，默认解码规则是”utf-8“
# print(type(str2.decode()),str2.decode())  #<class 'str'> 你好世界