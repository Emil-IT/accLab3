from flask import Flask
from flask_celery import make_celery
from os import environ
import count_words

flask_app = Flask(__name__)
flask_app.config['CELERY_BROKER_URL']='amqp://localhost//'
flask_app.config['CELERY_BACKEND']='rpc://'

celery_app = make_celery(flask_app)

@flask_app.route('/api/countPronouns')
def count():
	return (str(countPronouns.delay().wait())+'\n')

@flask_app.route('/api/add/')
def hello():
	print('Hello World!')
	result = add_numbers.delay(2,5)
	return (str(result.wait())+ '\n')

@celery_app.task(name='tasks.add')
def add_numbers(x, y):
	return x + y

@celery_app.task(name='task.countPronouns')
def countPronouns():
	return count_words.countPronouns()


if __name__ == '__main__':
	flask_app.run(host='0.0.0.0', debug=True)
