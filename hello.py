import werobot

robot = werobot.WeRoBot(token='kavichen')

@robot.handler
def echo(message):
    return 'Hello World!'

@robot.subscribe
def subscribe(message):
	return 'guanzhu'

robot.run()
