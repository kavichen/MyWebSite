#coding=utf-8
import werobot
from werobot.reply import ArticlesReply, Article,TextReply

robot = werobot.WeRoBot(token='kavichen')

#@robot.handler
#def echo(message):
  #return 'Hello World!'

@robot.subscribe
def subscribe(message):
  return '哈哈，多谢你的关注，目前我还在开发这个站，更多功能敬请期待啊啊啊啊啊！'

@robot.location
def echo(message):
    return '地址'

@robot.text
def echo(message):
  if message.content == '张凌一':
      reply=TextReply(message = message, content = 'hello')
      return reply
  else:
      return 'Bye'

@robot.image
def echo(message):
  return '图片'
robot.run()
