import subprocess
# subprocess模块是python从2.4版本开始引入的模块。主要用来取代 一些旧的模块方法，如os.system、os.spawn*、os.popen*、commands.*等。
# subprocess通过子进程来执行外部指令，并通过input/output/error管道，获取子进程的执行的返回信息。
# 常用方法：
# 【1】
# subprocess.call()：执行命令或终端语句，并返回执行状态码(不是结果,0为成功，1为程序有异常)，其中shell参数为False时，命令需要通过列表的方式传入，当shell为True时，可直接传入命令
# 如;
# subprocess.call(['ls','-l'],shell=False)
# subprocess.call('ls -l',shell=True)
# res = subprocess.call("python test.py",shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# print(res)


# 【2】
# subprocess.popen()
# 例子：
# res = subprocess.popen('ifconfig | grep 192',shell=True)
# res
# <subprocess.popen object at ox7f2131a>
# res.stdout.read()读不出来
# 要读出来要先输出到标准输出里，先存到管道PIPE 再给stdout python和shell是两个进程不能独立通信，必须通过操作系统提供的管道
# 用管道可以把结果存到stdin stdout stderr
# subprocess.popen('ifconfig | grep 192',shell=True,stdout=subprocess.PIPE)
# res.stdout.read()   #就可以读出来了
# subprocess.popen('ifconfig | gr1111ep 192',shell=True,stdout=subprocess.PIPE)

# 出错会直接打印错误。想不打印错误可以stderr保存stderr=subprocess.PIPE
# poll() check if child process has terminated. returns returncode
# ---------

# res=subprocess.popen("sleep 10;echo 'hello'", shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# 执行的时候没反应，不知道是卡主了还是执行完了

# 每次调subprocess执行Linux命令，都相当于启动了一个新的shell，启动新的进程，执行一次命令等结果
# 如果该命令要花半小时，不知道是卡主了还是执行完了，可以res.poll()返回none表示还没有执行完，返回0表示执行完了
# res.wait()等待结束然后返回0


# res = subprocess.Popen("python test.py",shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# the_out = res.stdout.read().decode()
#
# print(the_out)