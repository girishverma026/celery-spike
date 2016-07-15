from celery_app import app
from ibuilder import sub_build
from celery import chain

@app.task
def add(x, y):
	return x + y


@app.task
def mul(x, y):
	return x * y


@app.task
def build_insight():
	print 'running build insight'
	(sub_build.si() | sub_build.si()).delay()

