# Official Accounts automatic reply
## 0.前言
起源于对公众号自动回复的需求，发现官方的自动回复数据只可以添加5条，而我希望在更多的数据中随机选择回复，平时接触代码较少，现学现卖
## 1.实现功能
用户对公众号发送“吃什么”，后台从menu.txt（文件中每行一个菜名）随机选取一个菜名，进行回复
![avatar](/images/menu.png)
## 2.运行环境
python2.7  
web.py
## 3.运行方式
暂未加入后台运行和输出日志文件功能
````
nohup python main.py 80 > log.txt &
````
## 4.文件描述
main.py receive.py（接收脚本） reply.py（回复脚本）  
照搬微信官方手册  
handle.py（处理脚本）  
根据需求修改，随机实现代码如下
````python
a = len(open('menu.txt','rU').readlines())#读取菜单行数
num = random.randint(0, a-1)#以行数随机选取数字，注意要减1
fileName = 'menu.txt'
with open(fileName,'r') as f:
    lines = f.readlines( )
content = lines[num].strip("\n")#将随机行的内容读取，去除换行输出
````
## 5.后续完善计划
- [ ] 脚本执行为后台运行
- [ ] 日志输出，按启动时间
- [ ] 对用户发送内容判断灵活
## 6.遇到的问题
1.微信对接配置的接口路径要写完整  
2.公众号开发模式默认禁用，要启用  
3.py的格式需严格遵守，使用sublime统一调整  
4.注意数据的类型转化  
