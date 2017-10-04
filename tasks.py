from flask import Flask
from flask_celery import make_celery

flask_app = Flask(__name__)
flask_app.config['CELERY_BROKER_URL']='amqp://localhost//'
flask_app.config['CELERY_BACKEND']='rpc://'

celery = make_celery(flask_app)

@flask_app.route('/hello/')
def hello():
	print('Recieved message')
	add.delay(2,5)
	return 'Request sent'

@celery.task(name='tasks.add')
def add(x, y):
	return x + y
if __name__ == '__main__':
	flask_app.run(debug=True)
