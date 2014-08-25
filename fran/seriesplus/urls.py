from django.conf.urls import patterns, include, url
from seriesplus.views import auth_token, login, principal, obtener_user
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fran.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^auth$', auth_token),
    url(r'^login$', login),
    url(r'^obtener$', obtener_user),
    url(r'^$', principal),
)


