from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import json
import urllib2
import urllib
from django.core.files import File
from django.core.context_processors import csrf

# Create your views here.

f_auth = open('/home/fran/GitHub/seriesplus-django/fran/seriesplus/auth.txt','r')
myfile_auth = File(f_auth)
auth = myfile_auth.readline()

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
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)

def get_user(request):
        username = request.POST['username']
        password = request.POST['password']
        url = "http://api.series.ly/v2/user/user_token"
        values = {'auth_token':auth, 'username':username, 'password':password, 'remember':'1'}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        read = response.read()
        jresp = json.loads(read)
        print auth_token
        print jresp
        if 'user_token' in jresp:
                if len(jresp['user_token']) > 0:
                        user_token = jresp['user_token']
                        response = HttpResponse("user_token %s" % user_token)
                        response.set_cookie('user_token', user_token)

                        # data = fseriesfollowing(user_token)
                        # print data
                        return HttpResponseRedirect('/seriesplus')            
        else:
                return HttpResponse('MAL')

def principal(request):
        if request.COOKIES.get("user_token"):
                data_raw = fseriesfollowing(request.COOKIES.get("user_token"))
                print data_raw
                return render_to_response('inicio.html',{'data_raw':data_raw})

 
def fseriesfollowing(user_token):
        url = 'http://api.series.ly/v2/user/media/pending'
        values = {'auth_token':auth,'user_token':user_token}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        read = response.read()
        jresp = json.loads(read)
        return jresp

