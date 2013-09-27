#coding=utf-8
import werobot

robot = werobot.WeRoBot(token='kavichen')

@robot.handler
def echo(message):
  return 'Hello World!'

@robot.subscribe
def subscribe(message):
  return '关注'

@robot.
robot.run()
