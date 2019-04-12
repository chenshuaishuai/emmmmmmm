import os
import sys

from django.conf import settings

DEBUG = os.environ.get('DEBUG','on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY','''os.urandom(32)''' '{{ secret_key }}')	#DEBUG and SECRET_KEY may be changes in different environment
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS','localhost').split(',')	#the 'localhost' stand must input 'localhost:8000',you can choice '127.0.0.1'

settings.configure(
	#DEBUG=True,
	#SECRET_KEY='thisisthesecretkey',
	DEBUG=DEBUG,
	SECRET_KEY=SECRET_KEY,
	ALLOWED_HOSTS=ALLOWED_HOSTS,
	ROOT_URLCONF=__name__,
	MIDDLEWARE_CLASSES=(
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
		'django.middleware.clickjacking.XFrameOptionsMiddleware',
	),
)

from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application	#use 'get_wsgi_application' get the API whit wsgi

application = get_wsgi_application()

def index(request):
	return  HttpResponse('Hello world')

urlpatterns = (
	url(r'^$',index),
)

if __name__ == '__main__':
	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
