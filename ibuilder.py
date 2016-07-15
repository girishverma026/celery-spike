from celery_app import app

@app.task
def sub_build():
	print 'running sub build'