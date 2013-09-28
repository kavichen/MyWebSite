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
  if message.content=='陈琦威'.decode('utf-8'):
      reply=TextReply(message = message, content = 'jianren')
      return reply
  elif message.content == 'x':
      reply=ArticlesReply(message=message)
      article1 = Article(
          title="mm",
          description="test",
          img="http://ww4.sinaimg.cn/large/5f581355gw1e91zrosf3sj20c10ezt9z.jpg",
          url="http://ww4.sinaimg.cn/large/5f581355gw1e91zrosf3sj20c10ezt9z.jpg"
      )
      article2 = Article(
          title = "mm2",
          description = "test2",
          img="http://ww2.sinaimg.cn/large/5f581355gw1e9203prwxuj20d50jxt9u.jpg",
          url="http://ww2.sinaimg.cn/large/5f581355gw1e9203prwxuj20d50jxt9u.jpg"
      )
      reply.add_article(article1,article2)
      return reply
  else:
      return message.content

@robot.image
def echo(message):
  return '图片'
robot.run()
