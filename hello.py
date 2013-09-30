#coding=utf-8
import werobot
from werobot.reply import ArticlesReply, Article,TextReply
import random
from werobot.session.mongodbstorage import MongoDBStorage
import pymongo

#robot = werobot.WeRoBot(token='kavichen',enable_session=True)
#robot = werobot.WeRoBot(token='kavichen')
collection = pymongo.MongoClient()["wechat"]["session"]
session_storage = MongoDBStorage(collection)
robot = werobot.WeRoBot(token='kavichen',enable_session=True,session_storage = session_storage)

#@robot.text
#def hello(message,session):
#    count = session.get("count",0)+1
#    session["count"]=count
#    return "%s" % count



@robot.subscribe
def subscribe(message):
    return '哈哈，多谢你的关注，目前小爷还在开发这个站，更多功能敬请期待啊啊啊啊啊！回复「X」，满满的福利！'

@robot.location
def echo(message):
    return '有本事站在原地不要离开，分分钟找人来砍死你！'

@robot.text
def echo(message,session):
    if message.content == 't' or message.content == 'T':
        id = message.source
        count = session.get("count",0)
        #se = session_storage[id]
        #session = session_storage[id]
        #s = '%id\'s seesion is %s' %id %session
        return 'count'
    elif message.content == 'a' or message.content == 'A':
        return 'ok'

#@robot.text
#def echo(message,session):
#    #if message.content == 'a' or message.content == 'A':
#    #    count = session.get("count",0)+1
#    #    session["count"] = count
#    #    return "%s" %count
#    if message.content == 'x' or message.content == 'X':
#        count = session.get("count",0)+1
#        session["count"]=count
#        img_num = random.randint(1,3869)
#        reply=ArticlesReply(message=message)
#        if count <= 1000:
#            article = Article(
#                title="妹子",
#                description="第%s号妹子" % img_num,
#                img="http://chenqiwei.com/image/jiandan/%i.jpg" % img_num,
#                url="http://chenqiwei.com/image/jiandan/%i.jpg" % img_num
#            )
#            reply.add_article(article)
#            return reply
#        else:
#            return '看那么多次啊你！'
    #############################################
    #elif len(message.content.decode('utf-8'))>3:
    #    return 'c'
        #split_word = list(message.content.decode('utf-8'))
        #if split_word[-2] == '天'.decode('utf-8') and split_word[-1] == '气'.decode('utf-8'):
        #    word_len = len(message.content.decode('utf-8'))
        #    city_name_list = split_word[0:word_len-2]
        #    city_name = "".join(itertools.chain(*city_name_list))
        #    return city_name
    #############################################
    #elif message.content=='陈琦威'.decode('utf-8'):
    #    reply=TextReply(message = message, content = '贱人')
    #    return reply
    #else:
    #    return '输入 X 啊'

@robot.image
def echo(message):
    return '是你的裸照吗？'
robot.run()
