from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
import urllib2
from django.core.files import File

# Create your views here.

def auth_token(request):
        f_auth = open('/home/fran/GitHub/seriesplus-django/fran/seriesplus/auth.txt','w')
        f_secret = open('/home/fran/GitHub/seriesplus-django/fran/seriesplus/secret.txt','r')
        myfile_auth = File(f_auth)
        myfile_secret = File(f_secret)
        secret = myfile_secret.readline()
        id_api = '2132'
        resp = urllib2.urlopen("http://api.series.ly/v2/auth_token/?id_api=%s&secret=%s" % (id_api, secret))
        read = resp.read()
        jresp = json.loads(read)
        auth = jresp["auth_token"]
        myfile_auth.write(str(auth))
        print auth
	return HttpResponse('Done')


def login(request):
        return render_to_response('login.html')

def get_user(request):
        if request.method == 'POST':
                user = request.POST['username']
        elif request.method == 'GET':
                user = request.GET['username']
        print user
        return HttpResponse('get_user done')
