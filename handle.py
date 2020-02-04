# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import reply
import receive
import web
import re
import random

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "**"#填写公众号token 
			
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData#后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == '吃什么':#判断是否为文本和制定文字，后续优化
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                a= len(open('menu.txt','rU').readlines())#读取菜单行数
                print(a)
                b= int(a)
                num = random.randint(0, b-1)#以行数随机选取数字，主要要减1
                print(num)
                fileName = 'menu.txt'
                with open(fileName,'r') as f:
                    lines = f.readlines( )
                print lines[num].strip("\n")
                content = lines[num].strip("\n")#将随机行的内容读取，去除换行输出
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment