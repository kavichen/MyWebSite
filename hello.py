#coding=utf-8
import werobot
from werobot.reply import ArticlesReply, Article,TextReply
import random

robot = werobot.WeRoBot(token='kavichen')

#@robot.handler
#def echo(message):
  #return 'Hello World!'

@robot.subscribe
def subscribe(message):
  return '哈哈，多谢你的关注，目前我还在开发这个站，更多功能敬请期待啊啊啊啊啊！'

@robot.location
def echo(message):
    return '是坐标！你给我等着，分分钟来砍死你！'

@robot.text
def echo(message):
  if message.content=='陈琦威'.decode('utf-8'):
      reply=TextReply(message = message, content = 'jianren')
      return reply
  elif message.content == 'x' or message.content == 'X':
      img_num = random.randint(1,3869)
      reply=ArticlesReply(message=message)
      article = Article(
          title="妹子",
          description="第%s号妹子" % img_num,
          img="http://chenqiwei.com/image/jiandan/%i.jpg" % img_num,
          url="http://chenqiwei.com/image/jiandan/%i.jpg" % img_num
      )
      #article2 = Article(
      #    title = "mm2",
      #    description = "test2",
      #    img="http://ww2.sinaimg.cn/large/5f581355gw1e9203prwxuj20d50jxt9u.jpg",
      #    url="http://ww2.sinaimg.cn/large/5f581355gw1e9203prwxuj20d50jxt9u.jpg"
      #)
      reply.add_article(article)
      #reply.add_article(article2)
      return reply
  else:
      return message.content

@robot.image
def echo(message):
  return '图片'
robot.run()
