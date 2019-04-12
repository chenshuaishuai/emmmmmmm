import os
import hashlib
import sys
from django import forms
from django.conf.urls import url
from io import BytesIO
from PIL import Image,ImageDraw
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse,HttpResponseBadRequest
from django.core.cache import cache
from django.core.wsgi import get_wsgi_application	#use 'get_wsgi_application' get the API whit wsgi
from django.views.decorators.http import etag

DEBUG = os.environ.get('DEBUG','on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY','''os.urandom(32)''' '-*duu6j_1so*dk-ojzc$pigosbgvcf$v#m6pkkjgts@=o_dip&')	#DEBUG and SECRET_KEY may be changes in different environment
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

application = get_wsgi_application()

class ImageForm(forms.Form):
	height = forms.IntegerField(min_value=1,max_value=2000)
	width = forms.IntegerField(min_value=1,max_value=2000)

	def generate(self,image_format='PNG'):
		'''Generate an image of the given type and return as raw bytes.'''
		height = self.cleaned_data['height']
		width = self.cleaned_data['width']
		key = '{}.{}.{}'.format(width,height,image_format)	#allow this picture height,width and format to generated a cache keys
		content = cache.get(key)	#from cache get the key
		if content is None:
			image = Image.new('RGB',(width,height))
			draw = ImageDraw.Draw(image)
			text = '{} x {}'.format(width,height)
			textwidth,textheight = draw.textsize(text)
			if textwidth < width and textheight < height:
				texttop = (height - textheight) // 2
				textleft = (width - textwidth) // 2
				draw.text((textleft,texttop),text,fill(255,255,255))
			content = BytesIO()
			image.save(content,image_format)
			content.seek(0)
			cache.set(key,content,60*60)		#if this key is None,will save this cache with key,value and save's time
		return content


'''
def placeholder(request,width,height):
	form = ImageForm({'height':height,'width':width})
	if form.is_valid():
		image = form.generate()	#use form.generate to get this picture
		# EODO:Generate image of requested size
		return HttpResponse(image,content_type='image/png')
	else:
		return HttpResponseBadRequest('Invalid Image Request')
'''


def index(request):
	return  HttpResponse('Hello world')

def generate_etag(request,width,height):
	content = 'Placeholder:{0} x {1}'.format(width,height)
	return hashlib.sha1(content.encode('utf-8')).hexdigest()

@etag(generate_etag)
def placeholder(request,width,height):
	form = ImageForm({'height':height,'width':width})
	if form.is_valid():
		image = form.generate()	#use form.generate to get this picture
		# EODO:Generate image of requested size
		return HttpResponse(image,content_type='image/png')
	else:
		return HttpResponseBadRequest('Invalid Image Request')

urlpatterns = (
	url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$',placeholder,name='placeholder'),
	url(r'^$',index,name='homepage'),
)

if __name__ == '__main__':
	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
